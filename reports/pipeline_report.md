# Pipeline Report

- Timestamp: 2026-10-19T08:20:36.478561Z
- Sources configured: 43
- Raw items: 3786
- Stories: 2775
- Clusters: 2745
- LLM: {'status': 'degraded', 'calls': 186, 'ok': 185, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 77, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 175, 'ok': 174, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 77, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 175}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 186
- Enrichment: 11
- Publish: 175

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.30
- normalize: 0.21
- dedupe: 0.11
- llm_enrich: 15.02
- cluster: 0.33
- score: 0.03
- write_intermediate_outputs: 0.43
- publish: 533.04
- persist_llm_cache: 0.23