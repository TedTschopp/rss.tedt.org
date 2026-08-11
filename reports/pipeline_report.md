# Pipeline Report

- Timestamp: 2026-08-11T00:30:43.656272Z
- Sources configured: 43
- Raw items: 1962
- Stories: 1913
- Clusters: 1884
- LLM: {'status': 'degraded', 'calls': 147, 'ok': 142, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 63, 'importance': 53, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 136, 'ok': 131, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 63, 'importance': 53, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 136}, 'backlog': {'ai_relevance': {'before': 63, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 5}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 63, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 15}

## LLM Calls
- Total: 147
- Enrichment: 11
- Publish: 136

## Enrichment Backlog
- Remaining: 15
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 5
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.72
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 16.96
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 1027.78
- persist_llm_cache: 0.22