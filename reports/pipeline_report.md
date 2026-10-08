# Pipeline Report

- Timestamp: 2026-10-08T08:20:06.332941Z
- Sources configured: 43
- Raw items: 4610
- Stories: 3390
- Clusters: 3360
- LLM: {'status': 'degraded', 'calls': 179, 'ok': 177, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 73, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 168, 'ok': 166, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 73, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 168}, 'backlog': {'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 179
- Enrichment: 11
- Publish: 168

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.39
- normalize: 0.19
- dedupe: 0.10
- llm_enrich: 14.80
- cluster: 0.22
- score: 0.03
- write_intermediate_outputs: 0.53
- publish: 591.43
- persist_llm_cache: 0.24