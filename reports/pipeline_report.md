# Pipeline Report

- Timestamp: 2026-10-27T16:15:17.580820Z
- Sources configured: 43
- Raw items: 2184
- Stories: 2142
- Clusters: 2116
- LLM: {'status': 'degraded', 'calls': 158, 'ok': 156, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 54, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 147, 'ok': 145, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 54, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 147}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 158
- Enrichment: 11
- Publish: 147

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 4.51
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 16.74
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 544.80
- persist_llm_cache: 0.25