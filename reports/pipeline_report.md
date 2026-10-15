# Pipeline Report

- Timestamp: 2026-10-15T00:19:54.245722Z
- Sources configured: 43
- Raw items: 2128
- Stories: 2071
- Clusters: 2044
- LLM: {'status': 'degraded', 'calls': 161, 'ok': 159, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 60, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 150, 'ok': 148, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 60, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 150}, 'backlog': {'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 161
- Enrichment: 11
- Publish: 150

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 6.14
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 15.76
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.20
- publish: 446.22
- persist_llm_cache: 0.18