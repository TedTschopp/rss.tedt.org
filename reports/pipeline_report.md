# Pipeline Report

- Timestamp: 2026-07-27T09:16:31.192404Z
- Sources configured: 43
- Raw items: 1842
- Stories: 1798
- Clusters: 1770
- LLM: {'status': 'degraded', 'calls': 133, 'ok': 132, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 54, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 122, 'ok': 121, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 54, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 122}, 'backlog': {'ai_relevance': {'before': 54, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 54, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 133
- Enrichment: 11
- Publish: 122

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.96
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 17.98
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 655.27
- persist_llm_cache: 0.20