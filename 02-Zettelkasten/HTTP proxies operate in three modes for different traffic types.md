---
created: 2025-12-17
tags: [networking/http, networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# HTTP proxies operate in three modes for different traffic types

Proxies can handle network traffic in **three different modes**, each suited for different protocols and use cases.

## 1. HTTP Proxy Mode (Application Layer)

- Proxy **understands HTTP protocol**
- Parses and inspects all requests/responses
- Can **cache, modify, filter** content
- Used for: regular HTTP traffic

## 2. Transparent Pass-Through / TCP Tunnel Mode

- Proxy **forwards raw TCP bytes** without inspection
- Doesn't understand or parse the protocol
- Just moves data: `Client <-> Proxy <-> Server`
- Used for:
  - **WebSocket after upgrade** — proxy can't understand frames
  - Any TCP protocol proxy doesn't understand

## 3. CONNECT Tunnel Mode

- Similar to pass-through, **specifically for HTTPS/WSS**
- Client sends: `CONNECT example.com:443`
- Proxy creates tunnel for **encrypted traffic**
- Proxy can't inspect encrypted content

WebSocket leverages modes 1 and 2: the upgrade request goes through **HTTP mode** (inspected), then the connection switches to **pass-through mode** (forwarded without inspection).

---

## Links

- [[WebSocket piggybacking works, because initial request is valid]]
- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[WebSocket MOC]]
- [[Forward proxy hides the client's identity by relaying requests to the destination server]]
- [[Reverse proxy hides the origin server's IP by relaying client requests to backend servers]]
