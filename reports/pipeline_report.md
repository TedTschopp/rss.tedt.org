# Pipeline Report

- Timestamp: 2026-10-25T00:19:51.841310Z
- Sources configured: 43
- Raw items: 2063
- Stories: 2011
- Clusters: 1982
- LLM: {'status': 'degraded', 'calls': 110, 'ok': 107, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 31, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 99, 'ok': 96, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 31, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 99}, 'backlog': {'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 110
- Enrichment: 11
- Publish: 99

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 4.02
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 14.14
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 403.51
- persist_llm_cache: 0.22