# Pipeline Report

- Timestamp: 2026-08-16T00:12:56.906200Z
- Sources configured: 43
- Raw items: 1910
- Stories: 1864
- Clusters: 1835
- LLM: {'status': 'ok', 'calls': 108, 'ok': 108, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 26, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 97, 'ok': 97, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 26, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 97}, 'backlog': {'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 108
- Enrichment: 11
- Publish: 97

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.89
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 12.68
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 292.15
- persist_llm_cache: 0.21