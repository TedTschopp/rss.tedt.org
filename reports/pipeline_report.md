# Pipeline Report

- Timestamp: 2026-07-08T06:45:43.336122Z
- Sources configured: 43
- Raw items: 3263
- Stories: 2319
- Clusters: 2316
- LLM: {'status': 'ok', 'calls': 455, 'ok': 455, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 181, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 429, 'ok': 429, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 181, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 429}}}}

## LLM Calls
- Total: 455
- Enrichment: 26
- Publish: 429

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.70
- normalize: 0.17
- dedupe: 0.08
- llm_enrich: 63.82
- cluster: 3.17
- score: 0.01
- write_intermediate_outputs: 0.36
- publish: 1768.58
- persist_llm_cache: 2.89