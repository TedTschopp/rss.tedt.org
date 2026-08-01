# Pipeline Report

- Timestamp: 2026-08-01T16:29:20.934620Z
- Sources configured: 43
- Raw items: 1956
- Stories: 1925
- Clusters: 1897
- LLM: {'status': 'ok', 'calls': 113, 'ok': 113, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 37, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}}}, 'publish': {'status': 'ok', 'calls': 102, 'ok': 102, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 37, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 102}, 'backlog': {'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}, 'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 113
- Enrichment: 11
- Publish: 102

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 11
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.16
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 19.21
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 496.36
- persist_llm_cache: 0.21