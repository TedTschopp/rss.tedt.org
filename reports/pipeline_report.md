# Pipeline Report

- Timestamp: 2026-09-27T16:12:38.610377Z
- Sources configured: 43
- Raw items: 2090
- Stories: 2041
- Clusters: 2012
- LLM: {'status': 'degraded', 'calls': 137, 'ok': 135, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 47, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 126, 'ok': 124, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 47, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 126}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 137
- Enrichment: 11
- Publish: 126

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.72
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 11.93
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 383.16
- persist_llm_cache: 0.21