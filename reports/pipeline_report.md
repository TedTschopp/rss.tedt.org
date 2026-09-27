# Pipeline Report

- Timestamp: 2026-09-27T08:12:02.293650Z
- Sources configured: 43
- Raw items: 1982
- Stories: 1943
- Clusters: 1914
- LLM: {'status': 'degraded', 'calls': 108, 'ok': 106, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 29, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 97, 'ok': 95, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 29, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 97}, 'backlog': {'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 108
- Enrichment: 11
- Publish: 97

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.00
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 12.71
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 285.38
- persist_llm_cache: 0.23