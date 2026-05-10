# New-Home Promotion Plan

## Purpose

`New-Home/` is the active redesign and template workspace. It should stay isolated until the site is ready to move beyond the current RSS hub experience in a deliberate way.

## Promotion Principles

- Preserve public feed URLs.
- Preserve current Jekyll deployment behavior until replacement templates are validated.
- Treat browser-facing API dependencies as contracts.
- Promote templates intentionally, not by copying prototype files into root paths without a rollback plan.

## Promotion Stages

| Stage | Goal | Exit Criteria |
| --- | --- | --- |
| 1. Prototype | Explore layout, visual system, and page templates in isolation. | Templates render locally and design direction is stable. |
| 2. Data Mapping | Map prototype components to existing feeds/API/data files. | Every dynamic section has a known source path and fallback behavior. |
| 3. Jekyll Integration | Convert stable templates into Jekyll layouts/includes/pages. | Jekyll build passes and existing public URLs still work. |
| 4. Parallel Preview | Publish or preview new templates without replacing production root pages. | Stakeholders can review without subscriber impact. |
| 5. Production Promotion | Replace production templates/pages. | Rollback path exists; validation passes; public URL impact reviewed. |
| 6. Cleanup | Remove obsolete prototype files or archive them. | `New-Home/` contains only active future work or documented references. |

## Required Checks Before Promotion

- `bundle exec jekyll build` passes.
- `python -m scripts.validate_workflow` passes.
- `python -m scripts.validate_setup` passes.
- `python -m unittest discover -s tests` passes.
- `feeds.html` and `about.md` still fetch `/api/rss_status.json` or an intentionally updated endpoint.
- Root feed files remain in place.
- Mobile and desktop template behavior is manually reviewed.

## Data Dependencies To Map

| Experience Area | Likely Source |
| --- | --- |
| Feed health/status | `api/rss_status.json` |
| Top Stories | `api/feed.json`, `feeds/top.*`, `data/stories.json` |
| Feed catalog | `_config.yml` `feeds` collection |
| Story clusters | `data/clusters.json` |
| Source metadata | `data/sources.json`, `sources.yml` |

## Rollback Pattern

1. Keep the previous root page/layout available in Git history.
2. Limit the promotion commit to template/page changes where possible.
3. Avoid changing feed generation and site redesign in the same commit.
4. If production behavior fails, revert the template promotion while leaving feed artifacts untouched.

## Open Design Questions

- Which current root pages are replaced first: `index.html`, `feeds.html`, `about.md`, or a new page path?
- Should `New-Home` become a Jekyll collection, a set of layouts/includes, or remain a prototype folder until final cutover?
- Which sections require live data versus static editorial curation?
