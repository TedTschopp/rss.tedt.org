# Pipeline Report

- Timestamp: 2026-09-16T04:01:11.853798Z
- Sources configured: 43
- Raw items: 4631
- Stories: 3077
- Clusters: 3046
- LLM: {'status': 'ok', 'calls': 414, 'ok': 414, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 171, 'importance': 171, 'output_cleanup': 46}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'ok', 'calls': 388, 'ok': 388, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 171, 'importance': 171, 'output_cleanup': 46}, 'by_model': {'openai/gpt-4.1-mini': 388}, 'backlog': {'ai_relevance': {'before': 171, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 171, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 414
- Enrichment: 26
- Publish: 388

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.21
- normalize: 0.27
- dedupe: 0.12
- llm_enrich: 30.14
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.51
- publish: 1091.42
- persist_llm_cache: 0.22