# Pipeline Report

- Timestamp: 2026-07-10T17:49:03.912520Z
- Sources configured: 43
- Raw items: 1920
- Stories: 1867
- Clusters: 1862
- LLM: {'status': 'ok', 'calls': 99, 'ok': 99, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 27, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 88, 'ok': 88, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 27, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 88}}}}

## LLM Calls
- Total: 99
- Enrichment: 11
- Publish: 88

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.46
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 24.45
- cluster: 1.80
- score: 0.01
- write_intermediate_outputs: 0.20
- publish: 355.50
- persist_llm_cache: 3.31