# Pipeline Report

- Timestamp: 2026-08-13T00:27:07.864134Z
- Sources configured: 43
- Raw items: 2005
- Stories: 1955
- Clusters: 1923
- LLM: {'status': 'degraded', 'calls': 136, 'ok': 133, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 45, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 125, 'ok': 122, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 45, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 125}, 'backlog': {'ai_relevance': {'before': 60, 'remaining': 1}, 'importance': {'before': 4, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 60, 'remaining': 1}, 'importance': {'before': 4, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 136
- Enrichment: 11
- Publish: 125

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.51
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 16.72
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.17
- publish: 560.70
- persist_llm_cache: 0.13