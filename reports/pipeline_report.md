# Pipeline Report

- Timestamp: 2026-07-09T10:53:27.819595Z
- Sources configured: 43
- Raw items: 1764
- Stories: 1725
- Clusters: 1723
- LLM: {'status': 'ok', 'calls': 113, 'ok': 113, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 36, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'ok', 'calls': 102, 'ok': 102, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 36, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 102}}}}

## LLM Calls
- Total: 113
- Enrichment: 11
- Publish: 102

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.86
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 24.61
- cluster: 2.00
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 370.69
- persist_llm_cache: 3.13