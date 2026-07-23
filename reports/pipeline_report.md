# Pipeline Report

- Timestamp: 2026-07-23T08:59:01.947043Z
- Sources configured: 43
- Raw items: 1752
- Stories: 1723
- Clusters: 1694
- LLM: {'status': 'degraded', 'calls': 88, 'ok': 87, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 24, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 77, 'ok': 76, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 24, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 77}, 'backlog': {'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 88
- Enrichment: 11
- Publish: 77

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.78
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 16.61
- cluster: 0.20
- score: 0.01
- write_intermediate_outputs: 0.20
- publish: 373.97
- persist_llm_cache: 0.23