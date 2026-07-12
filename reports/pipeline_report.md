# Pipeline Report

- Timestamp: 2026-07-12T16:55:57.051088Z
- Sources configured: 43
- Raw items: 1874
- Stories: 1827
- Clusters: 1824
- LLM: {'status': 'degraded', 'calls': 100, 'ok': 98, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 41, 'importance': 29, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 10, 'ok': 10, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'degraded', 'calls': 90, 'ok': 88, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 41, 'importance': 29, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 90}}}}

## LLM Calls
- Total: 100
- Enrichment: 10
- Publish: 90

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.04
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 18.25
- cluster: 2.01
- score: 0.01
- write_intermediate_outputs: 0.23
- publish: 424.33
- persist_llm_cache: 3.43