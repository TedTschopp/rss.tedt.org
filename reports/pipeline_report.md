# Pipeline Report

- Timestamp: 2026-11-13T16:07:34.578839Z
- Sources configured: 43
- Raw items: 2268
- Stories: 2220
- Clusters: 2190
- LLM: {'status': 'ok', 'calls': 133, 'ok': 133, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 45, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}}}, 'publish': {'status': 'ok', 'calls': 122, 'ok': 122, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 45, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 122}, 'backlog': {'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}, 'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 133
- Enrichment: 11
- Publish: 122

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 11
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.26
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 16.47
- cluster: 0.22
- score: 0.03
- write_intermediate_outputs: 0.26
- publish: 473.11
- persist_llm_cache: 0.24