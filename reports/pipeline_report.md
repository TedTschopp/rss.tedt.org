# Pipeline Report

- Timestamp: 2026-10-27T08:18:06.993029Z
- Sources configured: 43
- Raw items: 5124
- Stories: 3898
- Clusters: 3872
- LLM: {'status': 'degraded', 'calls': 183, 'ok': 181, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 76, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 172, 'ok': 170, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 76, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 172}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 183
- Enrichment: 11
- Publish: 172

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 43.67
- normalize: 0.17
- dedupe: 0.08
- llm_enrich: 13.09
- cluster: 0.19
- score: 0.03
- write_intermediate_outputs: 0.50
- publish: 585.88
- persist_llm_cache: 0.25