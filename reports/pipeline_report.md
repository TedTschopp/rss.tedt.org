# Pipeline Report

- Timestamp: 2026-10-20T16:14:57.572974Z
- Sources configured: 43
- Raw items: 2162
- Stories: 2104
- Clusters: 2073
- LLM: {'status': 'degraded', 'calls': 139, 'ok': 138, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 50, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 128, 'ok': 127, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 50, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 128}, 'backlog': {'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 139
- Enrichment: 11
- Publish: 128

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.50
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 17.06
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 495.87
- persist_llm_cache: 0.22