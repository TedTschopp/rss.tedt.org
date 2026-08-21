# Pipeline Report

- Timestamp: 2026-08-21T08:25:10.218995Z
- Sources configured: 43
- Raw items: 3090
- Stories: 2524
- Clusters: 2495
- LLM: {'status': 'degraded', 'calls': 180, 'ok': 179, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 72, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 169, 'ok': 168, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 72, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 169}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 180
- Enrichment: 11
- Publish: 169

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.72
- normalize: 0.16
- dedupe: 0.09
- llm_enrich: 18.21
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.38
- publish: 724.49
- persist_llm_cache: 0.23