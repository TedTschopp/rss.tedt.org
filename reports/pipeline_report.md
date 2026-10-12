# Pipeline Report

- Timestamp: 2026-10-12T00:19:58.780376Z
- Sources configured: 43
- Raw items: 2032
- Stories: 1979
- Clusters: 1951
- LLM: {'status': 'degraded', 'calls': 109, 'ok': 107, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 29, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 98, 'ok': 96, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 29, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 98}, 'backlog': {'ai_relevance': {'before': 49, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 49, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 109
- Enrichment: 11
- Publish: 98

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.14
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 13.04
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 265.14
- persist_llm_cache: 0.22