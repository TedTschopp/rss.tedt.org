#!/usr/bin/env python3
import argparse
import os
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
    with open(report_path_md, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description="Run Natural20-style aggregation pipeline")
    parser.add_argument("--sources", default="sources.yml", help="Path to sources.yml")
    args = parser.parse_args()

    ensure_dirs([RAW_DIR, DATA_DIR, DERIVED_DIR, API_DIR, FEEDS_DIR, REPORTS_DIR])

    pipeline_config = {
        "schema_version": SCHEMA_VERSION,
        **load_pipeline_settings(args.sources),
    }
    if "PIPELINE_LLM_TOP_N" in os.environ:
        pipeline_config["llm_top_n"] = int(os.environ["PIPELINE_LLM_TOP_N"])
    if "PIPELINE_PUBLISH_TOP_N" in os.environ:
        pipeline_config["publish_top_n"] = int(os.environ["PIPELINE_PUBLISH_TOP_N"])
    if "PIPELINE_LLM_RATE_LIMIT_REQUESTS_PER_WINDOW" in os.environ:
        pipeline_config["llm_rate_limit_requests_per_window"] = int(os.environ["PIPELINE_LLM_RATE_LIMIT_REQUESTS_PER_WINDOW"])
    if "PIPELINE_LLM_RATE_LIMIT_WINDOW_SEC" in os.environ:
        pipeline_config["llm_rate_limit_window_sec"] = float(os.environ["PIPELINE_LLM_RATE_LIMIT_WINDOW_SEC"])
    if "PIPELINE_LLM_RATE_LIMIT_MIN_INTERVAL_SEC" in os.environ:
        pipeline_config["llm_rate_limit_min_interval_sec"] = float(os.environ["PIPELINE_LLM_RATE_LIMIT_MIN_INTERVAL_SEC"])

    sources = load_sources(args.sources)
    state = read_json(SOURCE_STATE_FILE, {})

    raw_items, fetch_rows, new_state = run_ingestion(sources, state, RAW_DIR, pipeline_config)
    append_jsonl(FETCH_LOG_FILE, fetch_rows)
    write_json(SOURCE_STATE_FILE, new_state)

    items = normalize_items(raw_items)
    stories = dedupe_to_stories(items)

    llm_cache = read_json(LLM_CACHE_FILE, {})
    stories, llm_cache, llm_meta = enrich_stories(stories, llm_cache, LLM_CALL_LOG_FILE, pipeline_config)
    write_json(LLM_CACHE_FILE, llm_cache)

    clusters, cluster_map = build_clusters(stories, llm_cache)
    ranked = score_stories(stories, cluster_map, pipeline_config)

    write_json(f"{DATA_DIR}/sources.json", {"schema_version": SCHEMA_VERSION, "items": sources})
    write_json(f"{DERIVED_DIR}/items.json", {"schema_version": SCHEMA_VERSION, "items": items})
    write_json(f"{DATA_DIR}/stories.json", {"schema_version": SCHEMA_VERSION, "items": ranked})
    write_json(f"{DATA_DIR}/clusters.json", {"schema_version": SCHEMA_VERSION, "items": clusters})

    api_payload, llm_cache = publish_outputs(
        ranked,
        f"{API_DIR}/feed.json",
        f"{FEEDS_DIR}/top",
        llm_cache=llm_cache,
        llm_call_log_path=LLM_CALL_LOG_FILE,
        config=pipeline_config,
    )

    write_json(LLM_CACHE_FILE, llm_cache)

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
    }

    _write_report(f"{REPORTS_DIR}/pipeline_report.json", f"{REPORTS_DIR}/pipeline_report.md", report)
    print("Pipeline completed", report)


if __name__ == "__main__":
    main()
