# Pipeline Report

- Timestamp: 2026-11-25T13:58:23.541168Z
- Sources configured: 43
- Raw items: 3979
- Stories: 2917
- Clusters: 2888
- LLM: {'status': 'ok', 'calls': 469, 'ok': 469, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 199, 'importance': 194, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 443, 'ok': 443, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 199, 'importance': 194, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 443}, 'backlog': {'ai_relevance': {'before': 199, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 199, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 469
- Enrichment: 26
- Publish: 443

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.74
- normalize: 0.12
- dedupe: 0.07
- llm_enrich: 32.64
- cluster: 0.16
- score: 0.02
- write_intermediate_outputs: 0.33
- publish: 2114.62
- persist_llm_cache: 0.24