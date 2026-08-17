# Pipeline Report

- Timestamp: 2026-08-17T08:25:02.339496Z
- Sources configured: 43
- Raw items: 3184
- Stories: 2289
- Clusters: 2257
- LLM: {'status': 'ok', 'calls': 182, 'ok': 182, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 75, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 171, 'ok': 171, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 75, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 171}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 182
- Enrichment: 11
- Publish: 171

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.56
- normalize: 0.17
- dedupe: 0.09
- llm_enrich: 18.60
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.37
- publish: 653.30
- persist_llm_cache: 0.21