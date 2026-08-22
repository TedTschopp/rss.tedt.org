# Pipeline Report

- Timestamp: 2026-08-22T03:56:36.698719Z
- Sources configured: 43
- Raw items: 1876
- Stories: 1838
- Clusters: 1808
- LLM: {'status': 'ok', 'calls': 189, 'ok': 189, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 89, 'importance': 29, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 36, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'ok', 'calls': 163, 'ok': 163, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 89, 'importance': 29, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 163}, 'backlog': {'ai_relevance': {'before': 89, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 36, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 89, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 17}

## LLM Calls
- Total: 189
- Enrichment: 26
- Publish: 163

## Enrichment Backlog
- Remaining: 17
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.35
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 31.78
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 492.31
- persist_llm_cache: 0.20