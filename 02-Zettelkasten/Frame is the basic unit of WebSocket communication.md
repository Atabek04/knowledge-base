---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# Frame is the basic unit of WebSocket communication

A **frame** is the basic unit of data transmission in WebSocket — comparable to a packet in network communication.

## Frame vs HTTP message

**HTTP:**
- Sends complete messages with headers
- Each message is independent request/response

**WebSocket:**
- Sends frames (small packets with minimal overhead)
- Frames flow over single persistent connection
- Multiple frames can be fragmented to reassemble one message

## Frame structure

Each frame contains:
- **Control information** (header) — 2–14 bytes
- **Payload data** — the actual message

This minimal overhead makes WebSocket **efficient** for continuous bidirectional communication compared to HTTP's request/response overhead.

---

## Links

- [[WebSocket frames are binary data chunks, not HTTP requests]]
- [[WebSocket frames use binary structure with opcodes and flags]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[WebSocket MOC]]
