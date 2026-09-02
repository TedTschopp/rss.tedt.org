# Pipeline Report

- Timestamp: 2026-09-02T04:07:35.888808Z
- Sources configured: 43
- Raw items: 5387
- Stories: 3360
- Clusters: 3332
- LLM: {'status': 'degraded', 'calls': 388, 'ok': 387, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 161, 'importance': 158, 'output_cleanup': 43}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}}}, 'publish': {'status': 'degraded', 'calls': 362, 'ok': 361, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 161, 'importance': 158, 'output_cleanup': 43}, 'by_model': {'openai/gpt-4.1-mini': 362}, 'backlog': {'ai_relevance': {'before': 161, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 43, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}, 'ai_relevance': {'before': 161, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 43, 'remaining': 0}}, 'backlog_remaining': 23}

## LLM Calls
- Total: 388
- Enrichment: 26
- Publish: 362

## Enrichment Backlog
- Remaining: 23
- embeddings: 0
- summaries: 22
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 3.23
- normalize: 0.21
- dedupe: 0.10
- llm_enrich: 39.55
- cluster: 0.18
- score: 0.02
- write_intermediate_outputs: 0.53
- publish: 1546.41
- persist_llm_cache: 0.15