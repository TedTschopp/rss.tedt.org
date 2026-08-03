# Pipeline Report

- Timestamp: 2026-08-03T16:58:51.631315Z
- Sources configured: 43
- Raw items: 2016
- Stories: 1968
- Clusters: 1939
- LLM: {'status': 'degraded', 'calls': 157, 'ok': 155, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 53, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 146, 'ok': 144, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 53, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 146}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 157
- Enrichment: 11
- Publish: 146

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 3.05
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 20.78
- cluster: 0.16
- score: 0.01
- write_intermediate_outputs: 0.18
- publish: 609.56
- persist_llm_cache: 0.12