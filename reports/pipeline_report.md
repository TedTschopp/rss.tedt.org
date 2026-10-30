# Pipeline Report

- Timestamp: 2026-10-30T16:11:41.216405Z
- Sources configured: 43
- Raw items: 2218
- Stories: 2165
- Clusters: 2138
- LLM: {'status': 'degraded', 'calls': 121, 'ok': 120, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 39, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 110, 'ok': 109, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 39, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 110}, 'backlog': {'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 121
- Enrichment: 11
- Publish: 110

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.17
- normalize: 0.09
- dedupe: 0.07
- llm_enrich: 14.09
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 397.38
- persist_llm_cache: 0.23