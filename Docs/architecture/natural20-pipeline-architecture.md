# Natural20-style Pipeline Architecture

## Scope

This repo now includes a batch pipeline that runs in GitHub Actions, persists JSON artifacts, and publishes static API/feed outputs for GitHub Pages.

## Flow

1. Load source registry from `sources.yml` (fallback `_config.yml` aggregated feeds).
2. Fetch source payloads with conditional requests where possible.
3. Normalize records into a common item model.
4. Dedupe items into canonical stories.
5. Optionally enrich with GitHub Models (`GH_MODELS_TOKEN`).
6. Cluster related stories.
7. Score and rank stories with explainable signal breakdown.
8. Publish static artifacts (`api/feed.json`, `feeds/top.*`, `data/*.json`, reports).

## Storage Layout

- `raw/YYYY-MM-DD/*.json`: source snapshots per run day.
- `derived/fetch_log.jsonl`: source fetch telemetry.
- `derived/source_state.json`: ETag/failure state.
- `derived/llm_cache.json`: enrichment cache by story id.
- `data/stories.json`: ranked canonical stories.
- `data/clusters.json`: cluster topology and representative story.
- `api/feed.json`: Natural20-like API payload.
- `feeds/top.xml|.atom|.json|_rss1.xml`: multi-format top feed.
- `reports/pipeline_report.json|.md`: pipeline health summary.

## Degraded Mode

If `GH_MODELS_TOKEN` is missing or model calls fail, the pipeline still publishes ranked outputs from non-LLM signals.
