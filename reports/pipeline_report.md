# Pipeline Report

- Timestamp: 2026-08-22T16:12:14.464443Z
- Sources configured: 43
- Raw items: 2009
- Stories: 1958
- Clusters: 1930
- LLM: {'status': 'ok', 'calls': 111, 'ok': 111, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 36, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 100, 'ok': 100, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 44, 'importance': 36, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 100}, 'backlog': {'ai_relevance': {'before': 44, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 44, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 111
- Enrichment: 11
- Publish: 100

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.56
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 22.24
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 418.60
- persist_llm_cache: 0.21