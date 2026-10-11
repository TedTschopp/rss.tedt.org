# Pipeline Report

- Timestamp: 2026-10-11T03:55:56.204433Z
- Sources configured: 43
- Raw items: 2042
- Stories: 1998
- Clusters: 1966
- LLM: {'status': 'ok', 'calls': 182, 'ok': 182, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 34, 'output_cleanup': 49}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'ok', 'calls': 156, 'ok': 156, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 34, 'output_cleanup': 49}, 'by_model': {'openai/gpt-4.1-mini': 156}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 17}

## LLM Calls
- Total: 182
- Enrichment: 26
- Publish: 156

## Enrichment Backlog
- Remaining: 17
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.88
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 30.46
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 284.67
- persist_llm_cache: 0.22