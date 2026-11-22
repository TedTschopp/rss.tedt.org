# Pipeline Report

- Timestamp: 2026-11-22T21:47:44.022101Z
- Sources configured: 43
- Raw items: 2139
- Stories: 2112
- Clusters: 2084
- LLM: {'status': 'degraded', 'calls': 85, 'ok': 84, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 21, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 74, 'ok': 73, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 21, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 74}, 'backlog': {'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 85
- Enrichment: 11
- Publish: 74

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.16
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 12.67
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.18
- publish: 269.99
- persist_llm_cache: 0.22