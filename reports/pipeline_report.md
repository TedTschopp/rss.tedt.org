# Pipeline Report

- Timestamp: 2026-11-14T11:02:33.556967Z
- Sources configured: 43
- Raw items: 2138
- Stories: 2098
- Clusters: 2070
- LLM: {'status': 'ok', 'calls': 216, 'ok': 216, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 85, 'importance': 59, 'output_cleanup': 46}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 190, 'ok': 190, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 85, 'importance': 59, 'output_cleanup': 46}, 'by_model': {'openai/gpt-4.1-mini': 190}, 'backlog': {'ai_relevance': {'before': 85, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 85, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 216
- Enrichment: 26
- Publish: 190

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.71
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 32.63
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 800.64
- persist_llm_cache: 0.27