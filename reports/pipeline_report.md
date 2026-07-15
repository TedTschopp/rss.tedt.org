# Pipeline Report

- Timestamp: 2026-07-15T06:21:54.232077Z
- Sources configured: 43
- Raw items: 1581
- Stories: 1552
- Clusters: 1511
- LLM: {'status': 'ok', 'calls': 835, 'ok': 835, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 82, 'output_cleanup': 250}, 'stages': {'enrichment': {'status': 'ok', 'calls': 253, 'ok': 253, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 914, 'remaining': 664}, 'summaries': {'before': 875, 'remaining': 625}}}, 'publish': {'status': 'ok', 'calls': 582, 'ok': 582, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 82, 'output_cleanup': 250}, 'by_model': {'openai/gpt-4.1-mini': 582}, 'backlog': {'ai_relevance': {'before': 1072, 'remaining': 822}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 1118, 'remaining': 868}}, 'backlog_remaining': 1690}}, 'backlog': {'embeddings': {'before': 914, 'remaining': 664}, 'summaries': {'before': 875, 'remaining': 625}, 'ai_relevance': {'before': 1072, 'remaining': 822}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 1118, 'remaining': 868}}, 'backlog_remaining': 2979}

## LLM Calls
- Total: 835
- Enrichment: 253
- Publish: 582

## Enrichment Backlog
- Remaining: 2979
- embeddings: 664
- summaries: 625
- ai_relevance: 822
- importance: 0
- output_cleanup: 868

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.37
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 253.40
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 667.46
- persist_llm_cache: 0.17