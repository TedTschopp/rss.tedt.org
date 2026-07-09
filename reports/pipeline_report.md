# Pipeline Report

- Timestamp: 2026-07-09T17:59:05.553399Z
- Sources configured: 43
- Raw items: 1931
- Stories: 1875
- Clusters: 1870
- LLM: {'status': 'ok', 'calls': 146, 'ok': 146, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 53, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 135, 'ok': 135, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 53, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 135}}}}

## LLM Calls
- Total: 146
- Enrichment: 11
- Publish: 135

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.99
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 22.50
- cluster: 2.40
- score: 0.01
- write_intermediate_outputs: 0.24
- publish: 571.38
- persist_llm_cache: 3.16