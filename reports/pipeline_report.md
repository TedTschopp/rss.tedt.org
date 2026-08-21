# Pipeline Report

- Timestamp: 2026-08-21T04:16:00.398551Z
- Sources configured: 43
- Raw items: 3033
- Stories: 2342
- Clusters: 2313
- LLM: {'status': 'degraded', 'calls': 417, 'ok': 416, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 176, 'importance': 169, 'output_cleanup': 46}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}}}, 'publish': {'status': 'degraded', 'calls': 391, 'ok': 390, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 176, 'importance': 169, 'output_cleanup': 46}, 'by_model': {'openai/gpt-4.1-mini': 391}, 'backlog': {'ai_relevance': {'before': 176, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}, 'ai_relevance': {'before': 176, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 417
- Enrichment: 26
- Publish: 391

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 24
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.83
- normalize: 0.16
- dedupe: 0.08
- llm_enrich: 35.46
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.36
- publish: 1548.26
- persist_llm_cache: 0.23