# Pipeline Report

- Timestamp: 2026-10-24T03:59:24.811786Z
- Sources configured: 43
- Raw items: 2091
- Stories: 2044
- Clusters: 2015
- LLM: {'status': 'degraded', 'calls': 209, 'ok': 207, 'errors': 2, 'skipped': 0, 'by_kind': {'importance': 45, 'ai_relevance': 94, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}}}, 'publish': {'status': 'degraded', 'calls': 183, 'ok': 181, 'errors': 2, 'skipped': 0, 'by_kind': {'importance': 45, 'ai_relevance': 94, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 183}, 'backlog': {'ai_relevance': {'before': 94, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}, 'ai_relevance': {'before': 94, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 209
- Enrichment: 26
- Publish: 183

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 19
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.06
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 29.18
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 889.69
- persist_llm_cache: 0.22