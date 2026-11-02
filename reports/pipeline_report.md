# Pipeline Report

- Timestamp: 2026-11-02T03:31:51.351851Z
- Sources configured: 43
- Raw items: 2163
- Stories: 2115
- Clusters: 2088
- LLM: {'status': 'degraded', 'calls': 99, 'ok': 98, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 25, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 88, 'ok': 87, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 25, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 88}, 'backlog': {'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 99
- Enrichment: 11
- Publish: 88

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 4.35
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 13.11
- cluster: 0.17
- score: 0.02
- write_intermediate_outputs: 0.21
- publish: 253.46
- persist_llm_cache: 0.19