# Pipeline Report

- Timestamp: 2026-08-27T11:28:03.755042Z
- Sources configured: 43
- Raw items: 1958
- Stories: 1899
- Clusters: 1871
- LLM: {'status': 'degraded', 'calls': 103, 'ok': 102, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 30, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 92, 'ok': 91, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 30, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 92}, 'backlog': {'ai_relevance': {'before': 42, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 42, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 103
- Enrichment: 11
- Publish: 92

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.23
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 18.53
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 371.85
- persist_llm_cache: 0.21