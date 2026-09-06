# Pipeline Report

- Timestamp: 2026-09-06T16:13:20.185836Z
- Sources configured: 43
- Raw items: 2017
- Stories: 1967
- Clusters: 1939
- LLM: {'status': 'degraded', 'calls': 136, 'ok': 135, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 125, 'ok': 124, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 125}, 'backlog': {'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 136
- Enrichment: 11
- Publish: 125

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.79
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 16.22
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 405.72
- persist_llm_cache: 0.14