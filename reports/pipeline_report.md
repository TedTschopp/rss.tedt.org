# Pipeline Report

- Timestamp: 2026-11-02T11:58:45.395937Z
- Sources configured: 43
- Raw items: 3540
- Stories: 2712
- Clusters: 2682
- LLM: {'status': 'ok', 'calls': 469, 'ok': 469, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 195, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 443, 'ok': 443, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 198, 'importance': 195, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 443}, 'backlog': {'ai_relevance': {'before': 198, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 198, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 469
- Enrichment: 26
- Publish: 443

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.53
- normalize: 0.13
- dedupe: 0.08
- llm_enrich: 31.90
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.41
- publish: 1381.04
- persist_llm_cache: 0.20