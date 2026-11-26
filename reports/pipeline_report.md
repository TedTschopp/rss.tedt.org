# Pipeline Report

- Timestamp: 2026-11-26T07:30:21.752656Z
- Sources configured: 43
- Raw items: 4505
- Stories: 3451
- Clusters: 3420
- LLM: {'status': 'degraded', 'calls': 187, 'ok': 186, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 76, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 176, 'ok': 175, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 76, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 176}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 187
- Enrichment: 11
- Publish: 176

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.27
- normalize: 0.16
- dedupe: 0.08
- llm_enrich: 18.37
- cluster: 0.17
- score: 0.02
- write_intermediate_outputs: 0.38
- publish: 816.19
- persist_llm_cache: 0.19