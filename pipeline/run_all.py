#!/usr/bin/env python3
import argparse
import os
import time
from datetime import datetime, timezone

from . import SCHEMA_VERSION
from .cluster import build_clusters
from .constants import (
    API_DIR,
    DATA_DIR,
    DERIVED_DIR,
    FETCH_LOG_FILE,
    FEEDS_DIR,
    LLM_CACHE_FILE,
    LLM_CALL_LOG_FILE,
    RAW_DIR,
    REPORTS_DIR,
    SOURCE_STATE_FILE,
)
from .dedupe import dedupe_to_stories
from .ingest import run_ingestion
from .io_utils import append_jsonl, ensure_dirs, read_json, write_json
from .llm_enrich import enrich_stories
from .normalize import normalize_items
from .publish import publish_outputs
from .score import score_stories
from .source_registry import load_pipeline_settings, load_sources


def _write_report(report_path_json: str, report_path_md: str, report: dict) -> None:
    write_json(report_path_json, report)

    lines = [
        "# Pipeline Report",
        "",
        f"- Timestamp: {report['timestamp']}",
        f"- Sources configured: {report['sources_configured']}",
        f"- Raw items: {report['raw_items']}",
        f"- Stories: {report['stories']}",
        f"- Clusters: {report['clusters']}",
        f"- LLM: {report['llm_status']}",
    ]
    stage_timings = report.get("stage_timings_sec")
    if isinstance(stage_timings, dict) and stage_timings:
        lines.extend(["", "## Stage Timings (seconds)"])
        for stage_name, seconds in stage_timings.items():
            try:
                value = float(seconds)
            except (TypeError, ValueError):
                continue
            lines.append(f"- {stage_name}: {value:.2f}")
    with open(report_path_md, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def _apply_env_overrides(pipeline_config: dict, environ: dict[str, str] | None = None) -> dict:
    env = environ or os.environ

    # Existing controls
    if "PIPELINE_LLM_TOP_N" in env:
        pipeline_config["llm_top_n"] = int(env["PIPELINE_LLM_TOP_N"])
    if "PIPELINE_PUBLISH_TOP_N" in env:
        pipeline_config["publish_top_n"] = int(env["PIPELINE_PUBLISH_TOP_N"])
    if "PIPELINE_LLM_RATE_LIMIT_REQUESTS_PER_WINDOW" in env:
        pipeline_config["llm_rate_limit_requests_per_window"] = int(env["PIPELINE_LLM_RATE_LIMIT_REQUESTS_PER_WINDOW"])
    if "PIPELINE_LLM_RATE_LIMIT_WINDOW_SEC" in env:
        pipeline_config["llm_rate_limit_window_sec"] = float(env["PIPELINE_LLM_RATE_LIMIT_WINDOW_SEC"])
    if "PIPELINE_LLM_RATE_LIMIT_MIN_INTERVAL_SEC" in env:
        pipeline_config["llm_rate_limit_min_interval_sec"] = float(env["PIPELINE_LLM_RATE_LIMIT_MIN_INTERVAL_SEC"])
    if "PIPELINE_LLM_PROVIDER" in env:
        pipeline_config["llm_provider"] = str(env["PIPELINE_LLM_PROVIDER"])
    if "PIPELINE_GITHUB_MODELS_COPILOT_PLAN" in env:
        pipeline_config["github_models_copilot_plan"] = str(env["PIPELINE_GITHUB_MODELS_COPILOT_PLAN"])
    if "PIPELINE_GITHUB_MODELS_DAILY_BUDGET_ENABLED" in env:
        pipeline_config["github_models_daily_budget_enabled"] = str(env["PIPELINE_GITHUB_MODELS_DAILY_BUDGET_ENABLED"]).strip().lower() in {
            "1",
            "true",
            "yes",
            "on",
        }
    if "PIPELINE_GITHUB_MODELS_DAILY_REQUEST_CAP" in env:
        pipeline_config["github_models_daily_request_cap"] = int(env["PIPELINE_GITHUB_MODELS_DAILY_REQUEST_CAP"])
    if "PIPELINE_GITHUB_MODELS_GLOBAL_DAILY_REQUEST_CAP" in env:
        pipeline_config["github_models_global_daily_request_cap"] = int(env["PIPELINE_GITHUB_MODELS_GLOBAL_DAILY_REQUEST_CAP"])
    if "PIPELINE_GITHUB_MODELS_FAIL_FAST_AUTH" in env:
        pipeline_config["github_models_fail_fast_auth"] = str(env["PIPELINE_GITHUB_MODELS_FAIL_FAST_AUTH"]).strip().lower() in {
            "1",
            "true",
            "yes",
            "on",
        }
    if "PIPELINE_OPENAI_BASE_URL" in env:
        pipeline_config["openai_base_url"] = str(env["PIPELINE_OPENAI_BASE_URL"])
    if "PIPELINE_OPENAI_RATE_LIMIT_REQUESTS_PER_MINUTE" in env:
        pipeline_config["openai_rate_limit_requests_per_minute"] = int(env["PIPELINE_OPENAI_RATE_LIMIT_REQUESTS_PER_MINUTE"])
    if "PIPELINE_OPENAI_DAILY_REQUEST_CAP" in env:
        pipeline_config["openai_daily_request_cap"] = int(env["PIPELINE_OPENAI_DAILY_REQUEST_CAP"])
    if "PIPELINE_OPENAI_GLOBAL_DAILY_REQUEST_CAP" in env:
        pipeline_config["openai_global_daily_request_cap"] = int(env["PIPELINE_OPENAI_GLOBAL_DAILY_REQUEST_CAP"])
    if "PIPELINE_LLM_RETRY_MAX_ATTEMPTS" in env:
        pipeline_config["llm_retry_max_attempts"] = int(env["PIPELINE_LLM_RETRY_MAX_ATTEMPTS"])
    if "PIPELINE_LLM_RETRY_BASE_DELAY_SEC" in env:
        pipeline_config["llm_retry_base_delay_sec"] = float(env["PIPELINE_LLM_RETRY_BASE_DELAY_SEC"])
    if "PIPELINE_LLM_RETRY_MAX_DELAY_SEC" in env:
        pipeline_config["llm_retry_max_delay_sec"] = float(env["PIPELINE_LLM_RETRY_MAX_DELAY_SEC"])
    if "PIPELINE_LLM_RETRY_JITTER_SEC" in env:
        pipeline_config["llm_retry_jitter_sec"] = float(env["PIPELINE_LLM_RETRY_JITTER_SEC"])
    if "PIPELINE_LLM_429_WINDOW_SEC" in env:
        pipeline_config["llm_429_window_sec"] = float(env["PIPELINE_LLM_429_WINDOW_SEC"])
    if "PIPELINE_LLM_429_THRESHOLD" in env:
        pipeline_config["llm_429_threshold"] = int(env["PIPELINE_LLM_429_THRESHOLD"])
    if "PIPELINE_LLM_429_COOLDOWN_BASE_SEC" in env:
        pipeline_config["llm_429_cooldown_base_sec"] = float(env["PIPELINE_LLM_429_COOLDOWN_BASE_SEC"])
    if "PIPELINE_LLM_429_COOLDOWN_MAX_SEC" in env:
        pipeline_config["llm_429_cooldown_max_sec"] = float(env["PIPELINE_LLM_429_COOLDOWN_MAX_SEC"])

    # Additional controls for runtime/cost tuning
    if "PIPELINE_LLM_CHAT_MAX_CALLS" in env:
        pipeline_config["llm_chat_max_calls"] = int(env["PIPELINE_LLM_CHAT_MAX_CALLS"])
    if "PIPELINE_SUMMARY_MODEL" in env:
        pipeline_config["summary_model"] = str(env["PIPELINE_SUMMARY_MODEL"])
    if "PIPELINE_AI_RELEVANCE_MODEL" in env:
        pipeline_config["ai_relevance_model"] = str(env["PIPELINE_AI_RELEVANCE_MODEL"])
    if "PIPELINE_IMPORTANCE_MODEL" in env:
        pipeline_config["importance_model"] = str(env["PIPELINE_IMPORTANCE_MODEL"])
    if "PIPELINE_OUTPUT_CLEANUP_MODEL" in env:
        pipeline_config["output_cleanup_model"] = str(env["PIPELINE_OUTPUT_CLEANUP_MODEL"])
    if "PIPELINE_OUTPUT_CLEANUP_TOP_N" in env:
        pipeline_config["output_cleanup_top_n"] = int(env["PIPELINE_OUTPUT_CLEANUP_TOP_N"])
    if "PIPELINE_IMPORTANCE_BACKFILL_DAYS" in env:
        pipeline_config["importance_backfill_days"] = int(env["PIPELINE_IMPORTANCE_BACKFILL_DAYS"])
    if "PIPELINE_OUTPUT_CLEANUP_ENABLED" in env:
        pipeline_config["output_cleanup_enabled"] = str(env["PIPELINE_OUTPUT_CLEANUP_ENABLED"]).strip().lower() in {
            "1",
            "true",
            "yes",
            "on",
        }
    if "PIPELINE_ARTICLE_FETCH_WORKERS" in env:
        pipeline_config["article_fetch_workers"] = int(env["PIPELINE_ARTICLE_FETCH_WORKERS"])
    if "PIPELINE_ARTICLE_CACHE_ENABLED" in env:
        pipeline_config["article_cache_enabled"] = str(env["PIPELINE_ARTICLE_CACHE_ENABLED"]).strip().lower() in {
            "1",
            "true",
            "yes",
            "on",
        }
    if "PIPELINE_ARTICLE_CACHE_TTL_HOURS" in env:
        pipeline_config["article_cache_ttl_hours"] = int(env["PIPELINE_ARTICLE_CACHE_TTL_HOURS"])
    if "PIPELINE_ARTICLE_CACHE_PATH" in env:
        pipeline_config["article_cache_path"] = str(env["PIPELINE_ARTICLE_CACHE_PATH"])

    return pipeline_config


def main():
    parser = argparse.ArgumentParser(description="Run Natural20-style aggregation pipeline")
    parser.add_argument("--sources", default="sources.yml", help="Path to sources.yml")
    args = parser.parse_args()

    ensure_dirs([RAW_DIR, DATA_DIR, DERIVED_DIR, API_DIR, FEEDS_DIR, REPORTS_DIR])

    pipeline_config = {
        "schema_version": SCHEMA_VERSION,
        **load_pipeline_settings(args.sources),
    }
    pipeline_config = _apply_env_overrides(pipeline_config)

    stage_timings_sec: dict[str, float] = {}

    started = time.perf_counter()
    sources = load_sources(args.sources)
    state = read_json(SOURCE_STATE_FILE, {})
    stage_timings_sec["load_sources_and_state"] = round(time.perf_counter() - started, 4)

    started = time.perf_counter()
    raw_items, fetch_rows, new_state = run_ingestion(sources, state, RAW_DIR, pipeline_config)
    append_jsonl(FETCH_LOG_FILE, fetch_rows)
    write_json(SOURCE_STATE_FILE, new_state)
    stage_timings_sec["ingestion"] = round(time.perf_counter() - started, 4)

    started = time.perf_counter()
    items = normalize_items(raw_items)
    stage_timings_sec["normalize"] = round(time.perf_counter() - started, 4)

    started = time.perf_counter()
    stories = dedupe_to_stories(items)
    stage_timings_sec["dedupe"] = round(time.perf_counter() - started, 4)

    started = time.perf_counter()
    llm_cache = read_json(LLM_CACHE_FILE, {})
    stories, llm_cache, llm_meta = enrich_stories(stories, llm_cache, LLM_CALL_LOG_FILE, pipeline_config)
    write_json(LLM_CACHE_FILE, llm_cache)
    stage_timings_sec["llm_enrich"] = round(time.perf_counter() - started, 4)

    started = time.perf_counter()
    clusters, cluster_map = build_clusters(stories, llm_cache)
    stage_timings_sec["cluster"] = round(time.perf_counter() - started, 4)

    started = time.perf_counter()
    ranked = score_stories(stories, cluster_map, pipeline_config)
    stage_timings_sec["score"] = round(time.perf_counter() - started, 4)

    started = time.perf_counter()
    write_json(f"{DATA_DIR}/sources.json", {"schema_version": SCHEMA_VERSION, "items": sources})
    write_json(f"{DERIVED_DIR}/items.json", {"schema_version": SCHEMA_VERSION, "items": items})
    write_json(f"{DATA_DIR}/stories.json", {"schema_version": SCHEMA_VERSION, "items": ranked})
    write_json(f"{DATA_DIR}/clusters.json", {"schema_version": SCHEMA_VERSION, "items": clusters})
    stage_timings_sec["write_intermediate_outputs"] = round(time.perf_counter() - started, 4)

    started = time.perf_counter()
    api_payload, llm_cache = publish_outputs(
        ranked,
        f"{API_DIR}/feed.json",
        f"{FEEDS_DIR}/top",
        llm_cache=llm_cache,
        llm_call_log_path=LLM_CALL_LOG_FILE,
        config=pipeline_config,
    )
    stage_timings_sec["publish"] = round(time.perf_counter() - started, 4)

    started = time.perf_counter()
    write_json(LLM_CACHE_FILE, llm_cache)
    stage_timings_sec["persist_llm_cache"] = round(time.perf_counter() - started, 4)

    report = {
        "schema_version": SCHEMA_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "sources_configured": len(sources),
        "fetch_attempts": len(fetch_rows),
        "raw_items": len(raw_items),
        "items": len(items),
        "stories": len(ranked),
        "clusters": len(clusters),
        "api_items": api_payload.get("count", 0),
        "llm_status": llm_meta,
        "stage_timings_sec": stage_timings_sec,
    }

    _write_report(f"{REPORTS_DIR}/pipeline_report.json", f"{REPORTS_DIR}/pipeline_report.md", report)
    print("Pipeline completed", report)


if __name__ == "__main__":
    main()
