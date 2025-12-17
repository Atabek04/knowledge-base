---
created: 2025-12-17
tags: [networking/tcp]
sr-due:
sr-interval:
sr-ease:
---

# Either side can initiate TCP connection termination with FIN

![[connection_termination_FIN_TCP.png]]

**TCP connection termination** is bidirectional — either the **client** or **server** can send the first **FIN** (finish) signal.

In **HTTP**, the client most commonly initiates termination after receiving the response.

However, the **server can initiate** termination too:
- **Timeout** — client hasn't sent requests within keep-alive window
- **Errors** — server encounters fatal error processing request
- **Resource limits** — server needs to free up connections

This bidirectional termination capability means applications must handle unexpected connection closures from either end.

---

## Links

- [[FIN terminates TCP connections through graceful shutdown handshake]]
- [[TCP three-way handshake establishes connection with SYN-SYN-ACK-ACK]]
- [[TCP MOC]]
