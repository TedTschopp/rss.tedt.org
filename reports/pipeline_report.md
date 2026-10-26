# Pipeline Report

- Timestamp: 2026-10-26T08:24:10.163693Z
- Sources configured: 43
- Raw items: 3856
- Stories: 2676
- Clusters: 2647
- LLM: {'status': 'degraded', 'calls': 186, 'ok': 185, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 76, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 175, 'ok': 174, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 76, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 175}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 186
- Enrichment: 11
- Publish: 175

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.18
- normalize: 0.15
- dedupe: 0.08
- llm_enrich: 15.38
- cluster: 0.23
- score: 0.03
- write_intermediate_outputs: 0.44
- publish: 624.23
- persist_llm_cache: 0.25