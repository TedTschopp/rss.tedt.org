# Pipeline Report

- Timestamp: 2026-09-17T00:18:52.901414Z
- Sources configured: 43
- Raw items: 2051
- Stories: 1989
- Clusters: 1959
- LLM: {'status': 'degraded', 'calls': 151, 'ok': 150, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 55, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 140, 'ok': 139, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 55, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 140}, 'backlog': {'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 151
- Enrichment: 11
- Publish: 140

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.97
- normalize: 0.08
- dedupe: 0.07
- llm_enrich: 13.78
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 391.33
- persist_llm_cache: 0.21