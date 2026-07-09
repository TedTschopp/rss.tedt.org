# Pipeline Report

- Timestamp: 2026-07-09T07:51:09.574577Z
- Sources configured: 43
- Raw items: 3106
- Stories: 2244
- Clusters: 2242
- LLM: {'status': 'ok', 'calls': 457, 'ok': 457, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 195, 'importance': 186, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 431, 'ok': 431, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 195, 'importance': 186, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 431}}}}

## LLM Calls
- Total: 457
- Enrichment: 26
- Publish: 431

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.54
- normalize: 0.17
- dedupe: 0.09
- llm_enrich: 63.40
- cluster: 3.09
- score: 0.01
- write_intermediate_outputs: 0.36
- publish: 2520.81
- persist_llm_cache: 3.10