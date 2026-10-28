# Pipeline Report

- Timestamp: 2026-10-28T04:01:45.550817Z
- Sources configured: 43
- Raw items: 5218
- Stories: 3383
- Clusters: 3355
- LLM: {'status': 'degraded', 'calls': 406, 'ok': 405, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 169, 'importance': 165, 'output_cleanup': 46}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'degraded', 'calls': 380, 'ok': 379, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 169, 'importance': 165, 'output_cleanup': 46}, 'by_model': {'openai/gpt-4.1-mini': 380}, 'backlog': {'ai_relevance': {'before': 169, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 169, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 406
- Enrichment: 26
- Publish: 380

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 12.02
- normalize: 0.31
- dedupe: 0.14
- llm_enrich: 29.36
- cluster: 0.26
- score: 0.04
- write_intermediate_outputs: 0.57
- publish: 1372.54
- persist_llm_cache: 0.24