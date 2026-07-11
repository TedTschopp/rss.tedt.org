# Pipeline Report

- Timestamp: 2026-07-11T06:13:28.029253Z
- Sources configured: 43
- Raw items: 2069
- Stories: 2024
- Clusters: 2022
- LLM: {'status': 'ok', 'calls': 227, 'ok': 227, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 113, 'importance': 41, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 23, 'ok': 23, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 204, 'ok': 204, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 113, 'importance': 41, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 204}}}}

## LLM Calls
- Total: 227
- Enrichment: 23
- Publish: 204

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.42
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 56.95
- cluster: 2.96
- score: 0.01
- write_intermediate_outputs: 0.26
- publish: 758.45
- persist_llm_cache: 3.49