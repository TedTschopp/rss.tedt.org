# Pipeline Report

- Timestamp: 2026-08-01T08:52:56.122725Z
- Sources configured: 43
- Raw items: 1824
- Stories: 1790
- Clusters: 1761
- LLM: {'status': 'degraded', 'calls': 88, 'ok': 86, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 32, 'importance': 25, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 15, 'remaining': 0}, 'summaries': {'before': 15, 'remaining': 5}}}, 'publish': {'status': 'degraded', 'calls': 77, 'ok': 75, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 32, 'importance': 25, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 77}, 'backlog': {'ai_relevance': {'before': 32, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 15, 'remaining': 0}, 'summaries': {'before': 15, 'remaining': 5}, 'ai_relevance': {'before': 32, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 7}

## LLM Calls
- Total: 88
- Enrichment: 11
- Publish: 77

## Enrichment Backlog
- Remaining: 7
- embeddings: 0
- summaries: 5
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.53
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 15.86
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.32
- publish: 390.61
- persist_llm_cache: 0.17