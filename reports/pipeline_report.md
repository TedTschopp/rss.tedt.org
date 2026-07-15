# Pipeline Report

- Timestamp: 2026-07-15T07:19:23.609575Z
- Sources configured: 43
- Raw items: 1646
- Stories: 1616
- Clusters: 1556
- LLM: {'status': 'ok', 'calls': 950, 'ok': 950, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 197, 'output_cleanup': 250}, 'stages': {'enrichment': {'status': 'ok', 'calls': 253, 'ok': 253, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 445, 'remaining': 195}, 'summaries': {'before': 396, 'remaining': 146}}}, 'publish': {'status': 'ok', 'calls': 697, 'ok': 697, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 197, 'output_cleanup': 250}, 'by_model': {'openai/gpt-4.1-mini': 697}, 'backlog': {'ai_relevance': {'before': 633, 'remaining': 383}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 657, 'remaining': 407}}, 'backlog_remaining': 790}}, 'backlog': {'embeddings': {'before': 445, 'remaining': 195}, 'summaries': {'before': 396, 'remaining': 146}, 'ai_relevance': {'before': 633, 'remaining': 383}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 657, 'remaining': 407}}, 'backlog_remaining': 1131}

## LLM Calls
- Total: 950
- Enrichment: 253
- Publish: 697

## Enrichment Backlog
- Remaining: 1131
- embeddings: 195
- summaries: 146
- ai_relevance: 383
- importance: 0
- output_cleanup: 407

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.36
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 252.84
- cluster: 0.31
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 724.17
- persist_llm_cache: 0.25