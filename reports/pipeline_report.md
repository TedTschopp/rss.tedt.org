# Pipeline Report

- Timestamp: 2026-09-13T08:10:43.830645Z
- Sources configured: 43
- Raw items: 1950
- Stories: 1905
- Clusters: 1872
- LLM: {'status': 'ok', 'calls': 123, 'ok': 123, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 56, 'importance': 37, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 18, 'remaining': 0}, 'summaries': {'before': 18, 'remaining': 8}}}, 'publish': {'status': 'ok', 'calls': 112, 'ok': 112, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 56, 'importance': 37, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 112}, 'backlog': {'ai_relevance': {'before': 56, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 18, 'remaining': 0}, 'summaries': {'before': 18, 'remaining': 8}, 'ai_relevance': {'before': 56, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 8}

## LLM Calls
- Total: 123
- Enrichment: 11
- Publish: 112

## Enrichment Backlog
- Remaining: 8
- embeddings: 0
- summaries: 8
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.28
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 13.63
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.21
- publish: 213.50
- persist_llm_cache: 0.19