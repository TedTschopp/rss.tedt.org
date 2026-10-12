# Pipeline Report

- Timestamp: 2026-10-12T16:13:49.125169Z
- Sources configured: 43
- Raw items: 2152
- Stories: 2098
- Clusters: 2069
- LLM: {'status': 'degraded', 'calls': 149, 'ok': 147, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 63, 'importance': 55, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 138, 'ok': 136, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 63, 'importance': 55, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 138}, 'backlog': {'ai_relevance': {'before': 63, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 63, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 149
- Enrichment: 11
- Publish: 138

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.32
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 14.60
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 430.28
- persist_llm_cache: 0.22