# Pipeline Report

- Timestamp: 2026-08-10T04:50:29.230011Z
- Sources configured: 43
- Raw items: 3320
- Stories: 2340
- Clusters: 2310
- LLM: {'status': 'ok', 'calls': 472, 'ok': 472, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 199, 'importance': 197, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 446, 'ok': 446, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 199, 'importance': 197, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 446}, 'backlog': {'ai_relevance': {'before': 199, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 199, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 472
- Enrichment: 26
- Publish: 446

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.68
- normalize: 0.18
- dedupe: 0.09
- llm_enrich: 78.94
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.38
- publish: 2300.35
- persist_llm_cache: 0.23