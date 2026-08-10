# Pipeline Report

- Timestamp: 2026-08-10T00:20:37.934480Z
- Sources configured: 43
- Raw items: 1924
- Stories: 1875
- Clusters: 1845
- LLM: {'status': 'degraded', 'calls': 99, 'ok': 97, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 28, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 88, 'ok': 86, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 40, 'importance': 28, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 88}, 'backlog': {'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 40, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 99
- Enrichment: 11
- Publish: 88

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.05
- normalize: 0.09
- dedupe: 0.07
- llm_enrich: 15.97
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 475.04
- persist_llm_cache: 0.22