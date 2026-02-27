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


def _call_with_retry(
    call,
    max_attempts: int,
    base_delay_sec: float,
    max_delay_sec: float,
    jitter_sec: float,
) -> tuple[Any, dict[str, Any]]:
    retries = 0
    for attempt in range(1, max_attempts + 1):
        try:
            result = call()
            return result, {"attempt": attempt, "retries": retries}
        except Exception as exc:
            retryable = _is_retryable_exception(exc)
            if attempt >= max_attempts or not retryable:
                status_code = _status_code_from_exception(exc)
                raise RuntimeError(
                    f"llm_call_failed attempt={attempt} retries={retries} status={status_code} error={exc}"
                ) from exc

            retry_after = _retry_after_seconds(exc)
            if retry_after is not None:
                delay = min(max_delay_sec, max(0.0, retry_after))
            else:
                delay = min(max_delay_sec, base_delay_sec * (2 ** (attempt - 1)) + random.uniform(0.0, jitter_sec))
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
    client = GitHubModelsClient(token=token, timeout_sec=int(cfg.get("request_timeout_sec", 25)))
    call_rows: list[dict[str, Any]] = []

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
