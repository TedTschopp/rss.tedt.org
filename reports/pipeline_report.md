# Pipeline Report

- Timestamp: 2026-10-22T04:06:38.452643Z
- Sources configured: 43
- Raw items: 4031
- Stories: 2857
- Clusters: 2831
- LLM: {'status': 'ok', 'calls': 396, 'ok': 396, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 165, 'importance': 163, 'output_cleanup': 42}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 38, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'ok', 'calls': 370, 'ok': 370, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 165, 'importance': 163, 'output_cleanup': 42}, 'by_model': {'openai/gpt-4.1-mini': 370}, 'backlog': {'ai_relevance': {'before': 165, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 38, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 165, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 42, 'remaining': 0}}, 'backlog_remaining': 17}

## LLM Calls
- Total: 396
- Enrichment: 26
- Publish: 370

## Enrichment Backlog
- Remaining: 17
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 35.19
- normalize: 0.12
- dedupe: 0.06
- llm_enrich: 36.82
- cluster: 0.18
- score: 0.02
- write_intermediate_outputs: 0.36
- publish: 1219.41
- persist_llm_cache: 0.20