# Pipeline Report

- Timestamp: 2026-10-15T08:13:45.159366Z
- Sources configured: 43
- Raw items: 6519
- Stories: 4276
- Clusters: 4246
- LLM: {'status': 'ok', 'calls': 180, 'ok': 180, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 72, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 169, 'ok': 169, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 72, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 169}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 180
- Enrichment: 11
- Publish: 169

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.52
- normalize: 0.40
- dedupe: 0.17
- llm_enrich: 15.02
- cluster: 0.29
- score: 0.04
- write_intermediate_outputs: 0.72
- publish: 406.93
- persist_llm_cache: 0.23