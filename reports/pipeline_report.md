# Pipeline Report

- Timestamp: 2026-07-15T08:04:00.809292Z
- Sources configured: 43
- Raw items: 1596
- Stories: 1558
- Clusters: 1495
- LLM: {'status': 'degraded', 'calls': 302, 'ok': 300, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 81, 'importance': 74, 'output_cleanup': 100}, 'stages': {'enrichment': {'status': 'ok', 'calls': 47, 'ok': 47, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 0}}}, 'publish': {'status': 'degraded', 'calls': 255, 'ok': 253, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 81, 'importance': 74, 'output_cleanup': 100}, 'by_model': {'openai/gpt-4.1-mini': 255}, 'backlog': {'ai_relevance': {'before': 118, 'remaining': 37}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 137, 'remaining': 37}}, 'backlog_remaining': 76}}, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 0}, 'ai_relevance': {'before': 118, 'remaining': 37}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 137, 'remaining': 37}}, 'backlog_remaining': 76}

## LLM Calls
- Total: 302
- Enrichment: 47
- Publish: 255

## Enrichment Backlog
- Remaining: 76
- embeddings: 0
- summaries: 0
- ai_relevance: 37
- importance: 2
- output_cleanup: 37

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.01
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 47.90
- cluster: 0.28
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 326.50
- persist_llm_cache: 0.21