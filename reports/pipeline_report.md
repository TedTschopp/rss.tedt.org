# Pipeline Report

- Timestamp: 2026-08-05T05:10:28.038199Z
- Sources configured: 43
- Raw items: 4229
- Stories: 3237
- Clusters: 3210
- LLM: {'status': 'ok', 'calls': 467, 'ok': 467, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 196, 'importance': 195, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 441, 'ok': 441, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 196, 'importance': 195, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 441}, 'backlog': {'ai_relevance': {'before': 196, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 196, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 467
- Enrichment: 26
- Publish: 441

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 3.01
- normalize: 0.14
- dedupe: 0.07
- llm_enrich: 62.67
- cluster: 0.17
- score: 0.02
- write_intermediate_outputs: 0.31
- publish: 1964.51
- persist_llm_cache: 0.14