# Data Contracts (v1)

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
