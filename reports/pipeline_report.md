# Pipeline Report

- Timestamp: 2026-10-06T04:03:03.622408Z
- Sources configured: 43
- Raw items: 2781
- Stories: 2737
- Clusters: 2708
- LLM: {'status': 'degraded', 'calls': 347, 'ok': 345, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 142, 'importance': 135, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 34, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}}}, 'publish': {'status': 'degraded', 'calls': 321, 'ok': 319, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 142, 'importance': 135, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 321}, 'backlog': {'ai_relevance': {'before': 142, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 34, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}, 'ai_relevance': {'before': 142, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 18}

## LLM Calls
- Total: 347
- Enrichment: 26
- Publish: 321

## Enrichment Backlog
- Remaining: 18
- embeddings: 0
- summaries: 16
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.23
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 31.72
- cluster: 0.16
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 938.42
- persist_llm_cache: 0.19