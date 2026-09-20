---
aliases: [MCP, Model Context Protocol]
created: 2026-09-20
---

Tool calling works, but every integration was bespoke: a GitHub tool written for one app could not be reused by another app, and a tool written for one model provider had to be rewritten for the next. N apps times M data sources meant N × M adapters.

<mark style="background: #FFF3A3A6;">The Model Context Protocol is an open standard, released by Anthropic in November 2024, that defines one wire format for a model host to discover and call tools, read resources and load prompts from an external server.</mark> Write an MCP server for GitHub once, and any MCP-aware host (Claude Desktop, Claude Code, an IDE, a custom agent) can use it. USB-C for AI tools is the usual analogy: one connector, many devices.

---

### The three roles

- **Host**: the application the user talks to (an IDE, a chat app, an agent).
- **Client**: the connection inside the host, one per server.
- **Server**: a small program exposing tools, resources and prompts, running locally over stdio or remotely over HTTP.

The host lists each server's tools into the model's context; when the model calls one, the client forwards the request and returns the result. <mark style="background: #ABF7F7A6;">MCP does not change what tool calling is; it standardises who provides the tools and how they are found, so the set of tools becomes pluggable instead of hard-coded.</mark>

---

### What it is not

<mark style="background: #FF5582A6;">MCP is vendor-neutral by design; calling it a vendor-specific integration mechanism gets it backwards.</mark> It is the opposite of vendor lock-in: the same server serves any model behind any host. What it does not solve is judgement about which tools to expose. Every listed tool costs context tokens on every call, so a host with fifty servers attached has a context-engineering problem, not an integration problem.

---

### Read more

- [[Tool calling lets a model fetch what it needs during a task instead of being handed everything upfront]]
- [[Context engineering curates everything in the window and not the wording of one message]]
- [[AI Engineering MOC]]
