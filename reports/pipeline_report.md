# Pipeline Report

- Timestamp: 2026-09-30T16:23:53.442064Z
- Sources configured: 43
- Raw items: 2104
- Stories: 2051
- Clusters: 2022
- LLM: {'status': 'degraded', 'calls': 153, 'ok': 150, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 54, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 142, 'ok': 139, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 54, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 142}, 'backlog': {'ai_relevance': {'before': 68, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 68, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 153
- Enrichment: 11
- Publish: 142

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 19.80
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 79.74
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 931.40
- persist_llm_cache: 0.20