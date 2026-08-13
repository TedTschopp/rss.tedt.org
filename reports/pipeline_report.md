# Pipeline Report

- Timestamp: 2026-08-13T08:37:31.395626Z
- Sources configured: 43
- Raw items: 1888
- Stories: 1848
- Clusters: 1819
- LLM: {'status': 'degraded', 'calls': 94, 'ok': 92, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 37, 'importance': 26, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 83, 'ok': 81, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 37, 'importance': 26, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 83}, 'backlog': {'ai_relevance': {'before': 37, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 37, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 94
- Enrichment: 11
- Publish: 83

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.12
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 17.19
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 408.59
- persist_llm_cache: 0.21