# Pipeline Report

- Timestamp: 2026-08-29T16:17:31.237526Z
- Sources configured: 43
- Raw items: 1964
- Stories: 1912
- Clusters: 1884
- LLM: {'status': 'degraded', 'calls': 144, 'ok': 139, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 49, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 133, 'ok': 128, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 49, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 133}, 'backlog': {'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 5}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 15}

## LLM Calls
- Total: 144
- Enrichment: 11
- Publish: 133

## Enrichment Backlog
- Remaining: 15
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 5
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.56
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 18.58
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 691.40
- persist_llm_cache: 0.19