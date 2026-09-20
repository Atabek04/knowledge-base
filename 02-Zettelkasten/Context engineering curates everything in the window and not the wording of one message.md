---
aliases: [context engineering, context engineering vs prompt engineering]
created: 2026-09-20
---

A model's answer is a function of exactly one thing: the tokens in its context window at the moment of the call. The prompt the developer wrote is one part of that. The rest is the system prompt, the tool definitions, the retrieved documents, the conversation history, the tool results from earlier turns, and any memory that was loaded.

<mark style="background: #FFF3A3A6;">Context engineering is the discipline of deciding, on every call, which tokens from the whole universe of available information go into the window, and which stay out.</mark> Prompt engineering is a subset of it: the part about wording the instructions. Anthropic's September 2025 guide frames context as a finite resource with diminishing returns per token, which is why the two are not the same job.

The term spread in mid-2025 (Tobi Lütke, Andrej Karpathy) once agent builders noticed that most failures were context failures: the right information was available, and it was not in the window, or was buried under the wrong information.

---

### Prompt versus context, side by side

| | Prompt engineering | Context engineering |
|---|---|---|
| Unit of work | one message | the whole window, per call |
| Timing | design time, by a human | run time, often by the agent itself |
| Fixes | unclear instructions | missing or irrelevant information |
| Tools | phrasing, examples, format | retrieval, tool calling, compaction, memory, sub-agents |

<mark style="background: #ADCCFFA6;">If the model has the information and answers badly, fix the prompt; if the model does not have the information, no prompt will fix it, fix the context.</mark>

---

### The core techniques

- **Just-in-time loading**: tools, files and skills are fetched when a step needs them, not front-loaded. Tool calling, RAG and MCP are the plumbing.
- **Compaction**: when the window fills, summarise the history and continue from the summary.
- **Structured notes and memory**: the agent writes state to a file outside the window and reads it back later.
- **Sub-agent isolation**: a worker gets a clean window for one sub-task and returns only a summary.

<mark style="background: #ABF7F7A6;">Every technique trades the same thing: fewer tokens in the window, chosen better, in exchange for an extra step to choose them.</mark>

---

### The trap of a big window

<mark style="background: #FF5582A6;">Filling a large window is not context engineering; it is the absence of it.</mark> Attention degrades as the window fills (context rot), so a 200k window stuffed with everything performs worse than a 20k window holding what the step needs.

---

### Read more

- [[Small context windows made single prompts insufficient for multi-step tasks and forced the shift to context engineering]]
- [[Tool calling lets a model fetch what it needs during a task instead of being handed everything upfront]]
- [[RAG retrieves the documents a question needs at query time so the model reads only those]]
- [[MCP is an open standard for plugging tools and data sources into any model]]
- [[Rich personal context is the main differentiator between elite and average AI users]]
- [[Prompt Engineering MOC]]
- [[AI Engineering MOC]]
- Source: [Effective context engineering for AI agents, Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
