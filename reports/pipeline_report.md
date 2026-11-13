# Pipeline Report

- Timestamp: 2026-11-13T22:02:30.025559Z
- Sources configured: 43
- Raw items: 2198
- Stories: 2144
- Clusters: 2115
- LLM: {'status': 'ok', 'calls': 135, 'ok': 135, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 43, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 124, 'ok': 124, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 43, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 124}, 'backlog': {'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 135
- Enrichment: 11
- Publish: 124

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.77
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 15.31
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 363.89
- persist_llm_cache: 0.28