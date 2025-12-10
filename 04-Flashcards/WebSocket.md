---
created: 2025-12-08
tags: [flashcards/websocket]
---

# WebSocket Flashcards

What is **WebSocket** and what primary problem does it solve?
**WebSocket** is a protocol that provides ==full-duplex== (bidirectional) communication over a single **TCP** connection. It solves the problem that **HTTP request-response model prevents server-initiated data push**, eliminating the need for inefficient polling.

---

How does a **WebSocket connection** start? Explain the upgrade process.
WebSocket starts as an **HTTP Upgrade request**. The client sends an HTTP request with Upgrade headers. The server responds with **HTTP 101 Switching Protocols**. The same TCP connection now speaks **WebSocket protocol** instead of HTTP, enabling bidirectional messaging.

---

What is the fundamental difference between **HTTP Keep-Alive** and **WebSocket**?
**HTTP Keep-Alive:** Reuses the TCP connection but communication is still request-response only. Each message pair has HTTP header overhead. **WebSocket:** Upgrades the connection to enable true bidirectional communication. Either party sends data anytime with minimal frame overhead.

---

Do **HTTP** and **WebSocket** use the same **TCP handshake** for initial connection?
Yes, both **HTTP** and **WebSocket** run on top of **TCP** and use the same **three-way handshake** (SYN, SYN-ACK, ACK) to establish the initial connection. The difference emerges after connection establishment in the protocols that run over TCP.

---

Why does **WebSocket eliminate polling**?
With **WebSocket**, the **server can push data immediately** whenever it's available. The client doesn't need to repeatedly ask "do you have updates?" This eliminates wasted requests, reduces latency, and is more scalable and energy-efficient.

---

What are some real-world use cases for **WebSocket**?
Real-time applications including: **chat** (instant messages), **live notifications** (alerts), **collaborative editing** (shared documents), **live dashboards** (stock prices, metrics), **multiplayer games** (instant state updates), **live streaming** (viewer count, comments).

---

What are the URL schemes for **WebSocket**?
==ws://== for unencrypted WebSocket connections and ==wss://== for encrypted (secure) WebSocket connections.

---

WebSocket starts as an ==HTTP request== and upgrades via HTTP ==101 Switching Protocols==.

---

After the WebSocket upgrade, the connection uses ==frames== instead of HTTP ==headers== for each message.

---

HTTP Keep-Alive requires ==request-response pairing== for each message exchange.

---

WebSocket enables ==bidirectional== communication where ==either party== can send data at any time.

---

**Polling** sends repeated requests asking "do you have ==updates==?" while **WebSocket** allows the ==server== to ==push== immediately.

---

The efficiency advantage of WebSocket over HTTP polling comes from ==eliminating wasted requests== and ==instant push== rather than waiting for polls.

---
