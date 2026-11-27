# Pipeline Report

- Timestamp: 2026-11-27T18:03:48.169860Z
- Sources configured: 43
- Raw items: 2200
- Stories: 2173
- Clusters: 2140
- LLM: {'status': 'ok', 'calls': 121, 'ok': 121, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 54, 'importance': 36, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 110, 'ok': 110, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 54, 'importance': 36, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 110}, 'backlog': {'ai_relevance': {'before': 54, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 54, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 121
- Enrichment: 11
- Publish: 110

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.54
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 14.30
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 417.13
- persist_llm_cache: 0.27