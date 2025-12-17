---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# Ping-Pong frames detect dead connections and prevent timeouts

**Ping and Pong** are **control frames** used for connection health monitoring and keeping long-lived connections alive.

## Three main purposes

1. **Detect dead connections** — determine if the other side is still responsive
2. **Heartbeat mechanism** — prevent idle timeout by proxies/firewalls
3. **Measure round-trip time** — calculate network latency

## How it works

1. One side sends **Ping frame** with optional payload
2. Receiver **must respond** with **Pong frame** containing the same payload
3. If no Pong received within timeout → **connection is dead**

```
Client → Ping frame → Server
Client ← Pong frame ← Server (echoes same payload)
```

## Implementation note

Either side (client or server) can send a Ping at any time. The receiver should automatically respond with a Pong — most WebSocket implementations handle this automatically.

---

## Links

- [[WebSocket frames use binary structure with opcodes and flags]]
- [[WebSocket connection progresses through four lifecycle states]]
- [[WebSocket MOC]]
