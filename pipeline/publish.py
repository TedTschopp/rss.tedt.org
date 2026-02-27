from datetime import datetime, timezone
import hashlib
import os
import re
import time
from typing import Any

from feed_generator import MultiFeedGenerator

from .constants import DEFAULT_PIPELINE_CONFIG
from .io_utils import append_jsonl, write_json
from .llm_client import GitHubModelsClient
from .text_utils import parse_datetime, to_iso


IMPORTANCE_RUBRIC_PATH = "docs/Rules-for-Business-and-Technical-Importance.md"


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
                delay = min(max_delay_sec, base_delay_sec * (2 ** (attempt - 1)) + (jitter_sec * (attempt / max_attempts)))
            time.sleep(delay)
            retries += 1

    raise RuntimeError("llm_call_failed exhausted retries")


def _rubric_hash(markdown: str) -> str:
    return hashlib.sha1((markdown or "").encode("utf-8")).hexdigest()


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
    if not importance or not isinstance(importance, dict):
        return None, None
    business_level = importance.get("business_level")
    technical_level = importance.get("technical_level")
    try:
        business_level_int = int(business_level)
        technical_level_int = int(technical_level)
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

    llm_topics = story.get("llm", {}).get("topics", []) if isinstance(story.get("llm"), dict) else []
    if isinstance(llm_topics, list):
        if any(keyword_match(str(topic)) for topic in llm_topics):
            return True

    title = str(story.get("title", "")).lower()
    summary = str(story.get("summary", "")).lower()
    domain = str(story.get("domain", "")).lower()
    haystack = f"{title}\n{summary}\n{domain}"
    return keyword_match(haystack)


def _to_feed_entry(story: dict) -> dict:
    base_title = _strip_trailing_importance_tags(story.get("title", ""))
    business_tag, technical_tag = _importance_tags(story.get("importance"))
    if business_tag and technical_tag:
        title = f"{base_title} {business_tag} {technical_tag}".strip()
    else:
        title = base_title
    return {
        "title": title,
        "link": story.get("canonical_url") or story.get("url", ""),
        "description": story.get("llm", {}).get("summary") or story.get("summary", ""),
        "pub_date": story.get("published"),
        "guid": story.get("story_id"),
    }


def publish_outputs(
    ranked_stories: list[dict],
    api_path: str,
    base_feed_path: str,
    llm_cache: dict[str, dict[str, Any]] | None = None,
    llm_call_log_path: str | None = None,
    config: dict | None = None,
):
    cfg = {**DEFAULT_PIPELINE_CONFIG, **(config or {})}
    publish_top_n = int(cfg.get("publish_top_n", 200))
    ai_keywords = [str(keyword).lower() for keyword in cfg.get("ai_keywords", [])]
    ai_only_stories = [story for story in ranked_stories if _is_ai_story(story, ai_keywords)]
    top_stories = ai_only_stories[:publish_top_n]

    importance_backfill_days = int(cfg.get("importance_backfill_days", 7))
    importance_model = str(cfg.get("importance_model", "openai/gpt-4.1-mini"))
    retry_max_attempts = int(cfg.get("llm_retry_max_attempts", 4))
    retry_base_delay_sec = float(cfg.get("llm_retry_base_delay_sec", 1.5))
    retry_max_delay_sec = float(cfg.get("llm_retry_max_delay_sec", 20.0))
    retry_jitter_sec = float(cfg.get("llm_retry_jitter_sec", 0.8))

    if llm_cache is None:
        llm_cache = {}

    rubric_markdown = _read_text_file(IMPORTANCE_RUBRIC_PATH)
    rubric_hash = _rubric_hash(rubric_markdown) if rubric_markdown else ""
    token = _resolve_models_token()
    client = GitHubModelsClient(token=token, timeout_sec=int(cfg.get("request_timeout_sec", 25))) if token else None
    call_rows: list[dict[str, Any]] = []

    for story in top_stories:
        story_id = str(story.get("story_id") or "").strip()
        if not story_id:
            continue
        cache_entry = llm_cache.setdefault(story_id, {})
        existing_importance = cache_entry.get("importance") if isinstance(cache_entry, dict) else None

        if isinstance(existing_importance, dict):
            story["importance"] = existing_importance

        if not rubric_markdown or not rubric_hash:
            continue

        if not _eligible_for_importance_backfill(str(story.get("published") or ""), importance_backfill_days):
            continue

        should_grade = False
        if not isinstance(existing_importance, dict):
            should_grade = True
        else:
            if str(existing_importance.get("rubric_hash") or "") != rubric_hash:
                should_grade = True

        if not should_grade or client is None:
            continue

        title_text = str(story.get("title") or "")
        context_text = str(story.get("llm", {}).get("summary") or story.get("summary") or "")
        try:
            result, retry_meta = _call_with_retry(
                lambda: client.grade_importance(title_text, context_text, rubric_markdown, model=importance_model),
                max_attempts=retry_max_attempts,
                base_delay_sec=retry_base_delay_sec,
                max_delay_sec=retry_max_delay_sec,
                jitter_sec=retry_jitter_sec,
            )

            importance_payload = {
                "business_level": result.get("business_level"),
                "technical_level": result.get("technical_level"),
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

    payload = {
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
                "summary": story.get("llm", {}).get("summary") or story.get("summary"),
                "score": story.get("score"),
                "upvotes": sum(int(m.get("upvotes") or 0) for m in story.get("mentions", [])) or None,
                "comments": sum(int(m.get("comments") or 0) for m in story.get("mentions", [])) or None,
                "clusterId": story.get("cluster_id"),
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
        feed.add_item(**_to_feed_entry(story))

    feed.write_all_formats(base_feed_path)
    return payload, llm_cache
