# Generated Artifact Ownership

## Purpose

This document explains which generated artifacts are public, which are internal, and which workflow step owns them.

## Ownership Table

| Artifact | Owner | Public? | Committed By Workflow? | Notes |
| --- | --- | --- | --- | --- |
| `ai_rss_feed.xml` | `scripts.enhanced_scraper` | Yes | Yes | Primary subscriber-facing RSS feed. |
| `ai_rss_feed.atom` | `scripts.enhanced_scraper` | Yes | Yes | Alternate feed format. |
| `ai_rss_feed.json` | `scripts.enhanced_scraper` | Yes | Yes | JSON feed format. |
| `ai_rss_feed_rss1.xml` | `scripts.enhanced_scraper` | Yes | Yes | RSS 1.0 format. |
| `aggregated_*.xml` | `scripts.enhanced_scraper` | Yes | Yes | Public aggregated feeds from `_config.yml`. |
| `aggregated_*.atom` | `scripts.enhanced_scraper` | Yes | Yes | Alternate feed format. |
| `aggregated_*.json` | `scripts.enhanced_scraper` | Yes | Yes | JSON feed format. |
| `aggregated_*_rss1.xml` | `scripts.enhanced_scraper` | Yes | Yes | RSS 1.0 format. |
| `*_archive.xml` | `scripts.enhanced_scraper` | Yes | Yes | Generated once retention produces archived items. |
| `reports/aggregation/*_health.json` | `scripts.enhanced_scraper` | No | Yes | Source-level health and skip details. |
| `reports/aggregation/*_report.md` | `scripts.enhanced_scraper` | No | Yes | Human-readable aggregation reports. |
| `derived/aggregator_cache.json` | `scripts.enhanced_scraper` | No | Yes | Fetch and importance cache. |
| `derived/previous_data.json` | `scripts.enhanced_scraper` | No | Yes | Change detection state. |
| `derived/skipped_sources.json` | `scripts.enhanced_scraper` | No | Yes | Skipped aggregation source summary. |
| `api/feed.json` | `pipeline.run_all` | Yes | Yes | Top Stories API payload. |
| `feeds/top.*` | `pipeline.run_all` | Yes | Yes | Top Stories feed formats. |
| `data/*.json` | `pipeline.run_all` | Site-facing data | Yes | Sources, stories, and clusters. |
| `derived/items.json` | `pipeline.run_all` | No | Yes | Normalized intermediate items. |
| `derived/source_state.json` | `pipeline.run_all` | No | Yes | Fetch continuity state. |
| `derived/fetch_log.jsonl` | `pipeline.run_all` | No | Yes | Fetch telemetry. |
| `derived/llm_cache.json` | `pipeline.run_all` | No | Yes | LLM enrichment cache with compact float32 embeddings, retained for active ranked stories up to 75 MiB. |
| `derived/llm_call_log.jsonl` | `pipeline.run_all` | No | Yes | LLM call telemetry. |
| `reports/pipeline_report.json` | `pipeline.run_all` | No | Yes | Machine-readable pipeline report. |
| `reports/pipeline_report.md` | `pipeline.run_all` | No | Yes | Human-readable pipeline report. |
| `api/rss_status.json` | `scripts.monitor` | Site-facing API | Yes | Feed and pipeline health payload. |

## Workflow Staging Rule

Generated artifacts persist only if `.github/workflows/scrape-and-generate-rss.yml` stages them in the `Check for RSS changes` step.

When adding a new generated artifact:

1. Assign an owner.
2. Decide whether it is public, site-facing, or internal.
3. Put it in the correct directory.
4. Add it to the workflow staging allowlist if it should persist.
5. Add path-contract validation if another component depends on it.

## Directory Guidance

| Directory | Use For | Avoid |
| --- | --- | --- |
| Repo root | Public feeds and public site root files. | Caches, reports, logs, private state. |
| `api/` | Browser-readable API payloads. | Large logs or private state. |
| `feeds/` | Public feed outputs under stable paths. | Internal feed generation state. |
| `data/` | Site-facing structured data. | Fetch logs or transient cache. |
| `derived/` | Machine state, caches, logs, intermediate artifacts. | Subscriber-facing URLs. |
| `reports/` | Human and machine operational summaries. | Public URL contracts. |
| `raw/` | Source snapshots. | Curated public artifacts. |
