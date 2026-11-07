# Pipeline Report

- Timestamp: 2026-11-07T14:51:06.178734Z
- Sources configured: 43
- Raw items: 2137
- Stories: 2093
- Clusters: 2063
- LLM: {'status': 'degraded', 'calls': 83, 'ok': 82, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 37, 'importance': 15, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 72, 'ok': 71, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 37, 'importance': 15, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 72}, 'backlog': {'ai_relevance': {'before': 37, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 37, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 83
- Enrichment: 11
- Publish: 72

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.17
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 13.55
- cluster: 0.15
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 274.99
- persist_llm_cache: 0.21