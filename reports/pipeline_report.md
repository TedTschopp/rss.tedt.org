# Pipeline Report

- Timestamp: 2026-11-06T21:28:02.668809Z
- Sources configured: 43
- Raw items: 2569
- Stories: 2514
- Clusters: 2486
- LLM: {'status': 'degraded', 'calls': 123, 'ok': 122, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 41, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 112, 'ok': 111, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 41, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 112}, 'backlog': {'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 123
- Enrichment: 11
- Publish: 112

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.11
- normalize: 0.10
- dedupe: 0.07
- llm_enrich: 13.81
- cluster: 0.24
- score: 0.03
- write_intermediate_outputs: 0.33
- publish: 282.76
- persist_llm_cache: 0.26