# Pipeline Report

- Timestamp: 2026-09-20T08:11:18.850243Z
- Sources configured: 43
- Raw items: 1962
- Stories: 1923
- Clusters: 1895
- LLM: {'status': 'degraded', 'calls': 83, 'ok': 81, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 19, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 72, 'ok': 70, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 33, 'importance': 19, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 72}, 'backlog': {'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 33, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 83
- Enrichment: 11
- Publish: 72

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.10
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 13.62
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 257.37
- persist_llm_cache: 0.20