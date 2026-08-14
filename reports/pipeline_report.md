# Pipeline Report

- Timestamp: 2026-08-14T00:26:06.663490Z
- Sources configured: 43
- Raw items: 1971
- Stories: 1918
- Clusters: 1888
- LLM: {'status': 'degraded', 'calls': 139, 'ok': 137, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 46, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 128, 'ok': 126, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 46, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 128}, 'backlog': {'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 5, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 5, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 139
- Enrichment: 11
- Publish: 128

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.56
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 14.00
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 488.15
- persist_llm_cache: 0.20