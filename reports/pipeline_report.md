# Pipeline Report

- Timestamp: 2026-07-27T16:52:45.711475Z
- Sources configured: 43
- Raw items: 1933
- Stories: 1884
- Clusters: 1856
- LLM: {'status': 'degraded', 'calls': 133, 'ok': 132, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 45, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 122, 'ok': 121, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 45, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 122}, 'backlog': {'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 133
- Enrichment: 11
- Publish: 122

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.95
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 16.30
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 573.16
- persist_llm_cache: 0.18