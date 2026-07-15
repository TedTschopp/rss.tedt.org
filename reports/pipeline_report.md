# Pipeline Report

- Timestamp: 2026-07-15T08:53:40.201252Z
- Sources configured: 43
- Raw items: 1657
- Stories: 1622
- Clusters: 1556
- LLM: {'status': 'ok', 'calls': 516, 'ok': 516, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 125, 'importance': 118, 'output_cleanup': 143}, 'stages': {'enrichment': {'status': 'ok', 'calls': 130, 'ok': 130, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 140, 'remaining': 0}, 'summaries': {'before': 128, 'remaining': 0}}}, 'publish': {'status': 'ok', 'calls': 386, 'ok': 386, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 125, 'importance': 118, 'output_cleanup': 143}, 'by_model': {'openai/gpt-4.1-mini': 386}, 'backlog': {'ai_relevance': {'before': 140, 'remaining': 15}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 158, 'remaining': 15}}, 'backlog_remaining': 30}}, 'backlog': {'embeddings': {'before': 140, 'remaining': 0}, 'summaries': {'before': 128, 'remaining': 0}, 'ai_relevance': {'before': 140, 'remaining': 15}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 158, 'remaining': 15}}, 'backlog_remaining': 30}

## LLM Calls
- Total: 516
- Enrichment: 130
- Publish: 386

## Enrichment Backlog
- Remaining: 30
- embeddings: 0
- summaries: 0
- ai_relevance: 15
- importance: 0
- output_cleanup: 15

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.90
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 130.86
- cluster: 0.36
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 425.43
- persist_llm_cache: 0.28