---
id: synthesize
name: Research synthesis
version: 1.0.0
agent: researcher
inputs: [research_question, rag_results, web_results, github_results, community_results]
outputs: [research_report]
---

# Research synthesis

1. Restate the question and decision context.
2. Deduplicate claims and sources.
3. Separate verified facts, opinions, and inference.
4. Resolve conflicts by authority, recency, directness, and reproducibility.
5. Mark confidence and unanswered questions.
6. Render the configured Research Report template.

Quality gates: every material claim has a citation; community evidence is labeled anecdotal; stale RAG content is checked against TTL; event dates are preferred over publication dates.
