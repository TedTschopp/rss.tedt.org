# Pipeline Report

- Timestamp: 2026-08-16T16:11:58.377978Z
- Sources configured: 43
- Raw items: 1990
- Stories: 1942
- Clusters: 1911
- LLM: {'status': 'degraded', 'calls': 116, 'ok': 115, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 35, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 105, 'ok': 104, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 35, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 105}, 'backlog': {'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 116
- Enrichment: 11
- Publish: 105

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.81
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 13.17
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 440.57
- persist_llm_cache: 0.20