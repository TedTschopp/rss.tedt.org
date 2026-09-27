# Pipeline Report

- Timestamp: 2026-09-27T00:19:50.283532Z
- Sources configured: 43
- Raw items: 2047
- Stories: 2001
- Clusters: 1974
- LLM: {'status': 'degraded', 'calls': 117, 'ok': 116, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 55, 'importance': 31, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 106, 'ok': 105, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 55, 'importance': 31, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 106}, 'backlog': {'ai_relevance': {'before': 55, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 55, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 117
- Enrichment: 11
- Publish: 106

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.70
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 12.40
- cluster: 0.19
- score: 0.01
- write_intermediate_outputs: 0.25
- publish: 297.57
- persist_llm_cache: 0.21