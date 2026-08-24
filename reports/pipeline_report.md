# Pipeline Report

- Timestamp: 2026-08-24T00:12:36.232650Z
- Sources configured: 43
- Raw items: 1914
- Stories: 1887
- Clusters: 1858
- LLM: {'status': 'degraded', 'calls': 81, 'ok': 79, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 32, 'importance': 22, 'output_cleanup': 16}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 70, 'ok': 68, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 32, 'importance': 22, 'output_cleanup': 16}, 'by_model': {'openai/gpt-4.1-mini': 70}, 'backlog': {'ai_relevance': {'before': 32, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 16, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 32, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 16, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 81
- Enrichment: 11
- Publish: 70

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 5.43
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 16.53
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.19
- publish: 272.11
- persist_llm_cache: 0.17