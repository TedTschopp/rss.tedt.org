# Pipeline Report

- Timestamp: 2026-10-07T04:02:02.447752Z
- Sources configured: 43
- Raw items: 5934
- Stories: 3665
- Clusters: 3635
- LLM: {'status': 'ok', 'calls': 384, 'ok': 384, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 159, 'importance': 155, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'ok', 'calls': 358, 'ok': 358, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 159, 'importance': 155, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 358}, 'backlog': {'ai_relevance': {'before': 159, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 159, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 17}

## LLM Calls
- Total: 384
- Enrichment: 26
- Publish: 358

## Enrichment Backlog
- Remaining: 17
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.38
- normalize: 0.36
- dedupe: 0.15
- llm_enrich: 31.04
- cluster: 0.31
- score: 0.03
- write_intermediate_outputs: 0.65
- publish: 755.50
- persist_llm_cache: 0.25