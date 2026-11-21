# Pipeline Report

- Timestamp: 2026-11-21T11:53:42.450079Z
- Sources configured: 43
- Raw items: 2069
- Stories: 2042
- Clusters: 2012
- LLM: {'status': 'degraded', 'calls': 272, 'ok': 270, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 122, 'importance': 74, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 23}}}, 'publish': {'status': 'degraded', 'calls': 246, 'ok': 244, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 122, 'importance': 74, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 246}, 'backlog': {'ai_relevance': {'before': 122, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 23}, 'ai_relevance': {'before': 122, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 272
- Enrichment: 26
- Publish: 246

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 23
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.82
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 29.98
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 973.54
- persist_llm_cache: 0.27