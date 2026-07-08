# Public URL Contracts

## Bottom Line

This repository is both source code and public web namespace. Some files are not just files; they are stable URLs consumed by feed readers, browser pages, crawlers, and GitHub Pages.

Do not move, rename, or repurpose public URLs without an explicit compatibility plan.

## Contract Categories

| Category | Paths | Consumer | Stability Rule |
| --- | --- | --- | --- |
| Primary AI feed | `/ai_rss_feed.xml`, `/ai_rss_feed.atom`, `/ai_rss_feed.json`, `/ai_rss_feed_rss1.xml` | Feed subscribers and site links | Keep stable. |
| Aggregated feeds | `/aggregated_*.xml`, `/aggregated_*.atom`, `/aggregated_*.json`, `/aggregated_*_rss1.xml` | Feed subscribers and site links | Keep stable once published. |
| Feed archives | `/*_archive.xml` | Feed subscribers and historical consumers | Keep stable where present. |
| Top Stories feeds | `/feeds/top.xml`, `/feeds/top.atom`, `/feeds/top.json`, `/feeds/top_rss1.xml` | Site/API consumers and subscribers | Keep stable. |
| Site status API | `/api/rss_status.json` | `feeds.html`, `about.md`, operators | Keep producer and consumers aligned. |
| Top Stories API | `/api/feed.json` | Browser/API consumers | Version before making breaking shape changes. |
| Site pages | `/`, `/feeds/`, `/status/`, `/about/`, `/404.html`, `/top-stories-manager.html` | Browser users | Preserve or redirect. |
| Feed stylesheet | `/feed-style.xsl` | XML feed rendering | Keep stable while feeds reference it. |
| SEO/discovery | `/robots.txt`, `/sitemap.xml`, `CNAME` | Crawlers, GitHub Pages, DNS | Keep stable. |

## Internal Paths That Are Not Public Contracts

| Path | Purpose |
| --- | --- |
| `scripts/` | Python entrypoints and helpers. |
| `pipeline/` | Top Stories ranking pipeline implementation. |
| `derived/` | Internal state, caches, logs, and run continuity. |
| `reports/` | Human-readable and machine-readable operational reports. |
| `raw/` | Historical source snapshots. |
| `Docs/` | Repository documentation, excluded from Jekyll processing. |
| `New-Home/` | Isolated redesign/template workspace. |

## Change Rules

### Safe Changes

- Add a new generated file under `derived/` or `reports/` and stage it in the workflow.
- Add a new internal script under `scripts/` and call it with `python -m scripts.<module>`.
- Add new documentation under `Docs/`.

### Review Required

- Add a new public feed URL.
- Change the shape of `api/feed.json` or `api/rss_status.json`.
- Change generated artifact staging globs in the workflow.
- Move public site pages or feed assets.

### High Risk

- Rename or remove a root feed file.
- Change `feed-style.xsl` without checking generated XML stylesheet references.
- Move `api/rss_status.json` without updating all browser fetches and validators.
- Change workflow trigger behavior on `main` without understanding bot push handling.

## Compatibility Pattern

When a public URL must change:

1. Create the replacement path.
2. Keep the old path working for a transition period if GitHub Pages can support it.
3. Update site links and documentation.
4. Update validators and path-contract tests.
5. Announce or document the change where subscribers/operators can find it.

## Validation

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m scripts.validate_workflow
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
```
