# Pipeline Report

- Timestamp: 2026-08-06T05:06:46.420971Z
- Sources configured: 43
- Raw items: 3589
- Stories: 2662
- Clusters: 2635
- LLM: {'status': 'ok', 'calls': 463, 'ok': 463, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 195, 'importance': 192, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 437, 'ok': 437, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 195, 'importance': 192, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 437}, 'backlog': {'ai_relevance': {'before': 195, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 195, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 463
- Enrichment: 26
- Publish: 437

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.07
- normalize: 0.20
- dedupe: 0.09
- llm_enrich: 70.49
- cluster: 0.28
- score: 0.03
- write_intermediate_outputs: 0.42
- publish: 1733.41
- persist_llm_cache: 0.23