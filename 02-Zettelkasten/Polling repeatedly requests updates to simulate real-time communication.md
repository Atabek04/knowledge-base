---
created: 2025-12-08
tags: [networking/patterns]
sr-due:
sr-interval:
sr-ease:
---
Polling is a workaround for HTTP's limitation: server cannot push data first.

Client repeatedly asks "do you have updates?" at fixed intervals (e.g., `GET /messages` every 5 seconds).

**Why it's inefficient:**

1. **Wasted requests**: most polls return "no updates" but consume bandwidth
2. **Latency**: if data arrives after a poll, client waits until next interval
3. **Scalability**: 10,000 clients polling every 5s = 2,000 req/sec even with no updates
4. **Battery drain**: mobile devices waste energy on empty requests

**Root cause — <mark>no good cadence exists</mark>:** the truth being watched is <mark>event-driven</mark> (a slot is booked at an unpredictable moment), but polling can only *guess a fixed interval* at it. Poll fast → mostly-empty wasted requests; poll slow → stale data. You are forced to trade waste against staleness, and no interval wins because you can never predict *when* the event fires. The fix is to stop guessing and let the server speak when the event actually happens — over [[SSE streams server events to client over a single persistent HTTP connection|a single server-to-client stream]] when updates flow one way, or a [[WebSocket maintains persistent TCP connection for bidirectional messaging|persistent bidirectional channel]] when both sides talk.

**Server-push eliminates polling:**

Instead of the client re-asking, it connects <mark>once</mark> and the server pushes each update the instant it happens. Two forms: [[SSE streams server events to client over a single persistent HTTP connection|SSE]] when data flows server→client only (live feeds, dashboards, notifications), [[WebSocket maintains persistent TCP connection for bidirectional messaging|WebSocket]] when the client also sends (chat, games, collaborative editing).

Example comparison for a chat updated over 100 seconds:
- **Polling**: 50 requests, 45 return "no messages" — mostly waste
- **Server-push**: 1 connection setup + N actual messages — zero empty round-trips

## Links
- [[HTTP request-response model prevents server-initiated data push]]
- [[SSE streams server events to client over a single persistent HTTP connection]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[Networking MOC]]
