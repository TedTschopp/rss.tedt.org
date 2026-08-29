# Pipeline Report

- Timestamp: 2026-08-29T08:19:48.639186Z
- Sources configured: 43
- Raw items: 1850
- Stories: 1828
- Clusters: 1801
- LLM: {'status': 'degraded', 'calls': 184, 'ok': 183, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 74, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 173, 'ok': 172, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 74, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 173}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 184
- Enrichment: 11
- Publish: 173

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 9.44
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 15.16
- cluster: 0.20
- score: 0.01
- write_intermediate_outputs: 0.20
- publish: 675.34
- persist_llm_cache: 0.17