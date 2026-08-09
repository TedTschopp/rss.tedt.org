# Pipeline Report

- Timestamp: 2026-08-09T00:19:23.789832Z
- Sources configured: 43
- Raw items: 1925
- Stories: 1877
- Clusters: 1849
- LLM: {'status': 'degraded', 'calls': 96, 'ok': 95, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 41, 'importance': 24, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 85, 'ok': 84, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 41, 'importance': 24, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 85}, 'backlog': {'ai_relevance': {'before': 41, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 41, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 96
- Enrichment: 11
- Publish: 85

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.04
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 19.25
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 440.58
- persist_llm_cache: 0.21