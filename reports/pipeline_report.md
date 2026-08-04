# Pipeline Report

- Timestamp: 2026-08-04T09:03:09.433024Z
- Sources configured: 43
- Raw items: 1839
- Stories: 1806
- Clusters: 1776
- LLM: {'status': 'degraded', 'calls': 84, 'ok': 82, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 35, 'importance': 18, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 73, 'ok': 71, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 35, 'importance': 18, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 73}, 'backlog': {'ai_relevance': {'before': 35, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 35, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 84
- Enrichment: 11
- Publish: 73

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.62
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 19.53
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.21
- publish: 350.59
- persist_llm_cache: 0.19