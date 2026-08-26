# Pipeline Report

- Timestamp: 2026-08-26T16:42:33.632785Z
- Sources configured: 43
- Raw items: 2663
- Stories: 2605
- Clusters: 2577
- LLM: {'status': 'degraded', 'calls': 166, 'ok': 163, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 62, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 155, 'ok': 152, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 62, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 155}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 166
- Enrichment: 11
- Publish: 155

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.49
- normalize: 0.13
- dedupe: 0.07
- llm_enrich: 19.60
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.34
- publish: 834.45
- persist_llm_cache: 0.21