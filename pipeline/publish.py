from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
import os
import re
from threading import Lock
from typing import Any, cast

from scripts.feed_generator import MultiFeedGenerator

from .article_content import fetch_article_markdown
from .constants import DEFAULT_PIPELINE_CONFIG
from .github_models_limits import (
    llm_call_limits,
    llm_global_daily_request_cap,
    normalize_llm_provider,
    rate_limit_state_for_model,
    seed_global_daily_state_from_call_log,
    seed_model_daily_states_from_call_log,
)
from .io_utils import append_jsonl, read_json, write_json
from .llm_client import GitHubModelsClient, LLMProviderConfigError, OpenAIAPIClient
from .llm_rate_limit import RateLimitBudgetExceeded
from .llm_rate_limit import call_with_retry as _call_with_retry
from .llm_rate_limit import is_auth_or_permission_exception as _is_auth_or_permission_exception
from .llm_rate_limit import status_code_from_exception as _status_code_from_exception
from .text_utils import parse_datetime, to_iso


IMPORTANCE_RUBRIC_PATH = "Docs/reference/business-and-technical-importance-rubric.md"
AI_RELEVANCE_RUBRIC_PATH = "Docs/reference/ai-relevance-rubric.md"
OUTPUT_CLEANUP_PROMPT_PATHS = [
    "Docs/design/Prompts-Needed/Headline-Generation-Instructions.md",
    "Docs/design/Prompts-Needed/Article-Summary.md",
    "prompts/output_cleanup/title_system.txt",
    "prompts/output_cleanup/title_user.txt",
    "prompts/output_cleanup/title_schema.json",
    "prompts/output_cleanup/description_system.txt",
    "prompts/output_cleanup/description_user.txt",
    "prompts/output_cleanup/description_schema.json",
]


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


def _read_text_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return handle.read().strip()
    except Exception:
        return ""


def _prompt_bundle_hash(paths: list[str]) -> str:
    raw = "\n\n".join(f"{path}\n{_read_text_file(path)}" for path in paths)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


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
    business_impact = str(importance.get("business_impact") or "").strip()
    technical_impact = str(importance.get("technical_impact") or "").strip()
    business_tag = business_impact if business_impact in BUSINESS_TAGS.values() else None
    technical_tag = technical_impact if technical_impact in TECHNICAL_TAGS.values() else None

    business_level = importance.get("business_level")
    technical_level = importance.get("technical_level")
    try:
        business_level_int = int(str(business_level or "0"))
        technical_level_int = int(str(technical_level or "0"))
    except Exception:
        return business_tag, technical_tag
    return business_tag or BUSINESS_TAGS.get(business_level_int), technical_tag or TECHNICAL_TAGS.get(technical_level_int)


def _normalize_importance_payload(importance: dict[str, Any] | None) -> dict[str, Any] | None:
    if not isinstance(importance, dict):
        return None
    normalized = dict(importance)
    business_tag, technical_tag = _importance_tags(normalized)
    if business_tag:
        normalized["business_impact"] = business_tag
    if technical_tag:
        normalized["technical_impact"] = technical_tag
    return normalized


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


def _story_title(story: dict[str, Any]) -> str:
    output_cleanup = story.get("output_cleanup")
    if isinstance(output_cleanup, dict):
        cleanup_map = cast(dict[str, Any], output_cleanup)
        title = str(cleanup_map.get("title") or "").strip()
        if title:
            return title
    return str(story.get("title") or "")


def _story_title_with_importance_tags(story: dict[str, Any]) -> str:
    base_title = _strip_trailing_importance_tags(_story_title(story))
    importance_raw = story.get("importance")
    importance = cast(dict[str, Any], importance_raw) if isinstance(importance_raw, dict) else None
    business_tag, technical_tag = _importance_tags(importance)
    title_parts = [base_title]
    title_parts.extend(tag for tag in (business_tag, technical_tag) if tag)
    return " ".join(part for part in title_parts if part).strip()


def _story_base_summary(story: dict[str, Any]) -> str:
    llm = story.get("llm")
    if isinstance(llm, dict):
        llm_map = cast(dict[str, Any], llm)
        llm_summary = llm_map.get("summary")
        if llm_summary:
            return str(llm_summary)
    return str(story.get("summary") or "")


def _story_summary(story: dict[str, Any]) -> str:
    output_cleanup = story.get("output_cleanup")
    if isinstance(output_cleanup, dict):
        cleanup_map = cast(dict[str, Any], output_cleanup)
        description = str(cleanup_map.get("description") or "").strip()
        if description:
            return description
    return _story_base_summary(story)


def _to_feed_entry(story: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": _story_title_with_importance_tags(story),
        "link": story.get("canonical_url") or story.get("url", ""),
        "description": _story_summary(story),
        "pub_date": story.get("published"),
        "guid": story.get("story_id"),
    }


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


def _article_excerpt(article_markdown: str, max_chars: int) -> str:
    article = str(article_markdown or "").strip()
    if not article or max_chars <= 0:
        return ""
    if len(article) <= max_chars:
        return article
    return article[:max_chars].rstrip() + "\n\n[truncated]"


def _source_context(story: dict[str, Any], article_markdown: str = "") -> str:
    payload = {
        "primary_source": story.get("primary_source")
        or {
            "source_id": story.get("primary_source_id"),
            "source_name": story.get("source_name"),
            "source_type": story.get("source_type"),
            "source_category": story.get("source_category"),
            "url": story.get("url"),
            "canonical_url": story.get("canonical_url"),
            "domain": story.get("domain"),
        },
        "sources": story.get("sources", []),
        "alternate_links": story.get("alternate_links", []),
        "duplicate_count": story.get("duplicate_count", 0),
        "duplicate_source_count": story.get("duplicate_source_count", 1),
    }
    if article_markdown:
        payload["article_markdown"] = article_markdown
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def _output_cleanup_context_hash(
    title: str,
    summary: str,
    source_context: str,
    prompt_hash: str,
    model: str,
) -> str:
    raw = json.dumps(
        {
            "title": title,
            "summary": summary,
            "source_context": source_context,
            "prompt_hash": prompt_hash,
            "model": model,
        },
        sort_keys=True,
        ensure_ascii=False,
    )
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _cached_output_cleanup(cache_entry: dict[str, Any], context_hash: str) -> dict[str, Any] | None:
    output_cleanup = cache_entry.get("output_cleanup")
    if not isinstance(output_cleanup, dict):
        return None
    cleanup_map = cast(dict[str, Any], output_cleanup)
    if cleanup_map.get("context_hash") != context_hash:
        return None
    if not cleanup_map.get("title") or not cleanup_map.get("description"):
        return None
    return cleanup_map


def _load_article_cache(path: str) -> dict[str, dict[str, Any]]:
    payload = read_json(path, {})
    if not isinstance(payload, dict):
        return {}
    cache: dict[str, dict[str, Any]] = {}
    for key, value in payload.items():
        if not isinstance(key, str) or not isinstance(value, dict):
            continue
        value_map = cast(dict[str, Any], value)
        markdown = str(value_map.get("markdown") or "")
        fetched_at = str(value_map.get("fetched_at") or "")
        fetch_failed = bool(value_map.get("fetch_failed"))
        if not fetched_at or (not markdown and not fetch_failed):
            continue
        cache[key] = {
            "markdown": markdown,
            "fetched_at": fetched_at,
            "fetch_failed": fetch_failed,
        }
    return cache


def _article_cache_fresh(entry: dict[str, Any], ttl_hours: int) -> bool:
    fetched_at = parse_datetime(str(entry.get("fetched_at") or ""))
    if not fetched_at:
        return False
    age_seconds = (datetime.now(timezone.utc) - fetched_at).total_seconds()
    return age_seconds <= max(0, int(ttl_hours)) * 3600


def _fetch_article_with_url(url: str, timeout_sec: int, max_chars: int) -> tuple[str, str]:
    markdown = fetch_article_markdown(url, timeout_sec=timeout_sec, max_chars=max_chars)
    return url, markdown


def _apply_output_cleanup(story: dict[str, Any], cleanup: dict[str, Any]) -> None:
    story["output_cleanup"] = cleanup


def publish_outputs(
    ranked_stories: list[dict[str, Any]],
    api_path: str,
    base_feed_path: str,
    llm_cache: dict[str, dict[str, Any]] | None = None,
    llm_call_log_path: str | None = None,
    llm_status: dict[str, Any] | None = None,
    config: dict[str, Any] | None = None,
)-> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    cfg: dict[str, Any] = {**DEFAULT_PIPELINE_CONFIG, **(config or {})}
    publish_top_n = int(cfg.get("publish_top_n", 200))
    llm_workers = max(1, int(cfg.get("llm_workers", 1)))
    raw_ai_keywords = cfg.get("ai_keywords", [])
    ai_keyword_values = cast(list[Any], raw_ai_keywords) if isinstance(raw_ai_keywords, list) else []
    ai_keywords = [str(keyword).lower() for keyword in ai_keyword_values]
    ai_only_stories: list[dict[str, Any]] = [story for story in ranked_stories if _is_ai_story(story, ai_keywords)]
    top_stories: list[dict[str, Any]] = ai_only_stories[:publish_top_n]

    importance_backfill_days = int(cfg.get("importance_backfill_days", 60))
    ai_relevance_model = str(cfg.get("ai_relevance_model", "openai/gpt-4.1-mini"))
    ai_relevance_max_calls = max(0, int(cfg.get("ai_relevance_max_calls", 0)))
    importance_model = str(cfg.get("importance_model", "openai/gpt-4.1-mini"))
    importance_max_calls = max(0, int(cfg.get("importance_max_calls", 0)))
    output_cleanup_enabled = str(cfg.get("output_cleanup_enabled", True)).lower() not in {"0", "false", "no"}
    output_cleanup_top_n = max(0, int(cfg.get("output_cleanup_top_n", publish_top_n)))
    output_cleanup_max_calls = max(0, int(cfg.get("output_cleanup_max_calls", 0)))
    output_cleanup_model = str(cfg.get("output_cleanup_model", "openai/gpt-4.1-mini"))
    output_cleanup_article_max_chars = int(cfg.get("output_cleanup_article_max_chars", 5000))
    output_cleanup_prompt_hash = _prompt_bundle_hash(OUTPUT_CLEANUP_PROMPT_PATHS)
    article_fetch_timeout_sec = int(cfg.get("article_fetch_timeout_sec", cfg.get("request_timeout_sec", 25)))
    article_max_chars = int(cfg.get("article_max_chars", 12000))
    article_fetch_workers = max(1, int(cfg.get("article_fetch_workers", 5)))
    article_fetch_max_urls = max(0, int(cfg.get("article_fetch_max_urls", 0)))
    article_cache_enabled = str(cfg.get("article_cache_enabled", True)).lower() not in {"0", "false", "no"}
    article_cache_path = str(cfg.get("article_cache_path", "derived/article_cache.json"))
    article_cache_ttl_hours = int(cfg.get("article_cache_ttl_hours", 48))
    retry_max_attempts = int(cfg.get("llm_retry_max_attempts", 4))
    retry_base_delay_sec = float(cfg.get("llm_retry_base_delay_sec", 1.5))
    retry_max_delay_sec = float(cfg.get("llm_retry_max_delay_sec", 20.0))
    retry_jitter_sec = float(cfg.get("llm_retry_jitter_sec", 0.8))
    rate_limit_window_sec = float(cfg.get("llm_429_window_sec", 60))
    rate_limit_threshold = int(cfg.get("llm_429_threshold", 5))
    rate_limit_cooldown_base_sec = float(cfg.get("llm_429_cooldown_base_sec", 45.0))
    rate_limit_cooldown_max_sec = float(cfg.get("llm_429_cooldown_max_sec", 300.0))
    fail_fast_auth = str(cfg.get("github_models_fail_fast_auth", True)).strip().lower() not in {"0", "false", "no", "off"}

    if llm_cache is None:
        llm_cache = {}

    rubric_markdown = _read_text_file(IMPORTANCE_RUBRIC_PATH)
    rubric_hash = _rubric_hash(rubric_markdown) if rubric_markdown else ""
    ai_relevance_rubric = _read_text_file(AI_RELEVANCE_RUBRIC_PATH)
    ai_relevance_rubric_hash = _rubric_hash(ai_relevance_rubric) if ai_relevance_rubric else ""
    client, _client_error, _provider_label = _resolve_llm_client(cfg)
    call_rows: list[dict[str, Any]] = []
    rate_limit_states: dict[str, dict[str, Any]] = seed_model_daily_states_from_call_log(llm_call_log_path)
    global_daily_max_calls = llm_global_daily_request_cap(cfg)
    global_daily_rate_limit_state = (
        seed_global_daily_state_from_call_log(llm_call_log_path) if global_daily_max_calls > 0 else None
    )
    models_auth_failed = False
    model_budget_exhausted = False
    ai_relevance_attempts = 0
    importance_attempts = 0
    output_cleanup_attempts = 0
    model_call_lock = Lock()
    state_lock = Lock()

    def _append_call_row(row: dict[str, Any]) -> None:
        with state_lock:
            call_rows.append(row)

    def _model_calls_stopped() -> bool:
        with state_lock:
            return models_auth_failed or model_budget_exhausted

    def _claim_relevance_attempt() -> bool:
        nonlocal ai_relevance_attempts
        with state_lock:
            if ai_relevance_max_calls and ai_relevance_attempts >= ai_relevance_max_calls:
                return False
            ai_relevance_attempts += 1
            return True

    def _claim_importance_attempt() -> bool:
        nonlocal importance_attempts
        with state_lock:
            if importance_max_calls and importance_attempts >= importance_max_calls:
                return False
            importance_attempts += 1
            return True

    def _claim_cleanup_attempt() -> bool:
        nonlocal output_cleanup_attempts
        with state_lock:
            if output_cleanup_max_calls and output_cleanup_attempts >= output_cleanup_max_calls:
                return False
            output_cleanup_attempts += 1
            return True

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
            request_lock=model_call_lock,
        )

    def _record_model_exception(kind: str, story_id: str, model: str, exc: Exception) -> str:
        nonlocal models_auth_failed, model_budget_exhausted
        with state_lock:
            if isinstance(exc, RateLimitBudgetExceeded):
                model_budget_exhausted = True
                status = "skipped"
                action = "budget"
            elif fail_fast_auth and _is_auth_or_permission_exception(exc):
                models_auth_failed = True
                status = "error"
                action = "auth"
            else:
                status = "error"
                action = "error"
            call_rows.append(
                {
                    "ts": to_iso(datetime.now(timezone.utc)),
                    "kind": kind,
                    "story_id": story_id,
                    "model": model,
                    "status": status,
                    "error": str(exc),
                    "status_code": _status_code_from_exception(exc),
                }
            )
        return action

    def _publish_llm_status() -> dict[str, Any]:
        ok_count = sum(1 for row in call_rows if row.get("status") == "ok")
        error_count = sum(1 for row in call_rows if row.get("status") == "error")
        skipped_count = sum(1 for row in call_rows if row.get("status") == "skipped")
        by_kind: dict[str, int] = {}
        by_model: dict[str, int] = {}
        for row in call_rows:
            kind = str(row.get("kind") or "unknown")
            model = str(row.get("model") or "unknown")
            by_kind[kind] = by_kind.get(kind, 0) + 1
            by_model[model] = by_model.get(model, 0) + 1
        if error_count:
            status = "degraded" if ok_count else "error"
        elif skipped_count and not ok_count:
            status = "skipped"
        else:
            status = "ok"
        return {
            "status": status,
            "calls": len(call_rows),
            "ok": ok_count,
            "errors": error_count,
            "skipped": skipped_count,
            "by_kind": by_kind,
            "by_model": by_model,
        }

    article_cache = _load_article_cache(article_cache_path) if article_cache_enabled else {}
    article_cache_updated = False
    article_markdown_by_url: dict[str, str] = {}

    stories_needing_article: list[dict[str, Any]] = []
    seen_article_story_ids: set[str] = set()
    for index, story in enumerate(top_stories):
        story_id = str(story.get("story_id") or "").strip()
        if not story_id:
            continue
        if story_id in seen_article_story_ids:
            continue
        needs_importance_article = (
            client is not None
            and _eligible_for_importance_backfill(str(story.get("published") or ""), importance_backfill_days)
            and bool(rubric_markdown and rubric_hash)
            and bool(ai_relevance_rubric and ai_relevance_rubric_hash)
        )
        needs_cleanup_article = index < output_cleanup_top_n
        if not (needs_importance_article or needs_cleanup_article):
            continue
        stories_needing_article.append(story)
        seen_article_story_ids.add(story_id)

    unique_urls: list[str] = []
    seen_urls: set[str] = set()
    for story in stories_needing_article:
        article_url = str(story.get("canonical_url") or story.get("url") or "").strip()
        if article_url and article_url not in seen_urls:
            unique_urls.append(article_url)
            seen_urls.add(article_url)

    urls_to_fetch: list[str] = []
    for url in unique_urls:
        cached_entry = article_cache.get(url)
        if cached_entry and (
            bool(cfg.get("backfill_mode"))
            or _article_cache_fresh(cached_entry, article_cache_ttl_hours)
        ):
            article_markdown_by_url[url] = str(cached_entry.get("markdown") or "")
        else:
            urls_to_fetch.append(url)

    deferred_article_urls: set[str] = set()
    if article_fetch_max_urls and len(urls_to_fetch) > article_fetch_max_urls:
        deferred_article_urls = set(urls_to_fetch[article_fetch_max_urls:])
        urls_to_fetch = urls_to_fetch[:article_fetch_max_urls]

    if urls_to_fetch:
        with ThreadPoolExecutor(max_workers=min(article_fetch_workers, len(urls_to_fetch))) as executor:
            futures = {
                executor.submit(_fetch_article_with_url, url, article_fetch_timeout_sec, article_max_chars): url
                for url in urls_to_fetch
            }
            for future in as_completed(futures):
                url = futures[future]
                try:
                    fetched_url, markdown = future.result()
                    article_markdown_by_url[fetched_url] = markdown
                    if article_cache_enabled and markdown:
                        article_cache[fetched_url] = {
                            "markdown": markdown,
                            "fetched_at": to_iso(datetime.now(timezone.utc)),
                        }
                        article_cache_updated = True
                except Exception:
                    article_markdown_by_url[url] = ""
                    if article_cache_enabled and bool(cfg.get("backfill_mode")):
                        article_cache[url] = {
                            "markdown": "",
                            "fetched_at": to_iso(datetime.now(timezone.utc)),
                            "fetch_failed": True,
                        }
                        article_cache_updated = True

    grading_candidates = [
        story
        for story in top_stories
        if rubric_markdown
        and rubric_hash
        and ai_relevance_rubric
        and ai_relevance_rubric_hash
        and _eligible_for_importance_backfill(str(story.get("published") or ""), importance_backfill_days)
    ]
    cleanup_candidates = top_stories[:output_cleanup_top_n] if output_cleanup_enabled else []

    def _current_relevance(story: dict[str, Any]) -> dict[str, Any] | None:
        story_id = str(story.get("story_id") or "")
        cache_entry = llm_cache.get(story_id, {})
        relevance = cache_entry.get("ai_relevance")
        if not isinstance(relevance, dict):
            return None
        article_url = str(story.get("canonical_url") or story.get("url") or "")
        context_hash = _ai_relevance_context_hash(
            str(story.get("title") or ""),
            _story_base_summary(story),
            article_markdown_by_url.get(article_url, ""),
            ai_relevance_rubric_hash,
            ai_relevance_model,
        )
        return relevance if str(relevance.get("context_hash") or "") == context_hash else None

    def _current_cleanup(story: dict[str, Any]) -> dict[str, Any] | None:
        story_id = str(story.get("story_id") or "")
        article_url = str(story.get("canonical_url") or story.get("url") or "")
        article_markdown = _article_excerpt(
            article_markdown_by_url.get(article_url, ""),
            output_cleanup_article_max_chars,
        )
        title_text = _strip_trailing_importance_tags(str(story.get("title") or ""))
        summary_text = _story_base_summary(story)
        context_hash = _output_cleanup_context_hash(
            title_text,
            summary_text,
            _source_context(story, article_markdown),
            output_cleanup_prompt_hash,
            output_cleanup_model,
        )
        return _cached_output_cleanup(llm_cache.get(story_id, {}), context_hash)

    def _backlog_counts() -> dict[str, int]:
        relevance_pending = 0
        importance_pending = 0
        for story in grading_candidates:
            relevance = _current_relevance(story)
            if relevance is None:
                relevance_pending += 1
                continue
            if not _ai_relevance_allows_grading(relevance):
                continue
            cache_entry = llm_cache.get(str(story.get("story_id") or ""), {})
            importance_raw = cache_entry.get("importance")
            importance = _normalize_importance_payload(
                cast(dict[str, Any], importance_raw) if isinstance(importance_raw, dict) else None
            )
            if not isinstance(importance, dict) or str(importance.get("rubric_hash") or "") != rubric_hash:
                importance_pending += 1

        return {
            "ai_relevance": relevance_pending,
            "importance": importance_pending,
            "output_cleanup": sum(1 for story in cleanup_candidates if _current_cleanup(story) is None),
        }

    backlog_before = _backlog_counts()

    def _grade_story(story: dict[str, Any]) -> None:
        story_id = str(story.get("story_id") or "").strip()
        if not story_id:
            return
        cache_entry = llm_cache.get(story_id, {})
        existing_importance_raw = cache_entry.get("importance")
        existing_importance = _normalize_importance_payload(
            cast(dict[str, Any], existing_importance_raw) if isinstance(existing_importance_raw, dict) else None
        )
        if existing_importance is not None and existing_importance != existing_importance_raw:
            cache_entry = llm_cache.setdefault(story_id, cache_entry)
            cache_entry["importance"] = existing_importance

        existing_relevance_raw = cache_entry.get("ai_relevance")
        existing_relevance = cast(dict[str, Any], existing_relevance_raw) if isinstance(existing_relevance_raw, dict) else None

        if not rubric_markdown or not rubric_hash:
            return

        if not ai_relevance_rubric or not ai_relevance_rubric_hash:
            return

        if not _eligible_for_importance_backfill(str(story.get("published") or ""), importance_backfill_days):
            return

        if client is None:
            if isinstance(existing_relevance, dict):
                story["ai_relevance"] = existing_relevance
            if isinstance(existing_importance, dict):
                story["importance"] = existing_importance
            return
        if _model_calls_stopped():
            if isinstance(existing_relevance, dict):
                story["ai_relevance"] = existing_relevance
            if isinstance(existing_importance, dict):
                story["importance"] = existing_importance
            return
        importance_client = client

        title_text = str(story.get("title") or "")
        context_text = _story_base_summary(story)
        article_url = str(story.get("canonical_url") or story.get("url") or "")
        if bool(cfg.get("backfill_mode")) and article_url in deferred_article_urls:
            return
        article_markdown = article_markdown_by_url.get(article_url, "")
        relevance_context_hash = _ai_relevance_context_hash(
            title_text,
            context_text,
            article_markdown,
            ai_relevance_rubric_hash,
            ai_relevance_model,
        )
        relevance_payload: dict[str, Any] | None = existing_relevance
        if not isinstance(relevance_payload, dict) or str(relevance_payload.get("context_hash") or "") != relevance_context_hash:
            if not _claim_relevance_attempt():
                return
            try:
                relevance_result, relevance_retry_meta = _model_call(
                    ai_relevance_model,
                    lambda: importance_client.check_ai_relevance(
                        title_text,
                        context_text,
                        ai_relevance_rubric,
                        model=ai_relevance_model,
                        article=article_markdown,
                    ),
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
                cache_entry = llm_cache.setdefault(story_id, cache_entry)
                cache_entry["ai_relevance"] = relevance_payload
                _append_call_row(
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
                _record_model_exception("ai_relevance", story_id, ai_relevance_model, exc)
                return

        story["ai_relevance"] = relevance_payload
        if not _ai_relevance_allows_grading(relevance_payload):
            story.pop("importance", None)
            return

        if isinstance(existing_importance, dict):
            story["importance"] = existing_importance

        should_grade = False
        if not isinstance(existing_importance, dict):
            should_grade = True
        else:
            if str(existing_importance.get("rubric_hash") or "") != rubric_hash:
                should_grade = True

        if not should_grade:
            return

        if not _claim_importance_attempt():
            return
        try:
            result, retry_meta = _model_call(
                importance_model,
                lambda: importance_client.grade_importance(
                    title_text,
                    context_text,
                    rubric_markdown,
                    model=importance_model,
                    article=article_markdown,
                ),
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
            cache_entry = llm_cache.setdefault(story_id, cache_entry)
            normalized_importance_payload = _normalize_importance_payload(importance_payload) or importance_payload
            cache_entry["importance"] = normalized_importance_payload
            story["importance"] = normalized_importance_payload

            _append_call_row(
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
            _record_model_exception("importance", story_id, importance_model, exc)

    if llm_workers > 1 and len(top_stories) > 1:
        with ThreadPoolExecutor(max_workers=min(llm_workers, len(top_stories))) as executor:
            list(executor.map(_grade_story, top_stories))
    else:
        for story in top_stories:
            _grade_story(story)

    def _cleanup_story(story: dict[str, Any]) -> None:
        story_id = str(story.get("story_id") or "").strip()
        if not story_id:
            return
        cache_entry = llm_cache.get(story_id, {})
        title_text = _strip_trailing_importance_tags(str(story.get("title") or ""))
        summary_text = _story_base_summary(story)
        article_url = str(story.get("canonical_url") or story.get("url") or "")
        if bool(cfg.get("backfill_mode")) and article_url in deferred_article_urls:
            return
        article_markdown = _article_excerpt(
            article_markdown_by_url.get(article_url, ""),
            output_cleanup_article_max_chars,
        )
        source_context = _source_context(story, article_markdown)
        cleanup_context_hash = _output_cleanup_context_hash(
            title_text,
            summary_text,
            source_context,
            output_cleanup_prompt_hash,
            output_cleanup_model,
        )

        cached_cleanup = _cached_output_cleanup(cache_entry, cleanup_context_hash)
        if cached_cleanup is not None:
            _apply_output_cleanup(story, cached_cleanup)
            return

        if not output_cleanup_enabled or client is None or _model_calls_stopped():
            return

        if not _claim_cleanup_attempt():
            return
        try:
            cleanup_result, cleanup_retry_meta = _model_call(
                output_cleanup_model,
                lambda: client.rewrite_output_cleanup(title_text, summary_text, source_context, model=output_cleanup_model),
            )
            rewritten_title = str(cleanup_result.get("title") or title_text).strip() or title_text
            rewritten_description = str(cleanup_result.get("description") or summary_text).strip() or summary_text
            _append_call_row(
                {
                    "ts": to_iso(datetime.now(timezone.utc)),
                    "kind": "output_cleanup",
                    "story_id": story_id,
                    "model": cleanup_result.get("model"),
                    "latency_ms": cleanup_result.get("latency_ms"),
                    "usage": cleanup_result.get("usage", {}),
                    "input_hash": cleanup_result.get("input_hash"),
                    "status": "ok",
                    "retries": cleanup_retry_meta.get("retries", 0),
                }
            )

            cleanup_payload: dict[str, Any] = {
                "title": rewritten_title,
                "description": rewritten_description,
                "context_hash": cleanup_context_hash,
                "prompt_hash": output_cleanup_prompt_hash,
                "model": output_cleanup_model,
                "input_hash": cleanup_result.get("input_hash"),
                "title_input_hash": cleanup_result.get("input_hash"),
                "description_input_hash": cleanup_result.get("input_hash"),
                "rewritten_at": to_iso(datetime.now(timezone.utc)),
            }
            cache_entry = llm_cache.setdefault(story_id, cache_entry)
            cache_entry["output_cleanup"] = cleanup_payload
            _apply_output_cleanup(story, cleanup_payload)
        except Exception as exc:
            _record_model_exception("output_cleanup", story_id, output_cleanup_model, exc)

    cleanup_work = top_stories[:output_cleanup_top_n]
    if llm_workers > 1 and len(cleanup_work) > 1:
        with ThreadPoolExecutor(max_workers=min(llm_workers, len(cleanup_work))) as executor:
            list(executor.map(_cleanup_story, cleanup_work))
    else:
        for story in cleanup_work:
            _cleanup_story(story)

    if llm_call_log_path and call_rows:
        append_jsonl(llm_call_log_path, call_rows)

    if llm_status is not None:
        publish_status = _publish_llm_status()
        backlog_after = _backlog_counts()
        publish_status["backlog"] = {
            stage: {
                "before": backlog_before[stage],
                "remaining": backlog_after[stage],
            }
            for stage in backlog_before
        }
        publish_status["backlog_remaining"] = sum(backlog_after.values())
        llm_status.update(publish_status)

    if article_cache_enabled and article_cache_updated:
        write_json(article_cache_path, article_cache)

    payload: dict[str, Any] = {
        "schema_version": cfg.get("schema_version", "1.0.0"),
        "generated": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "count": len(top_stories),
        "items": [
            {
                "title": _story_title_with_importance_tags(story),
                "originalTitle": story.get("title"),
                "url": story.get("canonical_url") or story.get("url"),
                "source": story.get("source_name"),
                "sourceType": story.get("source_type"),
                "sourceCategory": story.get("source_category"),
                "published": story.get("published"),
                "summary": _story_summary(story),
                "description": _story_summary(story),
                "originalSummary": _story_base_summary(story),
                "score": story.get("score"),
                "upvotes": _sum_mentions(story, "upvotes"),
                "comments": _sum_mentions(story, "comments"),
                "clusterId": story.get("cluster_id"),
                "primarySource": story.get("primary_source"),
                "sources": story.get("sources", []),
                "alternateLinks": story.get("alternate_links", []),
                "isDuplicate": story.get("is_duplicate", False),
                "duplicateCount": story.get("duplicate_count", 0),
                "duplicateSourceCount": story.get("duplicate_source_count", 1),
                "outputCleanup": story.get("output_cleanup"),
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
        description="Top Ranked AI stories across configured sources",
    )

    for story in top_stories:
        cast(Any, feed).add_item(**_to_feed_entry(story))

    cast(Any, feed).write_all_formats(base_feed_path)
    return payload, llm_cache
