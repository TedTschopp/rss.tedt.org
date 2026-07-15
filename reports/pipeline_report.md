# Pipeline Report

- Timestamp: 2026-07-15T05:02:57.771242Z
- Sources configured: 43
- Raw items: 3268
- Stories: 2626
- Clusters: 2621
- LLM: {'status': 'ok', 'calls': 1003, 'ok': 1003, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 250, 'output_cleanup': 250}, 'stages': {'enrichment': {'status': 'ok', 'calls': 253, 'ok': 253, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 2584, 'remaining': 2334}, 'summaries': {'before': 2563, 'remaining': 2313}}}, 'publish': {'status': 'ok', 'calls': 750, 'ok': 750, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 250, 'output_cleanup': 250}, 'by_model': {'openai/gpt-4.1-mini': 750}, 'backlog': {'ai_relevance': {'before': 2150, 'remaining': 1900}, 'importance': {'before': 38, 'remaining': 24}, 'output_cleanup': {'before': 2349, 'remaining': 2099}}, 'backlog_remaining': 4023}}, 'backlog': {'embeddings': {'before': 2584, 'remaining': 2334}, 'summaries': {'before': 2563, 'remaining': 2313}, 'ai_relevance': {'before': 2150, 'remaining': 1900}, 'importance': {'before': 38, 'remaining': 24}, 'output_cleanup': {'before': 2349, 'remaining': 2099}}, 'backlog_remaining': 8670}

## LLM Calls
- Total: 1003
- Enrichment: 253
- Publish: 750

## Enrichment Backlog
- Remaining: 8670
- embeddings: 2334
- summaries: 2313
- ai_relevance: 1900
- importance: 24
- output_cleanup: 2099

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.86
- normalize: 0.16
- dedupe: 0.10
- llm_enrich: 610.75
- cluster: 0.09
- score: 0.03
- write_intermediate_outputs: 0.41
- publish: 2300.02
- persist_llm_cache: 0.14