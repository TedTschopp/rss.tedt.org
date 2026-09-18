# Pipeline Report

- Timestamp: 2026-09-18T04:06:30.663545Z
- Sources configured: 43
- Raw items: 3381
- Stories: 2525
- Clusters: 2494
- LLM: {'status': 'degraded', 'calls': 394, 'ok': 391, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 164, 'importance': 157, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 47, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'degraded', 'calls': 368, 'ok': 365, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 164, 'importance': 157, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 368}, 'backlog': {'ai_relevance': {'before': 164, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 3}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 47, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 164, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 3}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 23}

## LLM Calls
- Total: 394
- Enrichment: 26
- Publish: 368

## Enrichment Backlog
- Remaining: 23
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.93
- normalize: 0.18
- dedupe: 0.09
- llm_enrich: 29.01
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.38
- publish: 1412.72
- persist_llm_cache: 0.22