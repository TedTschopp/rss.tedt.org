# Pipeline Report

- Timestamp: 2026-09-26T00:19:52.342084Z
- Sources configured: 43
- Raw items: 2030
- Stories: 1981
- Clusters: 1953
- LLM: {'status': 'degraded', 'calls': 145, 'ok': 142, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 52, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 134, 'ok': 131, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 52, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 134}, 'backlog': {'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 145
- Enrichment: 11
- Publish: 134

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.89
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 12.75
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 445.12
- persist_llm_cache: 0.21