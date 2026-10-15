# Pipeline Report

- Timestamp: 2026-10-15T16:14:18.098749Z
- Sources configured: 43
- Raw items: 2239
- Stories: 2185
- Clusters: 2155
- LLM: {'status': 'degraded', 'calls': 177, 'ok': 175, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 70, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 166, 'ok': 164, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 70, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 166}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 177
- Enrichment: 11
- Publish: 166

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.56
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 15.31
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.32
- publish: 421.02
- persist_llm_cache: 0.19