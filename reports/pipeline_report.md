# Pipeline Report

- Timestamp: 2026-08-28T11:54:20.628211Z
- Sources configured: 43
- Raw items: 2011
- Stories: 1947
- Clusters: 1919
- LLM: {'status': 'degraded', 'calls': 103, 'ok': 102, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 32, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 92, 'ok': 91, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 32, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 92}, 'backlog': {'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 103
- Enrichment: 11
- Publish: 92

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.96
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 17.22
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 423.61
- persist_llm_cache: 0.21