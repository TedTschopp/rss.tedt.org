# Pipeline Report

- Timestamp: 2026-08-12T08:37:05.549259Z
- Sources configured: 43
- Raw items: 1896
- Stories: 1863
- Clusters: 1835
- LLM: {'status': 'degraded', 'calls': 99, 'ok': 98, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 28, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 88, 'ok': 87, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 28, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 88}, 'backlog': {'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

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
- load_sources_and_state: 0.02
- ingestion: 2.18
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 19.19
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 450.57
- persist_llm_cache: 0.20