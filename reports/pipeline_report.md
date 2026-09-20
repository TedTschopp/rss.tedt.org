# Pipeline Report

- Timestamp: 2026-09-20T00:20:53.366104Z
- Sources configured: 43
- Raw items: 1994
- Stories: 1941
- Clusters: 1911
- LLM: {'status': 'degraded', 'calls': 125, 'ok': 122, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 56, 'importance': 38, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 114, 'ok': 111, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 56, 'importance': 38, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 114}, 'backlog': {'ai_relevance': {'before': 56, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 56, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 125
- Enrichment: 11
- Publish: 114

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.87
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 12.63
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 401.72
- persist_llm_cache: 0.21