# Pipeline Report

- Timestamp: 2026-11-12T11:57:14.955776Z
- Sources configured: 43
- Raw items: 2220
- Stories: 2170
- Clusters: 2140
- LLM: {'status': 'degraded', 'calls': 189, 'ok': 188, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 53, 'output_cleanup': 43}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}}}, 'publish': {'status': 'degraded', 'calls': 163, 'ok': 162, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 53, 'output_cleanup': 43}, 'by_model': {'openai/gpt-4.1-mini': 163}, 'backlog': {'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 43, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}, 'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 43, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 189
- Enrichment: 26
- Publish: 163

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 24
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.24
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 34.13
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.28
- publish: 894.31
- persist_llm_cache: 0.28