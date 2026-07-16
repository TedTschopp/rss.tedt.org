# Pipeline Report

- Timestamp: 2026-07-16T10:08:38.713662Z
- Sources configured: 43
- Raw items: 1851
- Stories: 1797
- Clusters: 1753
- LLM: {'status': 'degraded', 'calls': 106, 'ok': 104, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 41, 'importance': 34, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 95, 'ok': 93, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 41, 'importance': 34, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 95}, 'backlog': {'ai_relevance': {'before': 41, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 41, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 106
- Enrichment: 11
- Publish: 95

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.15
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 20.84
- cluster: 0.26
- score: 0.01
- write_intermediate_outputs: 0.21
- publish: 574.61
- persist_llm_cache: 0.19