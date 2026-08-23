# Pipeline Report

- Timestamp: 2026-08-23T08:12:43.468385Z
- Sources configured: 43
- Raw items: 1961
- Stories: 1918
- Clusters: 1888
- LLM: {'status': 'ok', 'calls': 114, 'ok': 114, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 35, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 103, 'ok': 103, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 35, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 103}, 'backlog': {'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 114
- Enrichment: 11
- Publish: 103

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.82
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 17.67
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 295.42
- persist_llm_cache: 0.21