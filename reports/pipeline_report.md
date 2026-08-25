# Pipeline Report

- Timestamp: 2026-08-25T04:24:06.183647Z
- Sources configured: 43
- Raw items: 2984
- Stories: 2318
- Clusters: 2290
- LLM: {'status': 'ok', 'calls': 427, 'ok': 427, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 179, 'importance': 178, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'ok', 'calls': 401, 'ok': 401, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 179, 'importance': 178, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 401}, 'backlog': {'ai_relevance': {'before': 179, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 39, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 179, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 427
- Enrichment: 26
- Publish: 401

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.83
- normalize: 0.13
- dedupe: 0.07
- llm_enrich: 46.13
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.39
- publish: 2015.05
- persist_llm_cache: 0.21