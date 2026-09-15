# Pipeline Report

- Timestamp: 2026-09-15T00:21:36.864366Z
- Sources configured: 43
- Raw items: 2020
- Stories: 1963
- Clusters: 1933
- LLM: {'status': 'degraded', 'calls': 163, 'ok': 161, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 57, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 152, 'ok': 150, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 57, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 152}, 'backlog': {'ai_relevance': {'before': 75, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 75, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 163
- Enrichment: 11
- Publish: 152

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 9
- ai_relevance: 1
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.68
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 17.80
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.17
- publish: 511.90
- persist_llm_cache: 0.16