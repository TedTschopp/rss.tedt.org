# Pipeline Report

- Timestamp: 2026-08-07T01:25:05.049548Z
- Sources configured: 43
- Raw items: 2038
- Stories: 1981
- Clusters: 1953
- LLM: {'status': 'degraded', 'calls': 181, 'ok': 180, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 70, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 170, 'ok': 169, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 70, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 170}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 181
- Enrichment: 11
- Publish: 170

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.60
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 17.26
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 839.48
- persist_llm_cache: 0.22