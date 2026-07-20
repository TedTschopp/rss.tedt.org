# Pipeline Report

- Timestamp: 2026-07-20T02:09:38.695090Z
- Sources configured: 43
- Raw items: 1806
- Stories: 1761
- Clusters: 1732
- LLM: {'status': 'ok', 'calls': 99, 'ok': 99, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 25, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 88, 'ok': 88, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 25, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 88}, 'backlog': {'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 99
- Enrichment: 11
- Publish: 88

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 6.00
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 19.87
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 353.98
- persist_llm_cache: 0.21