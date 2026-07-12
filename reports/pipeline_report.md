# Pipeline Report

- Timestamp: 2026-07-12T09:50:41.491151Z
- Sources configured: 43
- Raw items: 1741
- Stories: 1701
- Clusters: 1697
- LLM: {'status': 'degraded', 'calls': 81, 'ok': 79, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 29, 'importance': 21, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0}, 'publish': {'status': 'degraded', 'calls': 70, 'ok': 68, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 29, 'importance': 21, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 70}}}}

## LLM Calls
- Total: 81
- Enrichment: 11
- Publish: 70

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.59
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 20.86
- cluster: 1.74
- score: 0.01
- write_intermediate_outputs: 0.20
- publish: 339.89
- persist_llm_cache: 3.35