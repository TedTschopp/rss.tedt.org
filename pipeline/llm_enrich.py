from datetime import datetime, timezone
import os
from typing import Any, cast

from .constants import DEFAULT_PIPELINE_CONFIG
from .github_models_limits import (
    llm_call_limits,
    llm_global_daily_request_cap,
    normalize_llm_provider,
    rate_limit_state_for_model,
    seed_global_daily_state_from_call_log,
    seed_model_daily_states_from_call_log,
)
from .io_utils import append_jsonl
from .llm_client import GitHubModelsClient, LLMProviderConfigError, OpenAIAPIClient
from .llm_rate_limit import RateLimitBudgetExceeded
from .llm_rate_limit import call_with_retry as _call_with_retry
from .llm_rate_limit import is_auth_or_permission_exception as _is_auth_or_permission_exception
from .llm_rate_limit import status_code_from_exception as _status_code_from_exception
from .text_utils import to_iso


def _resolve_models_token() -> str:
    return (
        os.environ.get("GH_MODELS_TOKEN", "").strip()
        or os.environ.get("GH_Models_Token", "").strip()
    )


def _resolve_llm_client(cfg: dict[str, Any]):
    provider = normalize_llm_provider(cfg.get("llm_provider", "github_models"))
    timeout_sec = int(cfg.get("request_timeout_sec", 25))
    if provider == "openai":
        try:
            return (
                OpenAIAPIClient.from_env(
                    endpoint=str(cfg.get("openai_base_url") or "https://api.openai.com/v1"),
                    timeout_sec=timeout_sec,
                ),
                None,
                "OpenAI",
            )
        except LLMProviderConfigError as exc:
            return None, str(exc), "OpenAI"

    token = _resolve_models_token()
    if not token:
        return None, "missing GH_MODELS_TOKEN or GH_Models_Token", "GitHub Models"
    return GitHubModelsClient(token=token, timeout_sec=timeout_sec), None, "GitHub Models"


def _as_story_text(story: dict[str, Any], key: str) -> str:
    return str(story.get(key, "") or "")


def enrich_stories(
    stories: list[dict[str, Any]],
    llm_cache: dict[str, dict[str, Any]],
    llm_call_log_path: str,
    config: dict[str, Any] | None = None,
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, Any]]:
    cfg = {**DEFAULT_PIPELINE_CONFIG, **(config or {})}
    client, client_error, provider_label = _resolve_llm_client(cfg)
    if client is None:
        return stories, llm_cache, {"status": "skipped", "reason": client_error or "missing LLM credentials", "provider": provider_label, "calls": 0}

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
    fail_fast_auth = str(cfg.get("github_models_fail_fast_auth", True)).strip().lower() not in {"0", "false", "no", "off"}
    embed_model = str(cfg.get("embedding_model", "openai/text-embedding-3-small"))
    summary_model = str(cfg.get("summary_model", "openai/gpt-4.1-mini"))
    call_rows: list[dict[str, Any]] = []
    rate_limit_states: dict[str, dict[str, Any]] = seed_model_daily_states_from_call_log(llm_call_log_path)
    global_daily_max_calls = llm_global_daily_request_cap(cfg)
    global_daily_rate_limit_state = (
        seed_global_daily_state_from_call_log(llm_call_log_path) if global_daily_max_calls > 0 else None
    )

    def _model_call(model: str, call) -> tuple[dict[str, Any], dict[str, Any]]:
        limits = llm_call_limits(cfg, model)
        return _call_with_retry(
            call,
            max_attempts=retry_max_attempts,
            base_delay_sec=retry_base_delay_sec,
            max_delay_sec=retry_max_delay_sec,
            jitter_sec=retry_jitter_sec,
            rate_limit_state=rate_limit_state_for_model(rate_limit_states, model),
            rate_limit_window_sec=rate_limit_window_sec,
            rate_limit_threshold=rate_limit_threshold,
            rate_limit_cooldown_base_sec=rate_limit_cooldown_base_sec,
            rate_limit_cooldown_max_sec=rate_limit_cooldown_max_sec,
            request_rate_limit_window_sec=60.0,
            request_rate_limit_max_calls=limits.requests_per_minute,
            request_rate_limit_min_interval_sec=limits.min_interval_sec,
            request_daily_max_calls=limits.requests_per_day,
            global_daily_max_calls=global_daily_max_calls,
            global_daily_rate_limit_state=global_daily_rate_limit_state,
        )

    def _append_and_return(status: str, reason: str | None = None) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]], dict[str, Any]]:
        append_jsonl(llm_call_log_path, call_rows)
        ok_count = sum(1 for row in call_rows if row.get("status") == "ok")
        error_count = sum(1 for row in call_rows if row.get("status") == "error")
        skipped_count = sum(1 for row in call_rows if row.get("status") == "skipped")
        meta: dict[str, Any] = {
            "status": status,
            "calls": len(call_rows),
            "ok": ok_count,
            "errors": error_count,
            "skipped": skipped_count,
        }
        if reason:
            meta["reason"] = reason
        return stories, llm_cache, meta

    target_stories = stories[:top_n]
    embed_inputs = [f"{_as_story_text(story, 'title')}\n\n{_as_story_text(story, 'summary')}".strip() for story in target_stories]
    if embed_inputs:
        try:
            embed_result, retry_meta = _model_call(
                embed_model,
                lambda: client.embed(embed_inputs, model=embed_model),
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
            status = "skipped" if isinstance(exc, RateLimitBudgetExceeded) else "error"
            call_rows.append(
                {
                    "ts": to_iso(datetime.now(timezone.utc)),
                    "kind": "embeddings",
                    "model": embed_model,
                    "status": status,
                    "error": str(exc),
                    "status_code": _status_code_from_exception(exc),
                }
            )
            if isinstance(exc, RateLimitBudgetExceeded):
                return _append_and_return("deferred", f"{provider_label.lower()} daily request budget exhausted")
            if fail_fast_auth and _is_auth_or_permission_exception(exc):
                return _append_and_return("error", f"{provider_label.lower()} authentication or permission failure")

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
            result, retry_meta = _model_call(
                summary_model,
                lambda: client.summarize(_as_story_text(story, "title"), _as_story_text(story, "summary"), model=summary_model),
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
            status = "skipped" if isinstance(exc, RateLimitBudgetExceeded) else "error"
            call_rows.append(
                {
                    "ts": to_iso(datetime.now(timezone.utc)),
                    "kind": "chat",
                    "story_id": story_id,
                    "model": summary_model,
                    "status": status,
                    "error": str(exc),
                    "status_code": _status_code_from_exception(exc),
                }
            )
            if isinstance(exc, RateLimitBudgetExceeded):
                return _append_and_return("deferred", f"{provider_label.lower()} daily request budget exhausted")
            if fail_fast_auth and _is_auth_or_permission_exception(exc):
                return _append_and_return("error", f"{provider_label.lower()} authentication or permission failure")

    ok_count = sum(1 for row in call_rows if row.get("status") == "ok")
    error_count = sum(1 for row in call_rows if row.get("status") == "error")
    status = "ok" if error_count == 0 else ("degraded" if ok_count > 0 else "error")
    return _append_and_return(status)
