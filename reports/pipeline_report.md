# Pipeline Report

- Timestamp: 2026-08-29T00:18:23.449390Z
- Sources configured: 43
- Raw items: 1921
- Stories: 1869
- Clusters: 1841
- LLM: {'status': 'degraded', 'calls': 78, 'ok': 75, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 26, 'importance': 22, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 67, 'ok': 64, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 26, 'importance': 22, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 67}, 'backlog': {'ai_relevance': {'before': 26, 'remaining': 1}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 26, 'remaining': 1}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 78
- Enrichment: 11
- Publish: 67

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.87
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 18.42
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 346.28
- persist_llm_cache: 0.21