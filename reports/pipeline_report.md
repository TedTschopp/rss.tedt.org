# Pipeline Report

- Timestamp: 2026-09-01T16:38:36.424255Z
- Sources configured: 43
- Raw items: 2046
- Stories: 1990
- Clusters: 1962
- LLM: {'status': 'degraded', 'calls': 147, 'ok': 144, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 49, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 136, 'ok': 133, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 49, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 136}, 'backlog': {'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 147
- Enrichment: 11
- Publish: 136

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.59
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 22.73
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 635.25
- persist_llm_cache: 0.21