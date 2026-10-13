# Pipeline Report

- Timestamp: 2026-10-13T00:19:42.527758Z
- Sources configured: 43
- Raw items: 2127
- Stories: 2076
- Clusters: 2047
- LLM: {'status': 'ok', 'calls': 140, 'ok': 140, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 47, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 129, 'ok': 129, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 47, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 129}, 'backlog': {'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 140
- Enrichment: 11
- Publish: 129

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.21
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 13.01
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 307.90
- persist_llm_cache: 0.22