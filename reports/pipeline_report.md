# Pipeline Report

- Timestamp: 2026-07-10T07:37:29.011103Z
- Sources configured: 43
- Raw items: 3154
- Stories: 2490
- Clusters: 2488
- LLM: {'status': 'ok', 'calls': 457, 'ok': 457, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 183, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 431, 'ok': 431, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 183, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 431}}}}

## LLM Calls
- Total: 457
- Enrichment: 26
- Publish: 431

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 26.11
- normalize: 0.16
- dedupe: 0.10
- llm_enrich: 56.11
- cluster: 4.18
- score: 0.02
- write_intermediate_outputs: 0.38
- publish: 1991.65
- persist_llm_cache: 3.25