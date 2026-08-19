# Pipeline Report

- Timestamp: 2026-08-19T16:20:37.190226Z
- Sources configured: 43
- Raw items: 2019
- Stories: 1966
- Clusters: 1937
- LLM: {'status': 'degraded', 'calls': 131, 'ok': 129, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 41, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 120, 'ok': 118, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 41, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 120}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 131
- Enrichment: 11
- Publish: 120

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 4.53
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 19.96
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 761.87
- persist_llm_cache: 0.21