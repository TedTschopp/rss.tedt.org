# GitHub Actions Pipeline Architecture

## Bottom Line

The GitHub Actions pipeline is both the production data pipeline and the deployment pipeline for `rss.tedt.org`. It performs three distinct jobs:

1. Generate or refresh feed and API artifacts.
2. Commit generated artifacts back to the repository.
3. Build and deploy the static Jekyll site to GitHub Pages.

That means workflow changes are not just CI changes. They can affect public feed URLs, committed state, site health reporting, and deployment behavior.

## System Context

```text
External sources
  -> scripts.enhanced_scraper
  -> root public feed files
  -> reports/aggregation and derived state

sources.yml
  -> pipeline.run_all
  -> data, derived, api/feed.json, feeds/top.*
  -> reports/pipeline_report.*

root feed files + api/feed.json + api/rss_status.json + site pages
  -> Jekyll build
  -> GitHub Pages deployment
```

## Components

| Component | Location | Responsibility |
| --- | --- | --- |
| Workflow definition | `.github/workflows/scrape-and-generate-rss.yml` | Coordinates scraping, pipeline execution, artifact commits, and Pages deployment. |
| Scraper entrypoint | `scripts/enhanced_scraper.py` | Generates primary and aggregated public feed files. |
| Scraper config | `scripts/config.py` | Defines public feed names, internal artifact paths, scraper behavior, and aggregation defaults. |
| Ranking pipeline | `pipeline/run_all.py` | Ingests sources, deduplicates stories, enriches/scales ranking, and publishes Top Stories artifacts. |
| Feed generator | `scripts/feed_generator.py` | Generates RSS 1.0, Atom, and JSON feed variants. |
| Monitor | `scripts/monitor.py` | Validates feed health and writes `api/rss_status.json`. |
| Static site | Jekyll root files and `_layouts/` | Builds the website deployed to GitHub Pages. |

## Artifact Boundaries

| Category | Location | Public URL Contract | Notes |
| --- | --- | --- | --- |
| Public feed outputs | Repo root and `feeds/` | Yes | Do not move without redirects and subscriber impact review. |
| Public site status | `api/rss_status.json` | Site-used API | Site pages fetch `/api/rss_status.json`. |
| Public API feed | `api/feed.json` | Site/API output | Produced by `pipeline.run_all`. |
| Site data | `data/*.json` | Public if deployed | Used to support the generated site/API experience. |
| Internal state | `derived/` | No | Used by pipeline and workflow continuity. |
| Reports | `reports/` | No | Operational diagnostics and summaries. |
| Source snapshots | `raw/` | No | Historical source snapshots by run date. |

## Trust And Permission Boundaries

The workflow uses separate permission profiles:

| Job | Permissions | Why |
| --- | --- | --- |
| `scrape-and-generate-rss` | `contents: write`, `pages: write`, `id-token: write` | Needs to commit generated artifacts and enable downstream Pages deployment. |
| `deploy-on-push` | `contents: read`, `pages: write`, `id-token: write` | Builds and deploys only. It does not mutate repository contents. |
| `deploy-after-scrape` | `contents: read`, `pages: write`, `id-token: write` | Deploys latest main after scheduled/manual scraping. |

## Critical Invariants

- Root feed outputs are public URL contracts.
- Scripts are executed as modules under `scripts/`, not as root-level files.
- The monitor writes `api/rss_status.json`; site pages read `/api/rss_status.json`.
- Scheduled/manual runs may commit generated artifacts to `main`.
- Human pushes deploy the site but do not run scraping.
- Bot pushes created by the scrape job are not used as the deployment trigger; `deploy-after-scrape` handles deployment after scheduled/manual runs.

## Extension Risk Surface

| Change Type | Risk | Control |
| --- | --- | --- |
| New public feed | Breaks subscriber URLs if moved later. | Define stable root or `feeds/` path first. |
| New generated artifact | May not be committed by workflow. | Add it to the staging allowlist. |
| New dependency | May break scheduled runs. | Update `requirements.txt` or Gemfile and validate install path. |
| New secret | May fail silently in scheduled runs. | Document degraded behavior and add monitor/report signal. |
| New deploy job | Can race existing Pages deployments. | Use the existing `pages` concurrency model or define a specific one. |
| Moving files | Can break Linux Actions due case sensitivity. | Validate exact case and module import paths. |

## Recommended Future Enhancements

- Add `actionlint` validation to local tooling and possibly CI.
- Add a lightweight workflow validation script that checks command paths and artifact staging globs.
- Split artifact generation from deployment only if deployment cadence becomes materially different from data refresh cadence.
- Add explicit tests for `scripts.monitor` and pipeline artifact path contracts.
