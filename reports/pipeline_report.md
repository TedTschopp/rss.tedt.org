# Pipeline Report

- Timestamp: 2026-08-25T00:16:34.155632Z
- Sources configured: 43
- Raw items: 1964
- Stories: 1916
- Clusters: 1888
- LLM: {'status': 'degraded', 'calls': 122, 'ok': 120, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 52, 'importance': 39, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}}}, 'publish': {'status': 'degraded', 'calls': 111, 'ok': 109, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 52, 'importance': 39, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 111}, 'backlog': {'ai_relevance': {'before': 52, 'remaining': 1}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}, 'ai_relevance': {'before': 52, 'remaining': 1}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 122
- Enrichment: 11
- Publish: 111

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 11
- ai_relevance: 1
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.00
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 17.41
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 449.93
- persist_llm_cache: 0.20