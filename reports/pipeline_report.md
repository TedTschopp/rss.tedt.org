# Pipeline Report

- Timestamp: 2026-09-14T03:55:47.533181Z
- Sources configured: 43
- Raw items: 1994
- Stories: 1941
- Clusters: 1908
- LLM: {'status': 'ok', 'calls': 258, 'ok': 258, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 102, 'importance': 82, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'ok', 'calls': 232, 'ok': 232, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 102, 'importance': 82, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 232}, 'backlog': {'ai_relevance': {'before': 102, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 102, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 258
- Enrichment: 26
- Publish: 232

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.96
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 28.56
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 637.03
- persist_llm_cache: 0.23