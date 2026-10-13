# Pipeline Report

- Timestamp: 2026-10-13T08:19:53.735922Z
- Sources configured: 43
- Raw items: 2325
- Stories: 2281
- Clusters: 2252
- LLM: {'status': 'degraded', 'calls': 178, 'ok': 177, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 73, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 167, 'ok': 166, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 73, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 167}, 'backlog': {'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 178
- Enrichment: 11
- Publish: 167

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.71
- normalize: 0.10
- dedupe: 0.07
- llm_enrich: 13.84
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.29
- publish: 416.94
- persist_llm_cache: 0.26