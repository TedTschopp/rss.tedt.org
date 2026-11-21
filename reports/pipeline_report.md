# Pipeline Report

- Timestamp: 2026-11-21T06:10:33.423885Z
- Sources configured: 43
- Raw items: 2578
- Stories: 2547
- Clusters: 2519
- LLM: {'status': 'degraded', 'calls': 188, 'ok': 186, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 77, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 177, 'ok': 175, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 77, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 177}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 188
- Enrichment: 11
- Publish: 177

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.09
- normalize: 0.11
- dedupe: 0.08
- llm_enrich: 14.27
- cluster: 0.24
- score: 0.03
- write_intermediate_outputs: 0.33
- publish: 622.87
- persist_llm_cache: 0.27