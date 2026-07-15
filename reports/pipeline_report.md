# Pipeline Report

- Timestamp: 2026-07-15T05:44:47.532136Z
- Sources configured: 43
- Raw items: 1661
- Stories: 1632
- Clusters: 1606
- LLM: {'status': 'degraded', 'calls': 929, 'ok': 928, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 176, 'output_cleanup': 250}, 'stages': {'enrichment': {'status': 'ok', 'calls': 253, 'ok': 253, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 1398, 'remaining': 1148}, 'summaries': {'before': 1369, 'remaining': 1119}}}, 'publish': {'status': 'degraded', 'calls': 676, 'ok': 675, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 176, 'output_cleanup': 250}, 'by_model': {'openai/gpt-4.1-mini': 676}, 'backlog': {'ai_relevance': {'before': 1214, 'remaining': 964}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 1295, 'remaining': 1045}}, 'backlog_remaining': 2010}}, 'backlog': {'embeddings': {'before': 1398, 'remaining': 1148}, 'summaries': {'before': 1369, 'remaining': 1119}, 'ai_relevance': {'before': 1214, 'remaining': 964}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 1295, 'remaining': 1045}}, 'backlog_remaining': 4277}

## LLM Calls
- Total: 929
- Enrichment: 253
- Publish: 676

## Enrichment Backlog
- Remaining: 4277
- embeddings: 1148
- summaries: 1119
- ai_relevance: 964
- importance: 1
- output_cleanup: 1045

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.99
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 254.10
- cluster: 0.12
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 717.79
- persist_llm_cache: 0.14