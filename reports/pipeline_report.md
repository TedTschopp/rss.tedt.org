# Pipeline Report

- Timestamp: 2026-08-23T16:12:14.459034Z
- Sources configured: 43
- Raw items: 1988
- Stories: 1944
- Clusters: 1915
- LLM: {'status': 'degraded', 'calls': 108, 'ok': 106, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 32, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 97, 'ok': 95, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 32, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 97}, 'backlog': {'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 108
- Enrichment: 11
- Publish: 97

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.34
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 18.91
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 404.89
- persist_llm_cache: 0.19