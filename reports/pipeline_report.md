# Pipeline Report

- Timestamp: 2026-07-26T04:58:32.021642Z
- Sources configured: 43
- Raw items: 1746
- Stories: 1707
- Clusters: 1678
- LLM: {'status': 'degraded', 'calls': 200, 'ok': 196, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 93, 'importance': 32, 'output_cleanup': 49}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 38, 'remaining': 0}, 'summaries': {'before': 40, 'remaining': 15}}}, 'publish': {'status': 'degraded', 'calls': 174, 'ok': 170, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 93, 'importance': 32, 'output_cleanup': 49}, 'by_model': {'openai/gpt-4.1-mini': 174}, 'backlog': {'ai_relevance': {'before': 93, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 38, 'remaining': 0}, 'summaries': {'before': 40, 'remaining': 15}, 'ai_relevance': {'before': 93, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 19}

## LLM Calls
- Total: 200
- Enrichment: 26
- Publish: 174

## Enrichment Backlog
- Remaining: 19
- embeddings: 0
- summaries: 15
- ai_relevance: 1
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.74
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 32.45
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 946.37
- persist_llm_cache: 0.21