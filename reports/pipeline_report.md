# Pipeline Report

- Timestamp: 2026-09-06T00:20:17.817030Z
- Sources configured: 43
- Raw items: 1981
- Stories: 1934
- Clusters: 1904
- LLM: {'status': 'degraded', 'calls': 119, 'ok': 117, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 29, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 108, 'ok': 106, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 29, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 108}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 119
- Enrichment: 11
- Publish: 108

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.58
- normalize: 0.05
- dedupe: 0.03
- llm_enrich: 14.77
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.16
- publish: 355.84
- persist_llm_cache: 0.14