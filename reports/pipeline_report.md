# Pipeline Report

- Timestamp: 2026-07-15T03:40:18.104523Z
- Sources configured: 43
- Raw items: 4562
- Stories: 2823
- Clusters: 2818
- LLM: {'status': 'ok', 'calls': 468, 'ok': 468, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 200, 'importance': 192, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 442, 'ok': 442, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 200, 'importance': 192, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 442}}}}

## LLM Calls
- Total: 468
- Enrichment: 26
- Publish: 442

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.81
- normalize: 0.15
- dedupe: 0.07
- llm_enrich: 45.62
- cluster: 1.56
- score: 0.01
- write_intermediate_outputs: 0.40
- publish: 2052.57
- persist_llm_cache: 0.21