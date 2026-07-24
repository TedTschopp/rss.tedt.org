# Pipeline Report

- Timestamp: 2026-07-24T09:01:57.052588Z
- Sources configured: 43
- Raw items: 3519
- Stories: 2352
- Clusters: 2324
- LLM: {'status': 'ok', 'calls': 179, 'ok': 179, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 73, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 168, 'ok': 168, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 73, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 168}, 'backlog': {'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 179
- Enrichment: 11
- Publish: 168

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.56
- normalize: 0.20
- dedupe: 0.10
- llm_enrich: 15.91
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.40
- publish: 637.24
- persist_llm_cache: 0.22