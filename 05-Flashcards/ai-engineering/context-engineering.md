TARGET DECK: Tech-KB::AI Engineering::Context Engineering
Tags: ai-engineering context-engineering
**Chapter:** Context Engineering, Tool Use, RAG, MCP
**Related:** [[AI Engineering MOC]]

---

START
Coding Questions
Prompt engineering vs context engineering: what does each one control?
Back:
- **Prompt engineering**: the wording of one message (instructions, examples, format). Design time, by a human.
- **Context engineering**: everything in the window on every call (system prompt, tools, retrieved docs, history, memory). Run time, often by the agent.
Prompt engineering is a subset of context engineering.
Tags: ai-engineering context-engineering
<!--ID: 1789920990581-->
END

START
Coding Questions
Model answers badly. How do you decide between fixing the prompt and fixing the context?
Back:
If the model **has** the information and answers badly, fix the prompt. If the model **does not have** the information, no wording will fix it; fix the context.
Tags: ai-engineering context-engineering
<!--ID: 1789920990591-->
END

START
Coding Questions
What drove the shift from prompt engineering to context engineering?
Back:
ChatGPT (Nov 2022) had a 4,096-token window. A multi-step task's state (files, spec, previous steps) crowded out the instructions, so better wording could not help: the model was answering from an incomplete picture. Effort moved from writing the message to managing the window.
Tags: ai-engineering context-engineering
<!--ID: 1789920990593-->
END

START
Coding Questions
Why did context engineering stay relevant after windows grew to 200k or 1M tokens?
Back:
A bigger window raises the ceiling, not the quality. Attention over more tokens is noisier and slower (context rot), so irrelevant content degrades answers even when it fits. The bottleneck moved from window size to window contents.
Tags: ai-engineering context-engineering
<!--ID: 1789920990595-->
END

START
Coding Questions
What is tool calling, mechanically?
Back:
The model emits a structured request naming a registered function and its arguments; the **harness** runs it and appends the result to the context for the next turn. The model never executes anything itself.
Tags: ai-engineering context-engineering
<!--ID: 1789920990596-->
END

START
Coding Questions
Why is a tool description a form of prompt engineering?
Back:
The model reads every tool's name, description and schema on every call and uses them to decide whether and how to call it. A vague description is a vague instruction.
Tags: ai-engineering context-engineering
<!--ID: 1789920990598-->
END

START
Coding Questions
What are the three stages of a RAG pipeline?
Back:
1. **Index**: chunk documents, embed each chunk, store in a vector DB
2. **Retrieve**: embed the question, pull the nearest chunks by similarity
3. **Generate**: place those chunks in the prompt, model answers
Tags: ai-engineering context-engineering
<!--ID: 1789920990599-->
END

START
Coding Questions
What does RAG fix, and what does it not fix?
Back:
Fixes **staleness** (index new docs, no retraining) and **scale** (millions of docs behind a small window). Does not fix **retrieval quality**: if the right chunk is not in the top hits, the model answers confidently from the wrong ones.
Tags: ai-engineering context-engineering
<!--ID: 1789920990600-->
END

START
Coding Questions
What problem does MCP solve, and what are its three roles?
Back:
Bespoke integrations meant N apps × M sources adapters. MCP (Anthropic, Nov 2024) is one open wire format so any host can use any tool server: N + M.
Roles: **Host** (the app), **Client** (one connection per server inside the host), **Server** (exposes tools, resources, prompts over stdio or HTTP).
Tags: ai-engineering context-engineering
<!--ID: 1789920990601-->
END

START
Coding Questions
Is MCP vendor-specific?
Back:
No. It is vendor-neutral by design: the same server serves any model behind any MCP-aware host. Its cost is context, not lock-in: every attached tool spends tokens on every call.
Tags: ai-engineering context-engineering
<!--ID: 1789920990603-->
END
