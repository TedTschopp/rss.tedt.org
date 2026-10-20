# Pipeline Report

- Timestamp: 2026-10-20T03:52:26.249882Z
- Sources configured: 43
- Raw items: 2059
- Stories: 2016
- Clusters: 1983
- LLM: {'status': 'ok', 'calls': 166, 'ok': 166, 'errors': 0, 'skipped': 0, 'by_kind': {'importance': 34, 'ai_relevance': 58, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'ok', 'calls': 140, 'ok': 140, 'errors': 0, 'skipped': 0, 'by_kind': {'importance': 34, 'ai_relevance': 58, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 140}, 'backlog': {'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 166
- Enrichment: 26
- Publish: 140

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.14
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 29.63
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.18
- publish: 435.05
- persist_llm_cache: 0.23