# Pipeline Report

- Timestamp: 2026-10-23T04:17:23.228779Z
- Sources configured: 43
- Raw items: 3740
- Stories: 2714
- Clusters: 2683
- LLM: {'status': 'degraded', 'calls': 410, 'ok': 409, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 169, 'importance': 168, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}}}, 'publish': {'status': 'degraded', 'calls': 384, 'ok': 383, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 169, 'importance': 168, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 384}, 'backlog': {'ai_relevance': {'before': 169, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 19}, 'ai_relevance': {'before': 169, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 410
- Enrichment: 26
- Publish: 384

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 19
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.16
- normalize: 0.20
- dedupe: 0.10
- llm_enrich: 31.00
- cluster: 0.28
- score: 0.03
- write_intermediate_outputs: 0.42
- publish: 1871.03
- persist_llm_cache: 0.25