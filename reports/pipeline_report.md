# Pipeline Report

- Timestamp: 2026-09-09T08:17:05.529324Z
- Sources configured: 43
- Raw items: 5615
- Stories: 3492
- Clusters: 3462
- LLM: {'status': 'ok', 'calls': 178, 'ok': 178, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 73, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 167, 'ok': 167, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 73, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 167}, 'backlog': {'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 178
- Enrichment: 11
- Publish: 167

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.72
- normalize: 0.29
- dedupe: 0.14
- llm_enrich: 15.10
- cluster: 0.24
- score: 0.04
- write_intermediate_outputs: 0.65
- publish: 544.44
- persist_llm_cache: 0.22