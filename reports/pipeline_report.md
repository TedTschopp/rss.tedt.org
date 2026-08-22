# Pipeline Report

- Timestamp: 2026-08-22T00:14:59.481725Z
- Sources configured: 43
- Raw items: 1971
- Stories: 1921
- Clusters: 1892
- LLM: {'status': 'degraded', 'calls': 122, 'ok': 121, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 52, 'importance': 40, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 111, 'ok': 110, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 52, 'importance': 40, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 111}, 'backlog': {'ai_relevance': {'before': 52, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 52, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 122
- Enrichment: 11
- Publish: 111

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.55
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 14.92
- cluster: 0.16
- score: 0.01
- write_intermediate_outputs: 0.17
- publish: 401.89
- persist_llm_cache: 0.12