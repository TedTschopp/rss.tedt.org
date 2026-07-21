# Pipeline Report

- Timestamp: 2026-07-21T17:20:42.645203Z
- Sources configured: 43
- Raw items: 1958
- Stories: 1904
- Clusters: 1875
- LLM: {'status': 'degraded', 'calls': 136, 'ok': 134, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 125, 'ok': 123, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 125}, 'backlog': {'ai_relevance': {'before': 57, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 57, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 136
- Enrichment: 11
- Publish: 125

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.64
- normalize: 0.09
- dedupe: 0.05
- llm_enrich: 17.46
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 731.78
- persist_llm_cache: 0.21