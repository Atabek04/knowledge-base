---
aliases: [tool calling, function calling, tool use]
created: 2026-09-20
---

A plain LLM call is a closed box: whatever the prompt does not contain, the model cannot know. Tool calling opens the box. The developer registers a set of functions (read a file, run a query, search the web), each with a name, a description and a JSON schema for its arguments.

<mark style="background: #FFF3A3A6;">Tool calling is the model emitting a structured request to run one of those functions, the harness running it, and the result being appended to the context for the next turn.</mark> The model never executes anything itself; it only asks, and the application code around it decides and runs.

OpenAI shipped this as "function calling" in June 2023; every major provider now has an equivalent.

---

### Why it changes what a prompt has to contain

Before tool calling, the only way for a model to see a file was for the developer to paste the file into the prompt, in advance, guessing which files would matter. With tools, <mark style="background: #ABF7F7A6;">the model pulls context on demand: it reads the two files it decides are relevant instead of being given twenty it might need.</mark> The context window stays small and the coverage gets larger, because loading is decided at run time by the model rather than at design time by the author.

This is the mechanism behind agent loops: observe the tool result, think, call the next tool, repeat.

---

### What the model actually reads

The model sees the tool's name, description and argument schema in the prompt on every call. <mark style="background: #FF5582A6;">A vague tool description is a vague prompt; the description is the instruction the model follows when deciding whether and how to call it.</mark> Tool design is prompt engineering that happens to live in a schema.

---

### Read more

- [[Context engineering curates everything in the window and not the wording of one message]]
- [[MCP is an open standard for plugging tools and data sources into any model]]
- [[AI Engineering MOC]]
