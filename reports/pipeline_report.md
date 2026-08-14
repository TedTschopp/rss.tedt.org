# Pipeline Report

- Timestamp: 2026-08-14T08:36:05.897954Z
- Sources configured: 43
- Raw items: 1926
- Stories: 1881
- Clusters: 1853
- LLM: {'status': 'degraded', 'calls': 95, 'ok': 92, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 37, 'importance': 27, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 84, 'ok': 81, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 37, 'importance': 27, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 84}, 'backlog': {'ai_relevance': {'before': 37, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 37, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 95
- Enrichment: 11
- Publish: 84

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.69
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 18.11
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 426.82
- persist_llm_cache: 0.21