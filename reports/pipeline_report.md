# Pipeline Report

- Timestamp: 2026-10-31T00:16:59.877887Z
- Sources configured: 43
- Raw items: 2193
- Stories: 2131
- Clusters: 2104
- LLM: {'status': 'degraded', 'calls': 146, 'ok': 142, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 50, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 135, 'ok': 131, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 50, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 135}, 'backlog': {'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 146
- Enrichment: 11
- Publish: 135

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 4.78
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 14.89
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 509.94
- persist_llm_cache: 0.26