# Pipeline Report

- Timestamp: 2026-08-18T08:23:09.310213Z
- Sources configured: 43
- Raw items: 5043
- Stories: 3150
- Clusters: 3121
- LLM: {'status': 'ok', 'calls': 174, 'ok': 174, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 71, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 163, 'ok': 163, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 71, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 163}, 'backlog': {'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 72, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 174
- Enrichment: 11
- Publish: 163

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.78
- normalize: 0.31
- dedupe: 0.14
- llm_enrich: 21.42
- cluster: 0.27
- score: 0.03
- write_intermediate_outputs: 0.56
- publish: 765.63
- persist_llm_cache: 0.22