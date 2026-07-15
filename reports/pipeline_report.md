# Pipeline Report

- Timestamp: 2026-07-15T09:11:54.017970Z
- Sources configured: 43
- Raw items: 1584
- Stories: 1547
- Clusters: 1482
- LLM: {'status': 'ok', 'calls': 270, 'ok': 270, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 60, 'output_cleanup': 77}, 'stages': {'enrichment': {'status': 'ok', 'calls': 66, 'ok': 66, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 69, 'remaining': 0}, 'summaries': {'before': 65, 'remaining': 0}}}, 'publish': {'status': 'ok', 'calls': 204, 'ok': 204, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 67, 'importance': 60, 'output_cleanup': 77}, 'by_model': {'openai/gpt-4.1-mini': 204}, 'backlog': {'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 77, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 69, 'remaining': 0}, 'summaries': {'before': 65, 'remaining': 0}, 'ai_relevance': {'before': 67, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 77, 'remaining': 0}}, 'backlog_remaining': 0}

## LLM Calls
- Total: 270
- Enrichment: 66
- Publish: 204

## Enrichment Backlog
- Remaining: 0
- embeddings: 0
- summaries: 0
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.30
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 68.61
- cluster: 0.31
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 234.39
- persist_llm_cache: 0.25