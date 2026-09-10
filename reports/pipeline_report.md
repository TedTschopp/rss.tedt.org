# Pipeline Report

- Timestamp: 2026-09-10T08:17:08.861156Z
- Sources configured: 43
- Raw items: 3948
- Stories: 3230
- Clusters: 3197
- LLM: {'status': 'ok', 'calls': 182, 'ok': 182, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 74, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 171, 'ok': 171, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 74, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 171}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 182
- Enrichment: 11
- Publish: 171

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.35
- normalize: 0.23
- dedupe: 0.12
- llm_enrich: 17.29
- cluster: 0.28
- score: 0.04
- write_intermediate_outputs: 0.47
- publish: 595.47
- persist_llm_cache: 0.22