# Pipeline Report

- Timestamp: 2026-07-11T16:49:19.729052Z
- Sources configured: 43
- Raw items: 1896
- Stories: 1849
- Clusters: 1845
- LLM: {'status': 'ok', 'calls': 88, 'ok': 88, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 35, 'importance': 22, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 77, 'ok': 77, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 35, 'importance': 22, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 77}}}}

## LLM Calls
- Total: 88
- Enrichment: 11
- Publish: 77

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.08
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 21.04
- cluster: 1.84
- score: 0.01
- write_intermediate_outputs: 0.23
- publish: 265.30
- persist_llm_cache: 3.45