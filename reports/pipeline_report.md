# Pipeline Report

- Timestamp: 2026-09-07T00:18:27.128004Z
- Sources configured: 43
- Raw items: 2026
- Stories: 1972
- Clusters: 1943
- LLM: {'status': 'degraded', 'calls': 98, 'ok': 97, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 27, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 87, 'ok': 86, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 27, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 87}, 'backlog': {'ai_relevance': {'before': 40, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 40, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 98
- Enrichment: 11
- Publish: 87

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.83
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 13.46
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 289.53
- persist_llm_cache: 0.20