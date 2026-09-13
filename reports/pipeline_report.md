# Pipeline Report

- Timestamp: 2026-09-13T03:48:55.641762Z
- Sources configured: 43
- Raw items: 1870
- Stories: 1827
- Clusters: 1792
- LLM: {'status': 'ok', 'calls': 219, 'ok': 219, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 84, 'importance': 60, 'output_cleanup': 49}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 40, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}}}, 'publish': {'status': 'ok', 'calls': 193, 'ok': 193, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 84, 'importance': 60, 'output_cleanup': 49}, 'by_model': {'openai/gpt-4.1-mini': 193}, 'backlog': {'ai_relevance': {'before': 84, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 40, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}, 'ai_relevance': {'before': 84, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 16}

## LLM Calls
- Total: 219
- Enrichment: 26
- Publish: 193

## Enrichment Backlog
- Remaining: 16
- embeddings: 0
- summaries: 16
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.85
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 30.07
- cluster: 0.23
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 406.09
- persist_llm_cache: 0.17