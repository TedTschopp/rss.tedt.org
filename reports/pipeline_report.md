# Pipeline Report

- Timestamp: 2026-08-05T00:34:54.208229Z
- Sources configured: 43
- Raw items: 1950
- Stories: 1893
- Clusters: 1865
- LLM: {'status': 'degraded', 'calls': 136, 'ok': 135, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 46, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 125, 'ok': 124, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 46, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 125}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 136
- Enrichment: 11
- Publish: 125

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.89
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 23.77
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 535.31
- persist_llm_cache: 0.21