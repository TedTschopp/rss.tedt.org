# Pipeline Report

- Timestamp: 2026-07-15T08:14:32.941331Z
- Sources configured: 43
- Raw items: 1666
- Stories: 1629
- Clusters: 1563
- LLM: {'status': 'degraded', 'calls': 331, 'ok': 329, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 74, 'output_cleanup': 86}, 'stages': {'enrichment': {'status': 'ok', 'calls': 96, 'ok': 96, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 100, 'remaining': 0}, 'summaries': {'before': 95, 'remaining': 0}}}, 'publish': {'status': 'degraded', 'calls': 235, 'ok': 233, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 74, 'output_cleanup': 86}, 'by_model': {'openai/gpt-4.1-mini': 235}, 'backlog': {'ai_relevance': {'before': 113, 'remaining': 38}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 124, 'remaining': 38}}, 'backlog_remaining': 78}}, 'backlog': {'embeddings': {'before': 100, 'remaining': 0}, 'summaries': {'before': 95, 'remaining': 0}, 'ai_relevance': {'before': 113, 'remaining': 38}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 124, 'remaining': 38}}, 'backlog_remaining': 78}

## LLM Calls
- Total: 331
- Enrichment: 96
- Publish: 235

## Enrichment Backlog
- Remaining: 78
- embeddings: 0
- summaries: 0
- ai_relevance: 38
- importance: 2
- output_cleanup: 38

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.01
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 97.89
- cluster: 0.32
- score: 0.01
- write_intermediate_outputs: 0.28
- publish: 360.22
- persist_llm_cache: 0.22