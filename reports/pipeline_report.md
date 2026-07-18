# Pipeline Report

- Timestamp: 2026-07-18T06:15:57.324689Z
- Sources configured: 43
- Raw items: 2072
- Stories: 2029
- Clusters: 1996
- LLM: {'status': 'ok', 'calls': 466, 'ok': 466, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 197, 'importance': 193, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 440, 'ok': 440, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 197, 'importance': 193, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 440}, 'backlog': {'ai_relevance': {'before': 197, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 197, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 466
- Enrichment: 26
- Publish: 440

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.40
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 44.14
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 1829.61
- persist_llm_cache: 0.18