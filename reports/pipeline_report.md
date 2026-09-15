# Pipeline Report

- Timestamp: 2026-09-15T08:17:09.375363Z
- Sources configured: 43
- Raw items: 5225
- Stories: 3038
- Clusters: 3007
- LLM: {'status': 'ok', 'calls': 183, 'ok': 183, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 76, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 172, 'ok': 172, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 76, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 172}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 183
- Enrichment: 11
- Publish: 172

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.17
- normalize: 0.31
- dedupe: 0.14
- llm_enrich: 18.98
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.55
- publish: 589.96
- persist_llm_cache: 0.23