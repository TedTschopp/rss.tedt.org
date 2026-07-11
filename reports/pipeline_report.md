# Pipeline Report

- Timestamp: 2026-07-11T01:54:32.175365Z
- Sources configured: 43
- Raw items: 1829
- Stories: 1778
- Clusters: 1775
- LLM: {'status': 'ok', 'calls': 116, 'ok': 116, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 47, 'importance': 38, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 105, 'ok': 105, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 47, 'importance': 38, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 105}}}}

## LLM Calls
- Total: 116
- Enrichment: 11
- Publish: 105

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.10
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 17.43
- cluster: 1.93
- score: 0.01
- write_intermediate_outputs: 0.23
- publish: 381.62
- persist_llm_cache: 3.29