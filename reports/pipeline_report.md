# Pipeline Report

- Timestamp: 2026-10-03T15:56:39.895360Z
- Sources configured: 43
- Raw items: 2115
- Stories: 2058
- Clusters: 2031
- LLM: {'status': 'degraded', 'calls': 289, 'ok': 286, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 126, 'importance': 87, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'degraded', 'calls': 263, 'ok': 260, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 126, 'importance': 87, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 263}, 'backlog': {'ai_relevance': {'before': 126, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 3}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 126, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 3}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 28}

## LLM Calls
- Total: 289
- Enrichment: 26
- Publish: 263

## Enrichment Backlog
- Remaining: 28
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.04
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 33.26
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 1123.99
- persist_llm_cache: 0.22