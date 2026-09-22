# Pipeline Report

- Timestamp: 2026-09-22T04:00:36.144201Z
- Sources configured: 43
- Raw items: 3053
- Stories: 2409
- Clusters: 2381
- LLM: {'status': 'ok', 'calls': 396, 'ok': 396, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 164, 'importance': 161, 'output_cleanup': 45}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'ok', 'calls': 370, 'ok': 370, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 164, 'importance': 161, 'output_cleanup': 45}, 'by_model': {'openai/gpt-4.1-mini': 370}, 'backlog': {'ai_relevance': {'before': 164, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 164, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 45, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 396
- Enrichment: 26
- Publish: 370

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.94
- normalize: 0.15
- dedupe: 0.08
- llm_enrich: 30.74
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.36
- publish: 1047.24
- persist_llm_cache: 0.22