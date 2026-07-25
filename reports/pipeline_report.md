# Pipeline Report

- Timestamp: 2026-07-25T05:06:45.106806Z
- Sources configured: 43
- Raw items: 1933
- Stories: 1887
- Clusters: 1858
- LLM: {'status': 'degraded', 'calls': 410, 'ok': 409, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 170, 'importance': 164, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'degraded', 'calls': 384, 'ok': 383, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 170, 'importance': 164, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 384}, 'backlog': {'ai_relevance': {'before': 170, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 170, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 26}

## LLM Calls
- Total: 410
- Enrichment: 26
- Publish: 384

## Enrichment Backlog
- Remaining: 26
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.94
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 53.22
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 1740.03
- persist_llm_cache: 0.22