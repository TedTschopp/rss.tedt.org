# Pipeline Report

- Timestamp: 2026-07-31T05:11:35.933776Z
- Sources configured: 43
- Raw items: 3411
- Stories: 2658
- Clusters: 2629
- LLM: {'status': 'ok', 'calls': 462, 'ok': 462, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 193, 'importance': 193, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 436, 'ok': 436, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 193, 'importance': 193, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 436}, 'backlog': {'ai_relevance': {'before': 193, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 193, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 462
- Enrichment: 26
- Publish: 436

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.14
- normalize: 0.20
- dedupe: 0.10
- llm_enrich: 52.97
- cluster: 0.28
- score: 0.03
- write_intermediate_outputs: 0.41
- publish: 1732.00
- persist_llm_cache: 0.23