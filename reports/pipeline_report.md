# Pipeline Report

- Timestamp: 2026-11-05T11:37:26.378237Z
- Sources configured: 43
- Raw items: 2116
- Stories: 2071
- Clusters: 2043
- LLM: {'status': 'degraded', 'calls': 170, 'ok': 168, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 53, 'importance': 43, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}}}, 'publish': {'status': 'degraded', 'calls': 144, 'ok': 142, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 53, 'importance': 43, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 144}, 'backlog': {'ai_relevance': {'before': 53, 'remaining': 1}, 'importance': {'before': 3, 'remaining': 1}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}, 'ai_relevance': {'before': 53, 'remaining': 1}, 'importance': {'before': 3, 'remaining': 1}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 26}

## LLM Calls
- Total: 170
- Enrichment: 26
- Publish: 144

## Enrichment Backlog
- Remaining: 26
- embeddings: 0
- summaries: 24
- ai_relevance: 1
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.16
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 30.98
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 776.25
- persist_llm_cache: 0.24