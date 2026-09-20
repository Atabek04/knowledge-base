---
aliases: [4k context window limit, why prompt engineering was not enough]
created: 2026-09-20
---

ChatGPT launched in November 2022 on a model with a 4,096-token context window: roughly 3,000 words for the instructions, the conversation so far and the answer, combined. GPT-4 in March 2023 doubled that to 8k. A medium source file or a long email thread already did not fit.

Inside that budget, <mark style="background: #FFF3A3A6;">prompt engineering meant squeezing the most out of one message: clearer instructions, better examples, a persona, a requested output format.</mark> It worked for single-turn tasks. It could not work for a task that needed the model to hold a codebase, a spec and ten previous steps at once, because there was nowhere to put them.

---

### The failure that forced the change

A multi-step task needs state: what was tried, what came back, what is left. In a 4k window, <mark style="background: #ABF7F7A6;">the state of the task crowded out the instructions, and however well the prompt was worded, the model was answering from an incomplete picture.</mark> Better wording cannot fix missing information.

So the effort moved from writing the message to managing the window. Three techniques defined that move:

- Tool calling: let the model fetch a file when it needs it, instead of pasting every file upfront
- RAG: retrieve the few relevant passages per question from a corpus far larger than the window
- MCP: standardise how those tools and sources plug in, so the set of things a model can reach is pluggable

Each one answers the same question: given a window that cannot hold everything, what goes in, and who decides. <mark style="background: #ADCCFFA6;">When a model underperforms on a long task, check what was in the window before rewriting the prompt.</mark>

---

### Why the shift outlived the constraint

Windows grew to 128k, 200k and 1M tokens by 2025, and the shift did not reverse. <mark style="background: #FF5582A6;">A bigger window raises the ceiling, not the quality: attention over more tokens is noisier and slower, and irrelevant content degrades answers even when it fits.</mark> Context engineering became a discipline in its own right once the window stopped being the bottleneck and its contents became the bottleneck instead.

---

### Read more

- [[Context engineering curates everything in the window and not the wording of one message]]
- [[Tool calling lets a model fetch what it needs during a task instead of being handed everything upfront]]
- [[RAG retrieves the documents a question needs at query time so the model reads only those]]
- [[MCP is an open standard for plugging tools and data sources into any model]]
- [[Prompt Engineering MOC]]
