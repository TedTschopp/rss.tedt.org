from datetime import datetime, timezone
from collections.abc import Callable
import hashlib
import json
import os
import re
import time
from typing import Any, cast

from scripts.feed_generator import MultiFeedGenerator

from .article_content import fetch_article_markdown
from .constants import DEFAULT_PIPELINE_CONFIG
from .io_utils import append_jsonl, write_json
from .llm_client import GitHubModelsClient
from .text_utils import parse_datetime, to_iso


IMPORTANCE_RUBRIC_PATH = "Docs/reference/business-and-technical-importance-rubric.md"
AI_RELEVANCE_RUBRIC_PATH = "Docs/reference/ai-relevance-rubric.md"


def _resolve_models_token() -> str:
    return (
        os.environ.get("GH_MODELS_TOKEN", "").strip()
        or os.environ.get("GH_Models_Token", "").strip()
    )


def _read_text_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return handle.read().strip()
    except Exception:
        return ""


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
    recent_raw = state.setdefault("recent_429", [])
    if isinstance(recent_raw, list):
        recent = cast(list[Any], recent_raw)
    else:
        recent = []
        state["recent_429"] = recent
    recent.append(now)
    # Trim outside the window
    cutoff = now - float(max(1.0, window_sec))
    state["recent_429"] = [t for t in recent if isinstance(t, (int, float)) and t >= cutoff]

    if len(state["recent_429"]) < int(max(1, threshold)):
        return

    strikes = int(state.get("cooldown_strikes", 0) or 0) + 1
    state["cooldown_strikes"] = strikes
    cooldown = min(float(cooldown_max_sec), float(cooldown_base_sec) * (2 ** (strikes - 1)))
    if retry_after_sec is not None:
        cooldown = max(cooldown, float(retry_after_sec))
    # Add a touch of jitter so we don't re-sync with other callers.
    cooldown = min(float(cooldown_max_sec), cooldown + (0.1 * cooldown))
    state["cooldown_until"] = max(float(state.get("cooldown_until", 0.0) or 0.0), now + cooldown)


def _call_with_retry(
    call: Callable[[], Any],
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
                delay = min(max_delay_sec, base_delay_sec * (2 ** (attempt - 1)) + (jitter_sec * (attempt / max_attempts)))

            if state is not None:
                cooldown_until = float(state.get("cooldown_until", 0.0) or 0.0)
                cooldown_remaining = max(0.0, cooldown_until - time.time())
                delay = max(float(delay), cooldown_remaining)

            time.sleep(delay)
            retries += 1

    raise RuntimeError("llm_call_failed exhausted retries")


def _rubric_hash(markdown: str) -> str:
    return hashlib.sha1((markdown or "").encode("utf-8")).hexdigest()


def _ai_relevance_context_hash(title: str, summary: str, article: str, rubric_hash: str, model: str) -> str:
    raw = json.dumps(
        {
            "title": title,
            "summary": summary,
            "article": article,
            "rubric_hash": rubric_hash,
            "model": model,
        },
        sort_keys=True,
        ensure_ascii=False,
    )
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _ai_relevance_allows_grading(relevance: dict[str, Any] | None) -> bool:
    if not relevance:
        return False
    decision = str(relevance.get("decision") or "").strip().lower()
    return bool(relevance.get("is_ai_related")) and decision == "proceed"


BUSINESS_TAGS = {1: "[ ~ ]", 2: "[ * ]", 3: "[ ! ]"}
TECHNICAL_TAGS = {1: "[ ◻ ]", 2: "[ ◼ ]", 3: "[ ⬢ ]"}
ALL_TAG_STRINGS = list(BUSINESS_TAGS.values()) + list(TECHNICAL_TAGS.values())


def _strip_trailing_importance_tags(title: str) -> str:
    if not title:
        return ""
    cleaned = str(title)
    while True:
        stripped = cleaned.rstrip()
        removed = False
        for tag in ALL_TAG_STRINGS:
            if stripped.endswith(tag):
                cleaned = stripped[: -len(tag)].rstrip()
                removed = True
                break
        if not removed:
            return cleaned


def _importance_tags(importance: dict[str, Any] | None) -> tuple[str | None, str | None]:
    if not importance:
        return None, None
    business_level = importance.get("business_level")
    technical_level = importance.get("technical_level")
    try:
        business_level_int = int(str(business_level or "0"))
        technical_level_int = int(str(technical_level or "0"))
    except Exception:
        return None, None
    return BUSINESS_TAGS.get(business_level_int), TECHNICAL_TAGS.get(technical_level_int)


def _eligible_for_importance_backfill(published: str, backfill_days: int) -> bool:
    published_dt = parse_datetime(published)
    if not published_dt:
        return True
    now = datetime.now(timezone.utc)
    age_days = (now - published_dt).total_seconds() / 86400.0
    return age_days <= float(max(0, backfill_days))


def _is_ai_story(story: dict[str, Any], ai_keywords: list[str]) -> bool:
    def keyword_match(text: str) -> bool:
        lowered_text = text.lower()
        for keyword in ai_keywords:
            escaped = re.escape(keyword)
            if re.search(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])", lowered_text):
                return True
        return False

    llm = story.get("llm")
    if isinstance(llm, dict):
        llm_map = cast(dict[str, Any], llm)
        llm_topics_raw = llm_map.get("topics", [])
    else:
        llm_topics_raw = []
    llm_topics = cast(list[Any], llm_topics_raw) if isinstance(llm_topics_raw, list) else []
    if any(keyword_match(str(topic)) for topic in llm_topics):
        return True

    title = str(story.get("title", "")).lower()
    summary = str(story.get("summary", "")).lower()
    domain = str(story.get("domain", "")).lower()
    haystack = f"{title}\n{summary}\n{domain}"
    return keyword_match(haystack)


def _to_feed_entry(story: dict[str, Any]) -> dict[str, Any]:
    base_title = _strip_trailing_importance_tags(story.get("title", ""))
    importance_raw = story.get("importance")
    importance = cast(dict[str, Any], importance_raw) if isinstance(importance_raw, dict) else None
    business_tag, technical_tag = _importance_tags(importance)
    if business_tag and technical_tag:
        title = f"{base_title} {business_tag} {technical_tag}".strip()
    else:
        title = base_title
    return {
        "title": title,
        "link": story.get("canonical_url") or story.get("url", ""),
        "description": _story_summary(story),
        "pub_date": story.get("published"),
        "guid": story.get("story_id"),
    }


def _story_summary(story: dict[str, Any]) -> str:
    llm = story.get("llm")
    if isinstance(llm, dict):
        llm_map = cast(dict[str, Any], llm)
        llm_summary = llm_map.get("summary")
        if llm_summary:
            return str(llm_summary)
    return str(story.get("summary") or "")


def _sum_mentions(story: dict[str, Any], key: str) -> int | None:
    mentions = story.get("mentions", [])
    if not isinstance(mentions, list):
        return None
    mention_values = cast(list[Any], mentions)
    total = 0
    for mention in mention_values:
        if not isinstance(mention, dict):
            continue
        mention_map = cast(dict[str, Any], mention)
        try:
            total += max(0, int(mention_map.get(key) or 0))
        except Exception:
            continue
    return total or None


def publish_outputs(
    ranked_stories: list[dict[str, Any]],
    api_path: str,
    base_feed_path: str,
    llm_cache: dict[str, dict[str, Any]] | None = None,
    llm_call_log_path: str | None = None,
    config: dict[str, Any] | None = None,
)-> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    cfg: dict[str, Any] = {**DEFAULT_PIPELINE_CONFIG, **(config or {})}
    publish_top_n = int(cfg.get("publish_top_n", 200))
    raw_ai_keywords = cfg.get("ai_keywords", [])
    ai_keyword_values = cast(list[Any], raw_ai_keywords) if isinstance(raw_ai_keywords, list) else []
    ai_keywords = [str(keyword).lower() for keyword in ai_keyword_values]
    ai_only_stories: list[dict[str, Any]] = [story for story in ranked_stories if _is_ai_story(story, ai_keywords)]
    top_stories: list[dict[str, Any]] = ai_only_stories[:publish_top_n]

    importance_backfill_days = int(cfg.get("importance_backfill_days", 7))
    ai_relevance_model = str(cfg.get("ai_relevance_model", "openai/gpt-4.1-mini"))
    importance_model = str(cfg.get("importance_model", "openai/gpt-4.1-mini"))
    article_fetch_timeout_sec = int(cfg.get("article_fetch_timeout_sec", cfg.get("request_timeout_sec", 25)))
    article_max_chars = int(cfg.get("article_max_chars", 12000))
    retry_max_attempts = int(cfg.get("llm_retry_max_attempts", 4))
    retry_base_delay_sec = float(cfg.get("llm_retry_base_delay_sec", 1.5))
    retry_max_delay_sec = float(cfg.get("llm_retry_max_delay_sec", 20.0))
    retry_jitter_sec = float(cfg.get("llm_retry_jitter_sec", 0.8))
    rate_limit_window_sec = float(cfg.get("llm_429_window_sec", 60))
    rate_limit_threshold = int(cfg.get("llm_429_threshold", 5))
    rate_limit_cooldown_base_sec = float(cfg.get("llm_429_cooldown_base_sec", 45.0))
    rate_limit_cooldown_max_sec = float(cfg.get("llm_429_cooldown_max_sec", 300.0))

    if llm_cache is None:
        llm_cache = {}

    rubric_markdown = _read_text_file(IMPORTANCE_RUBRIC_PATH)
    rubric_hash = _rubric_hash(rubric_markdown) if rubric_markdown else ""
    ai_relevance_rubric = _read_text_file(AI_RELEVANCE_RUBRIC_PATH)
    ai_relevance_rubric_hash = _rubric_hash(ai_relevance_rubric) if ai_relevance_rubric else ""
    token = _resolve_models_token()
    client = GitHubModelsClient(token=token, timeout_sec=int(cfg.get("request_timeout_sec", 25))) if token else None
    call_rows: list[dict[str, Any]] = []
    rate_limit_state: dict[str, Any] = {}

    for story in top_stories:
        story_id = str(story.get("story_id") or "").strip()
        if not story_id:
            continue
        cache_entry = llm_cache.setdefault(story_id, {})
        existing_importance_raw = cache_entry.get("importance")
        existing_importance = cast(dict[str, Any], existing_importance_raw) if isinstance(existing_importance_raw, dict) else None

        existing_relevance_raw = cache_entry.get("ai_relevance")
        existing_relevance = cast(dict[str, Any], existing_relevance_raw) if isinstance(existing_relevance_raw, dict) else None

        if not rubric_markdown or not rubric_hash:
            continue

        if not ai_relevance_rubric or not ai_relevance_rubric_hash:
            continue

        if not _eligible_for_importance_backfill(str(story.get("published") or ""), importance_backfill_days):
            continue

        if client is None:
            if isinstance(existing_relevance, dict):
                story["ai_relevance"] = existing_relevance
            if isinstance(existing_importance, dict):
                story["importance"] = existing_importance
            continue
        importance_client = client

        title_text = str(story.get("title") or "")
        context_text = _story_summary(story)
        article_url = str(story.get("canonical_url") or story.get("url") or "")
        article_markdown = fetch_article_markdown(
            article_url,
            timeout_sec=article_fetch_timeout_sec,
            max_chars=article_max_chars,
        )
        relevance_context_hash = _ai_relevance_context_hash(
            title_text,
            context_text,
            article_markdown,
            ai_relevance_rubric_hash,
            ai_relevance_model,
        )
        relevance_payload: dict[str, Any] | None = existing_relevance
        if not isinstance(relevance_payload, dict) or str(relevance_payload.get("context_hash") or "") != relevance_context_hash:
            try:
                relevance_result, relevance_retry_meta = _call_with_retry(
                    lambda: importance_client.check_ai_relevance(
                        title_text,
                        context_text,
                        ai_relevance_rubric,
                        model=ai_relevance_model,
                        article=article_markdown,
                    ),
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
                relevance_payload = {
                    "is_ai_related": bool(relevance_result.get("is_ai_related")),
                    "decision": relevance_result.get("decision", ""),
                    "confidence": relevance_result.get("confidence", ""),
                    "primary_ai_topic": relevance_result.get("primary_ai_topic", ""),
                    "rationale": relevance_result.get("rationale", ""),
                    "evidence": relevance_result.get("evidence", []),
                    "rubric_hash": ai_relevance_rubric_hash,
                    "context_hash": relevance_context_hash,
                    "checked_at": to_iso(datetime.now(timezone.utc)),
                    "model": relevance_result.get("model"),
                    "input_hash": relevance_result.get("input_hash"),
                }
                cache_entry["ai_relevance"] = relevance_payload
                call_rows.append(
                    {
                        "ts": to_iso(datetime.now(timezone.utc)),
                        "kind": "ai_relevance",
                        "story_id": story_id,
                        "model": relevance_result.get("model"),
                        "latency_ms": relevance_result.get("latency_ms"),
                        "usage": relevance_result.get("usage", {}),
                        "input_hash": relevance_result.get("input_hash"),
                        "status": "ok",
                        "retries": relevance_retry_meta.get("retries", 0),
                    }
                )
            except Exception as exc:
                call_rows.append(
                    {
                        "ts": to_iso(datetime.now(timezone.utc)),
                        "kind": "ai_relevance",
                        "story_id": story_id,
                        "status": "error",
                        "error": str(exc),
                        "status_code": _status_code_from_exception(exc),
                    }
                )
                continue

        story["ai_relevance"] = relevance_payload
        if not _ai_relevance_allows_grading(relevance_payload):
            story.pop("importance", None)
            continue

        if isinstance(existing_importance, dict):
            story["importance"] = existing_importance

        should_grade = False
        if not isinstance(existing_importance, dict):
            should_grade = True
        else:
            if str(existing_importance.get("rubric_hash") or "") != rubric_hash:
                should_grade = True

        if not should_grade:
            continue

        try:
            result, retry_meta = _call_with_retry(
                lambda: importance_client.grade_importance(
                    title_text,
                    context_text,
                    rubric_markdown,
                    model=importance_model,
                    article=article_markdown,
                ),
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

            importance_payload: dict[str, Any] = {
                "business_level": result.get("business_level"),
                "technical_level": result.get("technical_level"),
                "business_impact": result.get("business_impact", ""),
                "technical_impact": result.get("technical_impact", ""),
                "risk_impact": result.get("risk_impact", ""),
                "enterprise_readiness": result.get("enterprise_readiness", ""),
                "labor_workflow_impact": result.get("labor_workflow_impact", ""),
                "confidence": result.get("confidence", ""),
                "attention_priority": result.get("attention_priority", ""),
                "development_summary": result.get("development_summary", ""),
                "reason_codes": result.get("reason_codes", []),
                "recommended_action": result.get("recommended_action", ""),
                "rationale": result.get("rationale", ""),
                "watch_items": result.get("watch_items", []),
                "business_rationale": result.get("business_rationale", ""),
                "technical_rationale": result.get("technical_rationale", ""),
                "rubric_hash": rubric_hash,
                "graded_at": to_iso(datetime.now(timezone.utc)),
                "model": result.get("model"),
                "input_hash": result.get("input_hash"),
            }
            cache_entry["importance"] = importance_payload
            story["importance"] = importance_payload

            call_rows.append(
                {
                    "ts": to_iso(datetime.now(timezone.utc)),
                    "kind": "importance",
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
                    "kind": "importance",
                    "story_id": story_id,
                    "status": "error",
                    "error": str(exc),
                    "status_code": _status_code_from_exception(exc),
                }
            )

    if llm_call_log_path and call_rows:
        append_jsonl(llm_call_log_path, call_rows)

    payload: dict[str, Any] = {
        "schema_version": cfg.get("schema_version", "1.0.0"),
        "generated": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "count": len(top_stories),
        "items": [
            {
                "title": story.get("title"),
                "url": story.get("canonical_url") or story.get("url"),
                "source": story.get("source_name"),
                "sourceType": story.get("source_type"),
                "published": story.get("published"),
                "summary": _story_summary(story),
                "score": story.get("score"),
                "upvotes": _sum_mentions(story, "upvotes"),
                "comments": _sum_mentions(story, "comments"),
                "clusterId": story.get("cluster_id"),
                "aiRelevance": story.get("ai_relevance"),
                "importance": story.get("importance"),
            }
            for story in top_stories
        ],
    }
    write_json(api_path, payload)

    feed = MultiFeedGenerator(
        title="TedTschopp News Graph - Top Stories",
        link="https://rss.tedt.org/feeds/top.xml",
        description="Natural20-style ranked stories across configured sources",
    )

    for story in top_stories:
        cast(Any, feed).add_item(**_to_feed_entry(story))

    cast(Any, feed).write_all_formats(base_feed_path)
    return payload, llm_cache
