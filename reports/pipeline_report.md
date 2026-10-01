# Pipeline Report

- Timestamp: 2026-10-01T16:15:55.072998Z
- Sources configured: 43
- Raw items: 2131
- Stories: 2081
- Clusters: 2053
- LLM: {'status': 'degraded', 'calls': 163, 'ok': 162, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 58, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 152, 'ok': 151, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 58, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 152}, 'backlog': {'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 163
- Enrichment: 11
- Publish: 152

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.51
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 15.17
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 506.99
- persist_llm_cache: 0.25