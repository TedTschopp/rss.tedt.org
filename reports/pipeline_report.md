# Pipeline Report

- Timestamp: 2026-08-24T03:59:42.587644Z
- Sources configured: 43
- Raw items: 1889
- Stories: 1878
- Clusters: 1848
- LLM: {'status': 'degraded', 'calls': 123, 'ok': 122, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 39, 'importance': 26, 'output_cleanup': 32}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 26, 'remaining': 0}, 'summaries': {'before': 35, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 97, 'ok': 96, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 39, 'importance': 26, 'output_cleanup': 32}, 'by_model': {'openai/gpt-4.1-mini': 97}, 'backlog': {'ai_relevance': {'before': 39, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 32, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 26, 'remaining': 0}, 'summaries': {'before': 35, 'remaining': 10}, 'ai_relevance': {'before': 39, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 32, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 123
- Enrichment: 26
- Publish: 97

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 4.00
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 44.06
- cluster: 0.29
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 516.06
- persist_llm_cache: 0.21