# Pipeline Report

- Timestamp: 2026-08-03T00:32:26.103227Z
- Sources configured: 43
- Raw items: 1946
- Stories: 1894
- Clusters: 1864
- LLM: {'status': 'degraded', 'calls': 111, 'ok': 110, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 35, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 100, 'ok': 99, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 35, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 100}, 'backlog': {'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 111
- Enrichment: 11
- Publish: 100

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.60
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 17.18
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 356.86
- persist_llm_cache: 0.19