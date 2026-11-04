# Pipeline Report

- Timestamp: 2026-11-04T22:01:15.788100Z
- Sources configured: 43
- Raw items: 2201
- Stories: 2141
- Clusters: 2113
- LLM: {'status': 'degraded', 'calls': 149, 'ok': 144, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 54, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 138, 'ok': 133, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 54, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 138}, 'backlog': {'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 5}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 5}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 5}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 15}

## LLM Calls
- Total: 149
- Enrichment: 11
- Publish: 138

## Enrichment Backlog
- Remaining: 15
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 5
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.46
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 12.94
- cluster: 0.15
- score: 0.01
- write_intermediate_outputs: 0.20
- publish: 615.83
- persist_llm_cache: 0.20