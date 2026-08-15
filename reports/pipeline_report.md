# Pipeline Report

- Timestamp: 2026-08-15T08:17:18.778492Z
- Sources configured: 43
- Raw items: 2490
- Stories: 2152
- Clusters: 2123
- LLM: {'status': 'degraded', 'calls': 181, 'ok': 179, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 74, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 170, 'ok': 168, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 74, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 170}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 181
- Enrichment: 11
- Publish: 170

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.70
- normalize: 0.11
- dedupe: 0.07
- llm_enrich: 17.21
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.32
- publish: 660.06
- persist_llm_cache: 0.21