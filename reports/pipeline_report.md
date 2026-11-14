# Pipeline Report

- Timestamp: 2026-11-14T14:57:14.750638Z
- Sources configured: 43
- Raw items: 2220
- Stories: 2175
- Clusters: 2147
- LLM: {'status': 'ok', 'calls': 107, 'ok': 107, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 32, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 96, 'ok': 96, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 32, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 96}, 'backlog': {'ai_relevance': {'before': 44, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 44, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 107
- Enrichment: 11
- Publish: 96

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.13
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 12.86
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.34
- publish: 279.23
- persist_llm_cache: 0.29