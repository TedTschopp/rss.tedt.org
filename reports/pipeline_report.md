# Pipeline Report

- Timestamp: 2026-09-26T03:56:56.789531Z
- Sources configured: 43
- Raw items: 2005
- Stories: 1954
- Clusters: 1926
- LLM: {'status': 'ok', 'calls': 313, 'ok': 313, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 140, 'importance': 113, 'output_cleanup': 34}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 35, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}}}, 'publish': {'status': 'ok', 'calls': 287, 'ok': 287, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 140, 'importance': 113, 'output_cleanup': 34}, 'by_model': {'openai/gpt-4.1-mini': 287}, 'backlog': {'ai_relevance': {'before': 140, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 0}, 'output_cleanup': {'before': 34, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 35, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}, 'ai_relevance': {'before': 140, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 0}, 'output_cleanup': {'before': 34, 'remaining': 0}}, 'backlog_remaining': 16}

## LLM Calls
- Total: 313
- Enrichment: 26
- Publish: 287

## Enrichment Backlog
- Remaining: 16
- embeddings: 0
- summaries: 16
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.89
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 29.05
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 810.28
- persist_llm_cache: 0.22