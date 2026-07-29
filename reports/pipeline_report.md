# Pipeline Report

- Timestamp: 2026-07-29T09:03:25.961602Z
- Sources configured: 43
- Raw items: 1813
- Stories: 1773
- Clusters: 1746
- LLM: {'status': 'ok', 'calls': 104, 'ok': 104, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 39, 'importance': 34, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 93, 'ok': 93, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 39, 'importance': 34, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 93}, 'backlog': {'ai_relevance': {'before': 39, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 39, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 104
- Enrichment: 11
- Publish: 93

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.25
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 22.82
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 345.19
- persist_llm_cache: 0.21