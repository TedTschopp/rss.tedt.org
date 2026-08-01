# Pipeline Report

- Timestamp: 2026-08-01T04:51:18.020760Z
- Sources configured: 43
- Raw items: 1880
- Stories: 1847
- Clusters: 1817
- LLM: {'status': 'ok', 'calls': 201, 'ok': 201, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 49, 'output_cleanup': 46}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 47, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}}}, 'publish': {'status': 'ok', 'calls': 175, 'ok': 175, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 49, 'output_cleanup': 46}, 'by_model': {'openai/gpt-4.1-mini': 175}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 47, 'remaining': 0}, 'summaries': {'before': 49, 'remaining': 24}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 24}

## LLM Calls
- Total: 201
- Enrichment: 26
- Publish: 175

## Enrichment Backlog
- Remaining: 24
- embeddings: 0
- summaries: 24
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.17
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 33.00
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 625.27
- persist_llm_cache: 0.22