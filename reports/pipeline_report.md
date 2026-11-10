# Pipeline Report

- Timestamp: 2026-11-10T06:30:50.003266Z
- Sources configured: 43
- Raw items: 2668
- Stories: 2608
- Clusters: 2580
- LLM: {'status': 'degraded', 'calls': 189, 'ok': 186, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 78, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 178, 'ok': 175, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 78, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 178}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 189
- Enrichment: 11
- Publish: 178

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.38
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 12.23
- cluster: 0.15
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 534.22
- persist_llm_cache: 0.22