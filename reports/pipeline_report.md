# Pipeline Report

- Timestamp: 2026-07-28T05:38:10.727299Z
- Sources configured: 43
- Raw items: 4309
- Stories: 2962
- Clusters: 2932
- LLM: {'status': 'degraded', 'calls': 470, 'ok': 467, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 196, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'degraded', 'calls': 444, 'ok': 441, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 196, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 444}, 'backlog': {'ai_relevance': {'before': 198, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 198, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 28}

## LLM Calls
- Total: 470
- Enrichment: 26
- Publish: 444

## Enrichment Backlog
- Remaining: 28
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 3.61
- normalize: 0.19
- dedupe: 0.09
- llm_enrich: 73.52
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.57
- publish: 3629.69
- persist_llm_cache: 0.18