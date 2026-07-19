# Pipeline Report

- Timestamp: 2026-07-19T09:50:51.116970Z
- Sources configured: 43
- Raw items: 1777
- Stories: 1734
- Clusters: 1704
- LLM: {'status': 'ok', 'calls': 85, 'ok': 85, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 21, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 74, 'ok': 74, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 21, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 74}, 'backlog': {'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 85
- Enrichment: 11
- Publish: 74

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.92
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 19.60
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 261.67
- persist_llm_cache: 0.20