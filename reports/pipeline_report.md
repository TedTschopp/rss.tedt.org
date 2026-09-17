# Pipeline Report

- Timestamp: 2026-09-17T16:14:44.595553Z
- Sources configured: 43
- Raw items: 2689
- Stories: 2637
- Clusters: 2606
- LLM: {'status': 'degraded', 'calls': 158, 'ok': 157, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 60, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 147, 'ok': 146, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 60, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 147}, 'backlog': {'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 158
- Enrichment: 11
- Publish: 147

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.82
- normalize: 0.12
- dedupe: 0.08
- llm_enrich: 18.54
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.34
- publish: 418.64
- persist_llm_cache: 0.22