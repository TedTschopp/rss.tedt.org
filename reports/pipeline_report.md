# Pipeline Report

- Timestamp: 2026-08-26T00:19:34.849669Z
- Sources configured: 43
- Raw items: 1977
- Stories: 1925
- Clusters: 1897
- LLM: {'status': 'degraded', 'calls': 126, 'ok': 124, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 36, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 115, 'ok': 113, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 36, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 115}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 126
- Enrichment: 11
- Publish: 115

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.27
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 22.19
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 626.65
- persist_llm_cache: 0.20