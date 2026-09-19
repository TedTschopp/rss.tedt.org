# Pipeline Report

- Timestamp: 2026-09-19T08:10:04.640672Z
- Sources configured: 43
- Raw items: 1928
- Stories: 1875
- Clusters: 1844
- LLM: {'status': 'degraded', 'calls': 80, 'ok': 79, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 16, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 18, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 69, 'ok': 68, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 16, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 69}, 'backlog': {'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 18, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 80
- Enrichment: 11
- Publish: 69

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.88
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 12.75
- cluster: 0.22
- score: 0.01
- write_intermediate_outputs: 0.18
- publish: 202.74
- persist_llm_cache: 0.17