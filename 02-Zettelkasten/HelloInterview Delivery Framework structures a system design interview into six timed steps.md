---
aliases: [Delivery Framework, HelloInterview system design framework]
created: 2026-05-27
tags: [system-design, interview-prep, framework]
---

### The Problem It Solves

System design interviews are open-ended and easy to derail — you can burn 20 minutes estimating capacity or chase complexity before a single requirement is pinned down. The Delivery Framework imposes a fixed running order with time budgets so you always ship a complete, working design inside ~45 minutes.

---

### The Six Steps (45-min interview)

| # | Step | Time | What you produce |
|---|------|------|------------------|
| 1 | **Requirements** | ~5 min | Top 3 functional ("users can…") + non-functional (scale, latency, availability). Estimate capacity **only** if it changes the design. |
| 2 | **Core Entities** | ~2 min | 3–5 domain nouns (User, Tweet, Follow). |
| 3 | **API / Interface** | ~5 min | 4–6 endpoints, REST by default. Current user from the auth token, never the request body. |
| 4 | **Data Flow** *(optional)* | ~5 min | Only for data-processing systems: Fetch → Parse → Store. |
| 5 | **High-Level Design** | ~10–15 min | Boxes + arrows. Walk through each API endpoint and show what state changes. |
| 6 | **Deep Dives** | ~10 min | Satisfy the non-functional requirements; find and kill bottlenecks (caching, sharding, fanout). |

---

### Guiding Principles

- **3 requirements beats 10** — ruthless prioritization is what wins offers; breadth dilutes.
- **Simplicity first** — get a working design on the board before adding complexity in deep dives.
- **Narrate the data flow** — say out loud what state changes on each request.
- **Iterate the diagram** — update boxes/arrows as new requirements surface; don't redraw from scratch.

---

### Why This Order

Requirements and entities are cheap and anchor everything downstream, so they come first. The API is the contract the high-level design must satisfy, so it precedes the diagram. Deep dives come last because you can only harden a design that already exists — premature optimization with no system on the board is wasted time.

---

Source: [HelloInterview — Delivery Framework](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery)

Read more:
- [[System Design - MOC]]
- [[Interview-Prep-Master-Plan]]
