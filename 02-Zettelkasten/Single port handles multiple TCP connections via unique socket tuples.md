---
created: 2025-12-17
tags: [networking/tcp]
sr-due:
sr-interval:
sr-ease:
---

# Single port handles multiple TCP connections via unique socket tuples

A server listening on **port 80** can handle **multiple simultaneous TCP connections** because each connection is uniquely identified by a **4-tuple**:

```
(Source IP, Source Port, Destination IP, Destination Port)
```

**Example — server with mixed HTTP and WebSocket connections:**

```
Connection 1: (1.1.1.1, 50000, server.com, 80) ← WebSocket
Connection 2: (2.2.2.2, 51000, server.com, 80) ← HTTP request
Connection 3: (3.3.3.3, 52000, server.com, 80) ← WebSocket
```

All three use **port 80**, but they're **different TCP connections** because their source IP/port combinations differ.

**When a new HTTP request arrives while WebSocket is active:**

```
Port 80 on Server:
├─ TCP Connection 1: WebSocket with Client A
│   └─ Sending/receiving WebSocket frames
│
├─ TCP Connection 2: New HTTP request from Client B
│   └─ Processes as normal HTTP
│   └─ Returns response
│   └─ Connection closes (or goes to Keep-Alive pool)
│
└─ TCP Connection 3: WebSocket with Client C
    └─ Sending/receiving WebSocket frames
```

This is why WebSocket can coexist with regular HTTP on the same port — the server distinguishes connections by their unique tuples, not just the port number.

---

## Links

- [[TCP three-way handshake establishes connection with SYN-SYN-ACK-ACK]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[TCP MOC]]
