# Pipeline Report

- Timestamp: 2026-09-03T05:30:16.294552Z
- Sources configured: 43
- Raw items: 3547
- Stories: 2454
- Clusters: 2427
- LLM: {'status': 'ok', 'calls': 468, 'ok': 468, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 196, 'importance': 196, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 442, 'ok': 442, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 196, 'importance': 196, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 442}, 'backlog': {'ai_relevance': {'before': 196, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 196, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 468
- Enrichment: 26
- Publish: 442

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.40
- normalize: 0.20
- dedupe: 0.09
- llm_enrich: 61.63
- cluster: 0.27
- score: 0.03
- write_intermediate_outputs: 0.39
- publish: 1708.26
- persist_llm_cache: 0.22