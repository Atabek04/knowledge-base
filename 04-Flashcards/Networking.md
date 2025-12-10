---
created: 2025-12-08
tags: [flashcards/networking]
---

# Networking Flashcards

What is the fundamental difference between **request-response** communication and **persistent connection** communication?
In **request-response** communication, the client sends a request, the server responds, and the connection closes. In **persistent connection** communication, the connection stays open and either party can send data at any time without new requests.

---

Why can't traditional **HTTP** efficiently handle scenarios where the **server needs to push data** to the client in **real-time**?
**HTTP** is built on a **request-response model** where only the **client can initiate** communication. The server cannot send data unless the client asks for it first, creating polling inefficiency and latency.

---

What is **polling** and what are its main inefficiencies?
**Polling** is when the client repeatedly asks "do you have updates?" at fixed intervals (e.g., every 5 seconds). Inefficiencies include: wasted requests when there are no updates, latency delays between data availability and client discovery, scalability problems from thousands of empty polls, and resource waste on bandwidth and battery.

---

What is **connection pooling** and where is it commonly used?
**Connection pooling** maintains a reusable pool of connections at the application level. Instead of creating new connections repeatedly, you borrow from the pool, use the connection, and return it. Common examples: **HikariCP** for database connections, **Apache HttpClient** pool for HTTP requests.

---

Request-response communication requires a ==new request== for each data exchange.

---

Persistent connections stay ==open== and allow ==either party== to send data at any time.

---

The difference between **HTTP Keep-Alive** and **polling** is that Keep-Alive ==reuses the TCP connection== while polling ==repeatedly requests== updates.

---

Connection overhead is reduced by ==reusing== connections, whether through **HTTP Keep-Alive** (protocol level) or **connection pooling** (application level).

---

Server push is the advantage of ==WebSocket== over ==HTTP== polling.

---

The ==communication pattern== differs between HTTP (request-response) and WebSocket (bidirectional).

---
