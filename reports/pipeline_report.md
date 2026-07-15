# Pipeline Report

- Timestamp: 2026-07-15T07:00:22.661997Z
- Sources configured: 43
- Raw items: 1691
- Stories: 1661
- Clusters: 1605
- LLM: {'status': 'ok', 'calls': 970, 'ok': 970, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 217, 'output_cleanup': 250}, 'stages': {'enrichment': {'status': 'ok', 'calls': 253, 'ok': 253, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 592, 'remaining': 342}, 'summaries': {'before': 548, 'remaining': 298}}}, 'publish': {'status': 'ok', 'calls': 717, 'ok': 717, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 217, 'output_cleanup': 250}, 'by_model': {'openai/gpt-4.1-mini': 717}, 'backlog': {'ai_relevance': {'before': 784, 'remaining': 534}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 810, 'remaining': 560}}, 'backlog_remaining': 1094}}, 'backlog': {'embeddings': {'before': 592, 'remaining': 342}, 'summaries': {'before': 548, 'remaining': 298}, 'ai_relevance': {'before': 784, 'remaining': 534}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 810, 'remaining': 560}}, 'backlog_remaining': 1734}

## LLM Calls
- Total: 970
- Enrichment: 253
- Publish: 717

## Enrichment Backlog
- Remaining: 1734
- embeddings: 342
- summaries: 298
- ai_relevance: 534
- importance: 0
- output_cleanup: 560

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.87
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 253.38
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 736.86
- persist_llm_cache: 0.23