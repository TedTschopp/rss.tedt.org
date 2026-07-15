# Pipeline Report

- Timestamp: 2026-07-15T08:27:07.860746Z
- Sources configured: 43
- Raw items: 1671
- Stories: 1633
- Clusters: 1567
- LLM: {'status': 'degraded', 'calls': 518, 'ok': 517, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 129, 'importance': 124, 'output_cleanup': 139}, 'stages': {'enrichment': {'status': 'ok', 'calls': 126, 'ok': 126, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 129, 'remaining': 0}, 'summaries': {'before': 124, 'remaining': 0}}}, 'publish': {'status': 'degraded', 'calls': 392, 'ok': 391, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 129, 'importance': 124, 'output_cleanup': 139}, 'by_model': {'openai/gpt-4.1-mini': 392}, 'backlog': {'ai_relevance': {'before': 146, 'remaining': 17}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 156, 'remaining': 17}}, 'backlog_remaining': 35}}, 'backlog': {'embeddings': {'before': 129, 'remaining': 0}, 'summaries': {'before': 124, 'remaining': 0}, 'ai_relevance': {'before': 146, 'remaining': 17}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 156, 'remaining': 17}}, 'backlog_remaining': 35}

## LLM Calls
- Total: 518
- Enrichment: 126
- Publish: 392

## Enrichment Backlog
- Remaining: 35
- embeddings: 0
- summaries: 0
- ai_relevance: 17
- importance: 1
- output_cleanup: 17

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.03
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 127.58
- cluster: 0.40
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 474.98
- persist_llm_cache: 0.29