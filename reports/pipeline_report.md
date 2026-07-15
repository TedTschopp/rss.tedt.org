# Pipeline Report

- Timestamp: 2026-07-15T08:41:46.808964Z
- Sources configured: 43
- Raw items: 1628
- Stories: 1593
- Clusters: 1529
- LLM: {'status': 'ok', 'calls': 309, 'ok': 309, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 66, 'output_cleanup': 83}, 'stages': {'enrichment': {'status': 'ok', 'calls': 88, 'ok': 88, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 93, 'remaining': 0}, 'summaries': {'before': 87, 'remaining': 0}}}, 'publish': {'status': 'ok', 'calls': 221, 'ok': 221, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 66, 'output_cleanup': 83}, 'by_model': {'openai/gpt-4.1-mini': 221}, 'backlog': {'ai_relevance': {'before': 87, 'remaining': 15}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 98, 'remaining': 15}}, 'backlog_remaining': 30}}, 'backlog': {'embeddings': {'before': 93, 'remaining': 0}, 'summaries': {'before': 87, 'remaining': 0}, 'ai_relevance': {'before': 87, 'remaining': 15}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 98, 'remaining': 15}}, 'backlog_remaining': 30}

## LLM Calls
- Total: 309
- Enrichment: 88
- Publish: 221

## Enrichment Backlog
- Remaining: 30
- embeddings: 0
- summaries: 0
- ai_relevance: 15
- importance: 0
- output_cleanup: 15

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.26
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 88.75
- cluster: 0.37
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 252.62
- persist_llm_cache: 0.27