# Pipeline Report

- Timestamp: 2026-09-19T16:13:40.773933Z
- Sources configured: 43
- Raw items: 1991
- Stories: 1940
- Clusters: 1910
- LLM: {'status': 'degraded', 'calls': 145, 'ok': 144, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 52, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 134, 'ok': 133, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 52, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 134}, 'backlog': {'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 145
- Enrichment: 11
- Publish: 134

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.51
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 15.63
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 476.38
- persist_llm_cache: 0.17