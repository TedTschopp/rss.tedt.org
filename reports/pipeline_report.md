# Pipeline Report

- Timestamp: 2026-09-06T03:52:12.544733Z
- Sources configured: 43
- Raw items: 1947
- Stories: 1909
- Clusters: 1878
- LLM: {'status': 'ok', 'calls': 237, 'ok': 237, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 118, 'importance': 43, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 39, 'remaining': 14}}}, 'publish': {'status': 'ok', 'calls': 211, 'ok': 211, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 118, 'importance': 43, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 211}, 'backlog': {'ai_relevance': {'before': 118, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 39, 'remaining': 14}, 'ai_relevance': {'before': 118, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 237
- Enrichment: 26
- Publish: 211

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 14
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.02
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 28.78
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 617.45
- persist_llm_cache: 0.21