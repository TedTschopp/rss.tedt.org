# Pipeline Report

- Timestamp: 2026-10-07T00:21:01.956392Z
- Sources configured: 43
- Raw items: 2084
- Stories: 2027
- Clusters: 1998
- LLM: {'status': 'ok', 'calls': 153, 'ok': 153, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 56, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 142, 'ok': 142, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 56, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 142}, 'backlog': {'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 153
- Enrichment: 11
- Publish: 142

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.49
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 15.92
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 429.14
- persist_llm_cache: 0.23