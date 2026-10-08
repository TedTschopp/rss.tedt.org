# Pipeline Report

- Timestamp: 2026-10-08T16:15:42.310915Z
- Sources configured: 43
- Raw items: 2147
- Stories: 2094
- Clusters: 2065
- LLM: {'status': 'degraded', 'calls': 153, 'ok': 151, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 57, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 142, 'ok': 140, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 57, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 142}, 'backlog': {'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 153
- Enrichment: 11
- Publish: 142

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.81
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 17.58
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 492.88
- persist_llm_cache: 0.23