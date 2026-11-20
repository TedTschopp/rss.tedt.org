# Pipeline Report

- Timestamp: 2026-11-20T12:29:14.332219Z
- Sources configured: 43
- Raw items: 1987
- Stories: 1959
- Clusters: 1931
- LLM: {'status': 'degraded', 'calls': 326, 'ok': 324, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 141, 'importance': 109, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}}}, 'publish': {'status': 'degraded', 'calls': 300, 'ok': 298, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 141, 'importance': 109, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 300}, 'backlog': {'ai_relevance': {'before': 141, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}, 'ai_relevance': {'before': 141, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 26}

## LLM Calls
- Total: 326
- Enrichment: 26
- Publish: 300

## Enrichment Backlog
- Remaining: 26
- embeddings: 0
- summaries: 24
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 6.55
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 33.62
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 1593.97
- persist_llm_cache: 0.29