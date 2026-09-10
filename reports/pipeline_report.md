# Pipeline Report

- Timestamp: 2026-09-10T00:16:52.825124Z
- Sources configured: 43
- Raw items: 1930
- Stories: 1876
- Clusters: 1846
- LLM: {'status': 'ok', 'calls': 145, 'ok': 145, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 134, 'ok': 134, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 134}, 'backlog': {'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 145
- Enrichment: 11
- Publish: 134

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.11
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 13.89
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 293.84
- persist_llm_cache: 0.20