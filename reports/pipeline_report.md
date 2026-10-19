# Pipeline Report

- Timestamp: 2026-10-19T16:16:03.253603Z
- Sources configured: 43
- Raw items: 2160
- Stories: 2110
- Clusters: 2081
- LLM: {'status': 'degraded', 'calls': 150, 'ok': 146, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 52, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 139, 'ok': 135, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 52, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 139}, 'backlog': {'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 150
- Enrichment: 11
- Publish: 139

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.41
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 15.40
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 559.64
- persist_llm_cache: 0.22