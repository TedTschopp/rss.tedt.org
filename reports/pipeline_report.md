# Pipeline Report

- Timestamp: 2026-10-21T04:06:29.792570Z
- Sources configured: 43
- Raw items: 5615
- Stories: 3524
- Clusters: 3495
- LLM: {'status': 'ok', 'calls': 411, 'ok': 411, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 174, 'importance': 169, 'output_cleanup': 42}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'ok', 'calls': 385, 'ok': 385, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 174, 'importance': 169, 'output_cleanup': 42}, 'by_model': {'openai/gpt-4.1-mini': 385}, 'backlog': {'ai_relevance': {'before': 174, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 174, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 411
- Enrichment: 26
- Publish: 385

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.39
- normalize: 0.34
- dedupe: 0.16
- llm_enrich: 29.22
- cluster: 0.30
- score: 0.03
- write_intermediate_outputs: 0.62
- publish: 1278.67
- persist_llm_cache: 0.24