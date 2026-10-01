# Pipeline Report

- Timestamp: 2026-10-01T04:08:33.056882Z
- Sources configured: 43
- Raw items: 5027
- Stories: 3229
- Clusters: 3198
- LLM: {'status': 'degraded', 'calls': 389, 'ok': 388, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 162, 'importance': 159, 'output_cleanup': 42}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'degraded', 'calls': 363, 'ok': 362, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 162, 'importance': 159, 'output_cleanup': 42}, 'by_model': {'openai/gpt-4.1-mini': 363}, 'backlog': {'ai_relevance': {'before': 162, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 162, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 389
- Enrichment: 26
- Publish: 363

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 5.22
- normalize: 0.30
- dedupe: 0.14
- llm_enrich: 33.54
- cluster: 0.28
- score: 0.04
- write_intermediate_outputs: 0.55
- publish: 1043.59
- persist_llm_cache: 0.24