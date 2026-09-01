# Pipeline Report

- Timestamp: 2026-09-01T08:19:53.945172Z
- Sources configured: 43
- Raw items: 5648
- Stories: 3618
- Clusters: 3589
- LLM: {'status': 'ok', 'calls': 181, 'ok': 181, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 72, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}}}, 'publish': {'status': 'ok', 'calls': 170, 'ok': 170, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 72, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 170}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 181
- Enrichment: 11
- Publish: 170

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 11
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.15
- normalize: 0.34
- dedupe: 0.16
- llm_enrich: 18.73
- cluster: 0.28
- score: 0.04
- write_intermediate_outputs: 0.63
- publish: 700.86
- persist_llm_cache: 0.23