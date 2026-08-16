# Pipeline Report

- Timestamp: 2026-08-16T03:59:56.073326Z
- Sources configured: 43
- Raw items: 1895
- Stories: 1862
- Clusters: 1833
- LLM: {'status': 'degraded', 'calls': 184, 'ok': 183, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 41, 'output_cleanup': 49}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 36, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}}}, 'publish': {'status': 'degraded', 'calls': 158, 'ok': 157, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 41, 'output_cleanup': 49}, 'by_model': {'openai/gpt-4.1-mini': 158}, 'backlog': {'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 36, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}, 'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 19}

## LLM Calls
- Total: 184
- Enrichment: 26
- Publish: 158

## Enrichment Backlog
- Remaining: 19
- embeddings: 0
- summaries: 18
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.28
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 31.21
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 609.02
- persist_llm_cache: 0.20