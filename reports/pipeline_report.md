# Pipeline Report

- Timestamp: 2026-09-29T03:56:07.956859Z
- Sources configured: 43
- Raw items: 1981
- Stories: 1940
- Clusters: 1911
- LLM: {'status': 'degraded', 'calls': 247, 'ok': 246, 'errors': 1, 'skipped': 0, 'by_kind': {'importance': 67, 'ai_relevance': 107, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 40, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'degraded', 'calls': 221, 'ok': 220, 'errors': 1, 'skipped': 0, 'by_kind': {'importance': 67, 'ai_relevance': 107, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 221}, 'backlog': {'ai_relevance': {'before': 107, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 40, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 107, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 247
- Enrichment: 26
- Publish: 221

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.38
- normalize: 0.03
- dedupe: 0.03
- llm_enrich: 30.29
- cluster: 0.16
- score: 0.01
- write_intermediate_outputs: 0.18
- publish: 585.54
- persist_llm_cache: 0.19