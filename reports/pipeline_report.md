# Pipeline Report

- Timestamp: 2026-07-11T09:23:24.022901Z
- Sources configured: 43
- Raw items: 1764
- Stories: 1721
- Clusters: 1717
- LLM: {'status': 'ok', 'calls': 82, 'ok': 82, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 32, 'importance': 19, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 71, 'ok': 71, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 32, 'importance': 19, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 71}}}}

## LLM Calls
- Total: 82
- Enrichment: 11
- Publish: 71

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.03
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 21.86
- cluster: 1.96
- score: 0.01
- write_intermediate_outputs: 0.21
- publish: 234.63
- persist_llm_cache: 3.39