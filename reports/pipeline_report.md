# Pipeline Report

- Timestamp: 2026-08-02T08:53:29.604464Z
- Sources configured: 43
- Raw items: 1871
- Stories: 1827
- Clusters: 1799
- LLM: {'status': 'ok', 'calls': 102, 'ok': 102, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 41, 'importance': 30, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 91, 'ok': 91, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 41, 'importance': 30, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 91}, 'backlog': {'ai_relevance': {'before': 41, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 41, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 102
- Enrichment: 11
- Publish: 91

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.10
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 13.45
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 344.66
- persist_llm_cache: 0.21