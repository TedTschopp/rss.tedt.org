# Pipeline Report

- Timestamp: 2026-09-08T03:49:04.810328Z
- Sources configured: 43
- Raw items: 1950
- Stories: 1900
- Clusters: 1869
- LLM: {'status': 'ok', 'calls': 150, 'ok': 150, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 23, 'output_cleanup': 42}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'ok', 'calls': 124, 'ok': 124, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 23, 'output_cleanup': 42}, 'by_model': {'openai/gpt-4.1-mini': 124}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 17}

## LLM Calls
- Total: 150
- Enrichment: 26
- Publish: 124

## Enrichment Backlog
- Remaining: 17
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.39
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 33.37
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 414.68
- persist_llm_cache: 0.21