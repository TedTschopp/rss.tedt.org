# Pipeline Report

- Timestamp: 2026-09-29T00:22:33.257284Z
- Sources configured: 43
- Raw items: 2204
- Stories: 2149
- Clusters: 2121
- LLM: {'status': 'degraded', 'calls': 162, 'ok': 159, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 59, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 151, 'ok': 148, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 59, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 151}, 'backlog': {'ai_relevance': {'before': 72, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 72, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 162
- Enrichment: 11
- Publish: 151

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.48
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 15.83
- cluster: 0.23
- score: 0.03
- write_intermediate_outputs: 0.26
- publish: 458.12
- persist_llm_cache: 0.20