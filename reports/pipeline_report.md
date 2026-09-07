# Pipeline Report

- Timestamp: 2026-09-07T08:19:41.144510Z
- Sources configured: 43
- Raw items: 3422
- Stories: 2395
- Clusters: 2366
- LLM: {'status': 'ok', 'calls': 183, 'ok': 183, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 75, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 172, 'ok': 172, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 75, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 172}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 183
- Enrichment: 11
- Publish: 172

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.05
- normalize: 0.18
- dedupe: 0.09
- llm_enrich: 17.78
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.38
- publish: 674.72
- persist_llm_cache: 0.22