---
created: 2026-04-28
tags: [networking/sse]
aliases: [SSE vs WebSocket]
sr-due:
sr-interval:
sr-ease:
---

# SSE is unidirectional server-to-client unlike WebSocket bidirectional channel

SSE only flows one way: server pushes, client listens. The client cannot send data back over the same SSE connection.

WebSocket is a full-duplex channel — both sides send and receive freely after the upgrade handshake.

---

### When to choose SSE

| Need | Use |
|---|---|
| Server pushes updates, client just reads | SSE |
| Client also sends messages (chat, games) | WebSocket |
| Want auto-reconnect out of the box | SSE |
| Binary data (audio, video frames) | WebSocket |
| Simple deployment through HTTP proxies | SSE |

SSE is the right tool when data flows in one direction — notifications, live feeds, LLM token streaming.

If the client also needs to send data, use WebSocket or pair SSE with separate POST requests.

---

### Key differences

| | SSE | WebSocket |
|---|---|---|
| Direction | server → client | both |
| Protocol | HTTP | upgraded |
| Auto-reconnect | yes | no (manual) |
| Text only | yes | text + binary |
| Proxy-friendly | yes | sometimes |

## Read more
- [[SSE streams server events to client over a single persistent HTTP connection]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[SSE MOC]]
