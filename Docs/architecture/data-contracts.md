# Data Contracts (v1)

## Contract Policy

Data contracts define the JSON and feed shapes consumed by the browser, subscribers, generated pages, or future integrations.

### Compatibility Rules

- Adding optional fields is non-breaking.
- Removing fields is breaking.
- Renaming fields is breaking unless the old field remains during a transition period.
- Changing field meaning is breaking even if the field name stays the same.
- Changing sort order or ranking semantics may be breaking for user experience even if the JSON shape is stable.

### Versioning Rules

- Keep `schema_version` in generated JSON payloads where available.
- If a browser page depends on a payload shape, update the page and this document together.
- If an external consumer may depend on a payload, prefer adding a versioned endpoint or transitional field.

### Ownership

| Contract | Producer | Primary Consumers |
| --- | --- | --- |
| `api/feed.json` | `pipeline.run_all` | Site/API consumers. |
| `api/rss_status.json` | `scripts.monitor` | `feeds.html`, `about.md`, operators. |
| `data/stories.json` | `pipeline.run_all` | Site data and future templates. |
| `data/clusters.json` | `pipeline.run_all` | Site data and future templates. |
| `data/sources.json` | `pipeline.run_all` | Site data and diagnostics. |
| `feeds/top.*` | `pipeline.run_all` | Feed subscribers and site links. |

## Story (`data/stories.json`)

- `story_id`: stable id.
- `canonical_url`: normalized link identity.
- `title`, `summary`, `published`.
- `source_name`, `source_type`, `authority_weight`.
- `mentions[]`: per-source records and engagement values.
- `cluster_id`.
- `score`, `rank`, `score_breakdown`.
- optional `llm`: summary/topics/entities and embedding metadata.

## Cluster (`data/clusters.json`)

- `cluster_id`.
- `label`.
- `story_ids[]`.
- `source_count`.
- `representative_story_id`.
- `updated_at`.

## Source (`data/sources.json`)

- `id`, `type`, `name`, `url`, `category`.
- `authority_weight`.
- `enabled`.

## Fetch telemetry (`derived/fetch_log.jsonl`)

- `fetch_id`, `source_id`, `source_type`.
- `fetched_at`, `http_status`, `latency_ms`.
- `item_count`.
- `error`, `error_class`.

## API (`api/feed.json`)

- `generated`, `count`.
- `items[]` with `title`, `url`, `source`, `sourceType`, `published`, `summary`, `score`, `upvotes`, `comments`, `clusterId`.
