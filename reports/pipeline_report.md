# Pipeline Report

- Timestamp: 2026-08-04T16:50:59.155614Z
- Sources configured: 43
- Raw items: 1974
- Stories: 1919
- Clusters: 1891
- LLM: {'status': 'degraded', 'calls': 142, 'ok': 138, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 52, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 131, 'ok': 127, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 52, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 131}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 142
- Enrichment: 11
- Publish: 131

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.06
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 28.08
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 810.45
- persist_llm_cache: 0.21