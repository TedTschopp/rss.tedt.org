# Pipeline Report

- Timestamp: 2026-07-15T06:03:50.231397Z
- Sources configured: 43
- Raw items: 1731
- Stories: 1694
- Clusters: 1656
- LLM: {'status': 'degraded', 'calls': 841, 'ok': 840, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 88, 'output_cleanup': 250}, 'stages': {'enrichment': {'status': 'ok', 'calls': 253, 'ok': 253, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 1218, 'remaining': 968}, 'summaries': {'before': 1183, 'remaining': 933}}}, 'publish': {'status': 'degraded', 'calls': 588, 'ok': 587, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 88, 'output_cleanup': 250}, 'by_model': {'openai/gpt-4.1-mini': 588}, 'backlog': {'ai_relevance': {'before': 1174, 'remaining': 925}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 1274, 'remaining': 1024}}, 'backlog_remaining': 1949}}, 'backlog': {'embeddings': {'before': 1218, 'remaining': 968}, 'summaries': {'before': 1183, 'remaining': 933}, 'ai_relevance': {'before': 1174, 'remaining': 925}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 1274, 'remaining': 1024}}, 'backlog_remaining': 3850}

## LLM Calls
- Total: 841
- Enrichment: 253
- Publish: 588

## Enrichment Backlog
- Remaining: 3850
- embeddings: 968
- summaries: 933
- ai_relevance: 925
- importance: 0
- output_cleanup: 1024

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.04
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 253.77
- cluster: 0.16
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 717.24
- persist_llm_cache: 0.15