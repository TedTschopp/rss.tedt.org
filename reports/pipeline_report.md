# Pipeline Report

- Timestamp: 2026-08-27T01:28:01.334784Z
- Sources configured: 43
- Raw items: 2602
- Stories: 2542
- Clusters: 2514
- LLM: {'status': 'degraded', 'calls': 139, 'ok': 136, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 49, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 128, 'ok': 125, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 49, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 128}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 1}, 'importance': {'before': 3, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 59, 'remaining': 1}, 'importance': {'before': 3, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 139
- Enrichment: 11
- Publish: 128

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.78
- normalize: 0.11
- dedupe: 0.07
- llm_enrich: 16.40
- cluster: 0.27
- score: 0.03
- write_intermediate_outputs: 0.34
- publish: 660.96
- persist_llm_cache: 0.22