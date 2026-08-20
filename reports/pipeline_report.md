# Pipeline Report

- Timestamp: 2026-08-20T04:13:15.720462Z
- Sources configured: 43
- Raw items: 3166
- Stories: 2475
- Clusters: 2444
- LLM: {'status': 'ok', 'calls': 381, 'ok': 381, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 159, 'importance': 151, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'ok', 'calls': 355, 'ok': 355, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 159, 'importance': 151, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 355}, 'backlog': {'ai_relevance': {'before': 159, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 159, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 17}

## LLM Calls
- Total: 381
- Enrichment: 26
- Publish: 355

## Enrichment Backlog
- Remaining: 17
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.95
- normalize: 0.17
- dedupe: 0.09
- llm_enrich: 36.11
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.37
- publish: 1402.16
- persist_llm_cache: 0.22