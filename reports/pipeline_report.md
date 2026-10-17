# Pipeline Report

- Timestamp: 2026-10-17T16:10:28.300940Z
- Sources configured: 43
- Raw items: 2143
- Stories: 2090
- Clusters: 2062
- LLM: {'status': 'ok', 'calls': 119, 'ok': 119, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 37, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 108, 'ok': 108, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 37, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 108}, 'backlog': {'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 119
- Enrichment: 11
- Publish: 108

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.15
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 14.17
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.18
- publish: 277.34
- persist_llm_cache: 0.18