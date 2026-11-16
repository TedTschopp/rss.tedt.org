# Pipeline Report

- Timestamp: 2026-11-16T12:12:55.836026Z
- Sources configured: 43
- Raw items: 1927
- Stories: 1861
- Clusters: 1833
- LLM: {'status': 'degraded', 'calls': 187, 'ok': 185, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 55, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}}}, 'publish': {'status': 'degraded', 'calls': 161, 'ok': 159, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 55, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 161}, 'backlog': {'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}, 'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 26}

## LLM Calls
- Total: 187
- Enrichment: 26
- Publish: 161

## Enrichment Backlog
- Remaining: 26
- embeddings: 0
- summaries: 24
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 9.09
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 41.23
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.16
- publish: 845.74
- persist_llm_cache: 0.18