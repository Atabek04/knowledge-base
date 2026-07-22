---
created: 2026-07-13
aliases: [silent TCP disconnect, half-open connection, TCP write fails late]
tags: [networking/tcp, os]
---

When a peer closes cleanly, it sends a <mark style="background: yellow">FIN</mark> — the local kernel learns immediately and the next `read()`/`write()` fails right away.

<mark style="background: #ff6b6b">When a peer vanishes instead of closing</mark> — crash, cable pull, laptop sleep, network partition — no FIN ever arrives. The local socket has no signal that anything changed.

---

### Why nothing notices right away

Nothing checks the connection on its own. The failure only surfaces when the app happens to touch the socket:

- `write()` — kernel sends the bytes, gets no ACK, retransmits a few times, only *then* errors (connection reset/timeout) — can take seconds to minutes
- `read()` — just blocks forever waiting for data that will never come
- OS-level TCP keepalive probes exist but default to ~2 hours on Linux — far too slow for an app to rely on

<mark style="background: #74c7ec">A closed socket errors fast. A vanished one just stays quiet until you happen to poke it.</mark>

### Why apps add their own heartbeat

Since the OS won't surface the failure on a useful schedule, the application forces a periodic `write()` itself (WebSocket ping/pong, SSE heartbeat comment). That turns "maybe discovered in 2 hours" into "discovered within one heartbeat interval" — at the cost of only proving the socket was writable *at that moment*, not that the peer is still genuinely there.

---

### Read more
- [[TCP write() blocks when send buffer is full]]
- [[Ping-Pong frames detect dead connections and prevent timeouts]]
- [[Either side can initiate TCP connection termination with FIN]]
- [[TCP MOC]]
