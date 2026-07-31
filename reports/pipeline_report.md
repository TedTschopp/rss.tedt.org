# Pipeline Report

- Timestamp: 2026-07-31T00:45:03.793919Z
- Sources configured: 43
- Raw items: 1902
- Stories: 1864
- Clusters: 1829
- LLM: {'status': 'degraded', 'calls': 149, 'ok': 145, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 53, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 138, 'ok': 134, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 53, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 138}, 'backlog': {'ai_relevance': {'before': 65, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 65, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 149
- Enrichment: 11
- Publish: 138

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 4.25
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 18.98
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 1115.50
- persist_llm_cache: 0.19