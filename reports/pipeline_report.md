# Pipeline Report

- Timestamp: 2026-07-10T10:52:03.611368Z
- Sources configured: 43
- Raw items: 1803
- Stories: 1763
- Clusters: 1760
- LLM: {'status': 'degraded', 'calls': 90, 'ok': 89, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 26, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'degraded', 'calls': 79, 'ok': 78, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 26, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 79}}}}

## LLM Calls
- Total: 90
- Enrichment: 11
- Publish: 79

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.70
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 21.56
- cluster: 2.06
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 347.01
- persist_llm_cache: 3.18