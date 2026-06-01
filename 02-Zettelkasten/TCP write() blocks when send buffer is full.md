---
created: 2026-06-01
tags: [networking/tcp, os]
aliases: [TCP send buffer blocking, write() blocks]
---

When your app calls `write()`, the OS copies data from your process into the <mark style="background: yellow">kernel-managed TCP send buffer</mark> — a fixed-size region in memory between your code and the network card.

The OS drains this buffer by shipping bytes to the remote peer. If the peer reads slowly, the buffer fills up and the OS has nowhere to put new bytes.

<mark style="background: #ff6b6b">When the buffer is full, `write()` does not return.</mark> The calling thread is suspended at that line until the peer reads enough data to free space.

---

### Why the peer controls your server

The flow is:

```
your app → kernel send buffer → network → peer's receive buffer → peer app
```

If the peer app reads slowly → peer receive buffer fills → TCP flow control signals "stop sending" → your kernel send buffer fills → `write()` blocks.

<mark style="background: #74c7ec">The slow reader at the end of the chain reaches back and freezes your server thread.</mark>

### Read more
- [[SSE backpressure matters when LLM generates faster than client consumes]]
- [[Buffers store data during transfers between components with speed mismatches]]
- [[SSE keeps HTTP response body open to push text chunks continuously]]
