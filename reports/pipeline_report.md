# Pipeline Report

- Timestamp: 2026-10-21T08:16:30.112827Z
- Sources configured: 43
- Raw items: 5128
- Stories: 3965
- Clusters: 3936
- LLM: {'status': 'ok', 'calls': 183, 'ok': 183, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 74, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 172, 'ok': 172, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 74, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 172}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 183
- Enrichment: 11
- Publish: 172

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.35
- normalize: 0.31
- dedupe: 0.14
- llm_enrich: 16.57
- cluster: 0.30
- score: 0.04
- write_intermediate_outputs: 0.60
- publish: 529.03
- persist_llm_cache: 0.25