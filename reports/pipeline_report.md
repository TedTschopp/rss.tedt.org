# Pipeline Report

- Timestamp: 2026-07-20T07:12:59.131310Z
- Sources configured: 43
- Raw items: 2831
- Stories: 2111
- Clusters: 2082
- LLM: {'status': 'ok', 'calls': 470, 'ok': 470, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 200, 'importance': 194, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 444, 'ok': 444, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 200, 'importance': 194, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 444}, 'backlog': {'ai_relevance': {'before': 200, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 200, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 470
- Enrichment: 26
- Publish: 444

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.08
- normalize: 0.15
- dedupe: 0.07
- llm_enrich: 46.50
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.33
- publish: 2218.78
- persist_llm_cache: 0.22