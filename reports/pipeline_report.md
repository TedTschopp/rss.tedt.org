# Pipeline Report

- Timestamp: 2026-08-17T00:16:22.380718Z
- Sources configured: 43
- Raw items: 1945
- Stories: 1898
- Clusters: 1866
- LLM: {'status': 'degraded', 'calls': 137, 'ok': 135, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 45, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 126, 'ok': 124, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 45, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 126}, 'backlog': {'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

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
- ingestion: 2.00
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 13.83
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 535.55
- persist_llm_cache: 0.21