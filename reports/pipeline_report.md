# Pipeline Report

- Timestamp: 2026-09-13T00:19:58.255933Z
- Sources configured: 43
- Raw items: 2034
- Stories: 1980
- Clusters: 1950
- LLM: {'status': 'degraded', 'calls': 159, 'ok': 158, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 57, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 17, 'remaining': 0}, 'summaries': {'before': 18, 'remaining': 8}}}, 'publish': {'status': 'degraded', 'calls': 148, 'ok': 147, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 57, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 148}, 'backlog': {'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 17, 'remaining': 0}, 'summaries': {'before': 18, 'remaining': 8}, 'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 159
- Enrichment: 11
- Publish: 148

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 8
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 4.38
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 14.20
- cluster: 0.19
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 363.77
- persist_llm_cache: 0.14