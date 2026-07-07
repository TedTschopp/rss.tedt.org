# GitHub Action: Table / Feed Aggregator to RSS

This project scrapes a dynamic table (GAI Insights) and also aggregates multiple external RSS feeds into unified local RSS outputs (with retention + archives) automatically via GitHub Actions.

## Features (Current)

- Scheduled every 8 hours + manual dispatch
- Table scraping (Playwright) for `newsTable` (GAI Insights)
- Primary AI feed: `ai_rss_feed.xml`
- Automatic 60-day retention + `ai_rss_feed_archive.xml`
- Multi-source aggregation for enabled feeds in `_config.yml`
- Aggregated archives for feeds once retention produces older items
- Change detection with JSON snapshot
- Robust error handling & retries
- Health monitoring (`scripts/monitor.py`) writing `api/rss_status.json`

## Setup

1. **Enable GitHub Actions**: Make sure GitHub Actions are enabled for your repository
2. **Set Permissions**: The workflow has `contents: write` permission to commit the RSS feed back to the repo
3. **Files of Interest**:
   - `scripts/enhanced_scraper.py` (primary orchestrator: scraping + aggregation + retention)
   - `scripts/monitor.py` (feed health & summary)
   - `scripts/config.py` (constants & defaults)
   - `_config.yml` (Jekyll + aggregation settings)
   - `ai_rss_feed.xml` / `ai_rss_feed_archive.xml`
   - `aggregated_*.xml` / `aggregated_*_archive.xml`
   - `derived/previous_data.json` (change tracking)
   - `reports/aggregation/` (repo-only aggregation health and report artifacts)

### GitHub Models Token Setup (for LLM enrichment)

The pipeline supports optional LLM enrichment through GitHub Models.

1. Create a fine-grained PAT in GitHub with:
   - Resource owner: your account/org
   - Repository access: this repository (or broader, if intended)
   - Permission: `Models` → `Read`
2. Add a repository secret in GitHub:
   - Preferred: `GH_MODELS_TOKEN`
   - Also supported: `GH_Models_Token`
3. For local runs, export one of these before running the pipeline:
   - `export GH_MODELS_TOKEN=...`
4. Run:
   - `source .venv/bin/activate && python -m pipeline.run_all`

When the token is missing, the pipeline still runs in degraded mode (no summaries/embeddings) and publishes feeds/API JSON.

## Top Stories Controls

`Top Stories (LLM Aggregated)` now reads both its source list and ranking settings from `sources.yml`.

- `ranking.half_life_hours` controls how quickly older stories decay.
- `ranking.weights.*` controls the contribution of authority, freshness, engagement, coverage, and other score factors.
- `sources[*].authority_weight` controls how much each source influences ranking.

For a browser-based editor, open `/top-stories-manager/` locally or on the site. The page can:

- load the repo copy of `sources.yml`
- open a local `sources.yml` file
- add, duplicate, disable, or delete Top Stories sources
- edit ranking weights
- save back to the opened file when browser file APIs are available, or download the updated YAML otherwise

## How It Works

1. **Scraping**: The script fetches the webpage and extracts all data from the table with ID "newsTable"
2. **Data Processing**: Extracts text content and any links from each table cell
3. **Change Detection**: Compares current data with previously saved data
4. **RSS Generation**: Creates RSS entries from table rows, using first 3 columns for titles
5. **Repository Update**: Commits the updated RSS feed if changes are detected

## Customization

Primary customization via `_config.yml` (aggregation) and `scripts/config.py` (scraping/filters).

Example aggregation block:

```yaml
aggregated_feeds:
   enabled: true
   output: "/aggregated_external.xml"
   max_items: 150
   retention_days: 60
   source_attribution: title  # or description / none
   sources:
      - "https://feeds.arstechnica.com/arstechnica/technology-lab"
      - "https://www.infoworld.com/index.rss"
```

## Schedule

The action runs:

- **Automatically**: Light aggregation every 8 hours, plus one daily heavy enrichment run
- **Manually**: Via the "Actions" tab in your GitHub repository

## Generated RSS Feeds

Primary AI Feed: `/ai_rss_feed.xml` (+ archive `/ai_rss_feed_archive.xml`)

Enabled aggregated feeds: `/aggregated_wes_ai_news.xml`, `/aggregated_ea.xml`, and `/aggregated_broad_ai_news.xml` (+ archives where retention has produced them)

## Troubleshooting

- Check the Actions tab for any errors
- The script includes detailed logging for debugging
- If the table structure changes, you may need to update the scraping logic
- Make sure the repository has write permissions for the action

## Dependencies

- `requests`: For HTTP requests
- `beautifulsoup4`: For HTML parsing
- `PyYAML`: Parse Jekyll `_config.yml` aggregation settings
- `feedgen`: For RSS feed generation

## Documentation

- Documentation home: [Docs/README.md](Docs/README.md).
- GitHub Actions pipeline overview: [Docs/operations/github-actions-pipeline.md](Docs/operations/github-actions-pipeline.md).
- Pipeline extension guide: [Docs/operations/github-actions-extension-guide.md](Docs/operations/github-actions-extension-guide.md).
- Operations runbook: [Docs/operations/github-actions-runbook.md](Docs/operations/github-actions-runbook.md).
