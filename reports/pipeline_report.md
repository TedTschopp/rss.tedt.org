# Pipeline Report

- Timestamp: 2026-09-01T00:23:59.773768Z
- Sources configured: 43
- Raw items: 1986
- Stories: 1929
- Clusters: 1901
- LLM: {'status': 'degraded', 'calls': 122, 'ok': 119, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 41, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 111, 'ok': 108, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 41, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 111}, 'backlog': {'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 122
- Enrichment: 11
- Publish: 111

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.04
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 21.85
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 543.11
- persist_llm_cache: 0.22