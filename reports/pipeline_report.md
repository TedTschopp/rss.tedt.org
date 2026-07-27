# Pipeline Report

- Timestamp: 2026-07-27T05:23:10.618894Z
- Sources configured: 43
- Raw items: 2715
- Stories: 2139
- Clusters: 2111
- LLM: {'status': 'ok', 'calls': 472, 'ok': 472, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 199, 'importance': 197, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 446, 'ok': 446, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 199, 'importance': 197, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 446}, 'backlog': {'ai_relevance': {'before': 199, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 199, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 472
- Enrichment: 26
- Publish: 446

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.59
- normalize: 0.13
- dedupe: 0.08
- llm_enrich: 61.71
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.32
- publish: 2117.24
- persist_llm_cache: 0.24