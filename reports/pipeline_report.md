# Pipeline Report

- Timestamp: 2026-07-23T16:48:52.139683Z
- Sources configured: 43
- Raw items: 1949
- Stories: 1896
- Clusters: 1867
- LLM: {'status': 'degraded', 'calls': 152, 'ok': 148, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 55, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 141, 'ok': 137, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 55, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 141}, 'backlog': {'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 152
- Enrichment: 11
- Publish: 141

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.04
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 23.68
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 1015.08
- persist_llm_cache: 0.21