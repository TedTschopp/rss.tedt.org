from datetime import datetime, timezone
import os
import random
import time
from typing import Any, cast

from .constants import DEFAULT_PIPELINE_CONFIG
from .io_utils import append_jsonl
from .llm_client import GitHubModelsClient
from .text_utils import to_iso


def _resolve_models_token() -> str:
    return (
        os.environ.get("GH_MODELS_TOKEN", "").strip()
        or os.environ.get("GH_Models_Token", "").strip()
    )


def _as_story_text(story: dict[str, Any], key: str) -> str:
    return str(story.get(key, "") or "")


def _status_code_from_exception(exc: Exception) -> int | None:
    response = getattr(exc, "response", None)
    if response is None:
        return None
    status = getattr(response, "status_code", None)
    if isinstance(status, int):
        return status
    return None


def _retry_after_seconds(exc: Exception) -> float | None:
    response = getattr(exc, "response", None)
    if response is None:
        return None
    headers = getattr(response, "headers", None)
    if not headers:
        return None
    retry_after = headers.get("Retry-After")
    if retry_after is None:
        return None
    try:
        return float(retry_after)
    except Exception:
        return None


def _is_retryable_exception(exc: Exception) -> bool:
    status_code = _status_code_from_exception(exc)
    if status_code in {429, 500, 502, 503, 504}:
        return True
    text = str(exc).lower()
    return "too many requests" in text or "timed out" in text


def _rate_limit_wait_if_needed(state: dict[str, Any]) -> None:
    now = time.time()
    cooldown_until = float(state.get("cooldown_until", 0.0) or 0.0)
    if now < cooldown_until:
        time.sleep(max(0.0, cooldown_until - now))


def _rate_limit_note_429(
    state: dict[str, Any],
    *,
    window_sec: float,
    threshold: int,
    cooldown_base_sec: float,
    cooldown_max_sec: float,
    retry_after_sec: float | None,
) -> None:
    now = time.time()
    recent = state.setdefault("recent_429", [])
    if not isinstance(recent, list):
        recent = []
        state["recent_429"] = recent
    recent.append(now)
    cutoff = now - float(max(1.0, window_sec))
    state["recent_429"] = [t for t in recent if isinstance(t, (int, float)) and t >= cutoff]

    if len(state["recent_429"]) < int(max(1, threshold)):
        return

    strikes = int(state.get("cooldown_strikes", 0) or 0) + 1
    state["cooldown_strikes"] = strikes
    cooldown = min(float(cooldown_max_sec), float(cooldown_base_sec) * (2 ** (strikes - 1)))
    if retry_after_sec is not None:
        cooldown = max(cooldown, float(retry_after_sec))
    cooldown = min(float(cooldown_max_sec), cooldown + (0.1 * cooldown))
    state["cooldown_until"] = max(float(state.get("cooldown_until", 0.0) or 0.0), now + cooldown)


def _call_with_retry(
    call,
    max_attempts: int,
    base_delay_sec: float,
    max_delay_sec: float,
    jitter_sec: float,
    rate_limit_state: dict[str, Any] | None = None,
    rate_limit_window_sec: float = 60.0,
    rate_limit_threshold: int = 5,
    rate_limit_cooldown_base_sec: float = 45.0,
    rate_limit_cooldown_max_sec: float = 300.0,
) -> tuple[Any, dict[str, Any]]:
    retries = 0
    state = rate_limit_state if isinstance(rate_limit_state, dict) else None
    for attempt in range(1, max_attempts + 1):
        try:
            if state is not None:
                _rate_limit_wait_if_needed(state)
            result = call()
            if state is not None:
                state["recent_429"] = []
                state["cooldown_strikes"] = 0
            return result, {"attempt": attempt, "retries": retries}
        except Exception as exc:
            retryable = _is_retryable_exception(exc)
            if attempt >= max_attempts or not retryable:
                status_code = _status_code_from_exception(exc)
                raise RuntimeError(
                    f"llm_call_failed attempt={attempt} retries={retries} status={status_code} error={exc}"
                ) from exc

            status_code = _status_code_from_exception(exc)
            retry_after = _retry_after_seconds(exc)
            if state is not None and status_code == 429:
                _rate_limit_note_429(
                    state,
                    window_sec=rate_limit_window_sec,
                    threshold=rate_limit_threshold,
                    cooldown_base_sec=rate_limit_cooldown_base_sec,
                    cooldown_max_sec=rate_limit_cooldown_max_sec,
                    retry_after_sec=retry_after,
                )
            if retry_after is not None:
                delay = min(max_delay_sec, max(0.0, retry_after))
            else:
                delay = min(max_delay_sec, base_delay_sec * (2 ** (attempt - 1)) + random.uniform(0.0, jitter_sec))

            if state is not None:
                cooldown_until = float(state.get("cooldown_until", 0.0) or 0.0)
                cooldown_remaining = max(0.0, cooldown_until - time.time())
                delay = max(float(delay), cooldown_remaining)
            time.sleep(delay)
            retries += 1

    raise RuntimeError("llm_call_failed exhausted retries")


def enrich_stories(
    stories: list[dict[str, Any]],
    llm_cache: dict[str, dict[str, Any]],
    llm_call_log_path: str,
    config: dict[str, Any] | None = None,
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, Any]]:
    cfg = {**DEFAULT_PIPELINE_CONFIG, **(config or {})}
    token = _resolve_models_token()
    if not token:
        return stories, llm_cache, {"status": "skipped", "reason": "missing GH_MODELS_TOKEN or GH_Models_Token", "calls": 0}

    top_n = int(cfg.get("llm_top_n", 50))
    chat_max_calls = int(cfg.get("llm_chat_max_calls", 25))
    retry_max_attempts = int(cfg.get("llm_retry_max_attempts", 4))
    retry_base_delay_sec = float(cfg.get("llm_retry_base_delay_sec", 1.5))
    retry_max_delay_sec = float(cfg.get("llm_retry_max_delay_sec", 20.0))
    retry_jitter_sec = float(cfg.get("llm_retry_jitter_sec", 0.8))
    rate_limit_window_sec = float(cfg.get("llm_429_window_sec", 60))
    rate_limit_threshold = int(cfg.get("llm_429_threshold", 5))
    rate_limit_cooldown_base_sec = float(cfg.get("llm_429_cooldown_base_sec", 45.0))
    rate_limit_cooldown_max_sec = float(cfg.get("llm_429_cooldown_max_sec", 300.0))
    client = GitHubModelsClient(token=token, timeout_sec=int(cfg.get("request_timeout_sec", 25)))
    call_rows: list[dict[str, Any]] = []
    rate_limit_state: dict[str, Any] = {}

    target_stories = stories[:top_n]
    embed_inputs = [f"{_as_story_text(story, 'title')}\n\n{_as_story_text(story, 'summary')}".strip() for story in target_stories]
    if embed_inputs:
        try:
            embed_result, retry_meta = _call_with_retry(
                lambda: client.embed(embed_inputs),
                max_attempts=retry_max_attempts,
                base_delay_sec=retry_base_delay_sec,
                max_delay_sec=retry_max_delay_sec,
                jitter_sec=retry_jitter_sec,
                rate_limit_state=rate_limit_state,
                rate_limit_window_sec=rate_limit_window_sec,
                rate_limit_threshold=rate_limit_threshold,
                rate_limit_cooldown_base_sec=rate_limit_cooldown_base_sec,
                rate_limit_cooldown_max_sec=rate_limit_cooldown_max_sec,
            )
            vectors = cast(list[Any], embed_result.get("vectors", []))
            for index, story in enumerate(target_stories):
                story_id = str(story["story_id"])
                vector: list[Any] = []
                if index < len(vectors):
                    maybe_vector = vectors[index]
                    if isinstance(maybe_vector, list):
                        vector = cast(list[Any], maybe_vector)
                llm_cache.setdefault(story_id, {})["embedding"] = vector
                story_llm = story.setdefault("llm", {})
                if isinstance(story_llm, dict):
                    story_llm["embedding_dim"] = len(vector)

            call_rows.append(
                {
                    "ts": to_iso(datetime.now(timezone.utc)),
                    "kind": "embeddings",
                    "model": embed_result["model"],
                    "latency_ms": embed_result["latency_ms"],
                    "usage": embed_result.get("usage", {}),
                    "input_hash": embed_result["input_hash"],
                    "status": "ok",
                    "retries": retry_meta.get("retries", 0),
                }
            )
        except Exception as exc:
            call_rows.append(
                {
                    "ts": to_iso(datetime.now(timezone.utc)),
                    "kind": "embeddings",
                    "status": "error",
                    "error": str(exc),
                    "status_code": _status_code_from_exception(exc),
                }
            )

    for story in target_stories[:chat_max_calls]:
        story_id = str(story["story_id"])
        cache_entry = llm_cache.setdefault(story_id, {})
        if cache_entry.get("summary") and cache_entry.get("topics"):
            existing_llm = story.get("llm", {})
            if not isinstance(existing_llm, dict):
                existing_llm = {}
            story["llm"] = {
                "summary": cache_entry.get("summary"),
                "topics": cache_entry.get("topics", []),
                "entities": cache_entry.get("entities", []),
                **existing_llm,
            }
            continue

        try:
            result, retry_meta = _call_with_retry(
                lambda: client.summarize(_as_story_text(story, "title"), _as_story_text(story, "summary")),
                max_attempts=retry_max_attempts,
                base_delay_sec=retry_base_delay_sec,
                max_delay_sec=retry_max_delay_sec,
                jitter_sec=retry_jitter_sec,
                rate_limit_state=rate_limit_state,
                rate_limit_window_sec=rate_limit_window_sec,
                rate_limit_threshold=rate_limit_threshold,
                rate_limit_cooldown_base_sec=rate_limit_cooldown_base_sec,
                rate_limit_cooldown_max_sec=rate_limit_cooldown_max_sec,
            )
            cache_entry.update(
                {
                    "summary": result.get("summary", ""),
                    "topics": result.get("topics", []),
                    "entities": result.get("entities", []),
                }
            )
            existing_llm = story.get("llm", {})
            if not isinstance(existing_llm, dict):
                existing_llm = {}
            story["llm"] = {
                "summary": cache_entry.get("summary"),
                "topics": cache_entry.get("topics", []),
                "entities": cache_entry.get("entities", []),
                **existing_llm,
            }
            call_rows.append(
                {
                    "ts": to_iso(datetime.now(timezone.utc)),
                    "kind": "chat",
                    "story_id": story_id,
                    "model": result.get("model"),
                    "latency_ms": result.get("latency_ms"),
                    "usage": result.get("usage", {}),
                    "input_hash": result.get("input_hash"),
                    "status": "ok",
                    "retries": retry_meta.get("retries", 0),
                }
            )
        except Exception as exc:
            call_rows.append(
                {
                    "ts": to_iso(datetime.now(timezone.utc)),
                    "kind": "chat",
                    "story_id": story_id,
                    "status": "error",
                    "error": str(exc),
                    "status_code": _status_code_from_exception(exc),
                }
            )

    append_jsonl(llm_call_log_path, call_rows)
    return stories, llm_cache, {"status": "ok", "calls": len(call_rows)}
