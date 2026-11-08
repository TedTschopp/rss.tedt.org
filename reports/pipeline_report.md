# Pipeline Report

- Timestamp: 2026-11-08T14:59:18.997975Z
- Sources configured: 43
- Raw items: 2197
- Stories: 2151
- Clusters: 2122
- LLM: {'status': 'degraded', 'calls': 130, 'ok': 129, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 42, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 119, 'ok': 118, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 42, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 119}, 'backlog': {'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 130
- Enrichment: 11
- Publish: 119

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 6.72
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 13.13
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 421.51
- persist_llm_cache: 0.26