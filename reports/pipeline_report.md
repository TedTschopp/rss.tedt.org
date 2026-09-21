# Pipeline Report

- Timestamp: 2026-09-21T00:20:38.162122Z
- Sources configured: 43
- Raw items: 2020
- Stories: 1970
- Clusters: 1942
- LLM: {'status': 'degraded', 'calls': 104, 'ok': 101, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 41, 'importance': 32, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 93, 'ok': 90, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 41, 'importance': 32, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 93}, 'backlog': {'ai_relevance': {'before': 41, 'remaining': 0}, 'importance': {'before': 5, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 41, 'remaining': 0}, 'importance': {'before': 5, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 104
- Enrichment: 11
- Publish: 93

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.13
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 12.34
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 400.37
- persist_llm_cache: 0.21