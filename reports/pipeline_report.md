# Pipeline Report

- Timestamp: 2026-08-12T00:28:00.085583Z
- Sources configured: 43
- Raw items: 1689
- Stories: 1649
- Clusters: 1620
- LLM: {'status': 'degraded', 'calls': 133, 'ok': 131, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 44, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 122, 'ok': 120, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 44, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 122}, 'backlog': {'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 133
- Enrichment: 11
- Publish: 122

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 10.08
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 18.93
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.20
- publish: 560.57
- persist_llm_cache: 0.19