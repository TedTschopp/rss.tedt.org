# Pipeline Report

- Timestamp: 2026-10-02T00:21:00.898763Z
- Sources configured: 43
- Raw items: 2072
- Stories: 2016
- Clusters: 1989
- LLM: {'status': 'degraded', 'calls': 147, 'ok': 145, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 49, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 136, 'ok': 134, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 49, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 136}, 'backlog': {'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 147
- Enrichment: 11
- Publish: 136

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.60
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 17.70
- cluster: 0.15
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 417.26
- persist_llm_cache: 0.18