---
created: 2025-12-12
tags: [networking/socket]
sr-due:
sr-interval:
sr-ease:
---

# Persistent connections keep sockets open at protocol level not application level

Persistent connections are implemented by the protocol (TCP/WebSocket), not your application code.

At protocol level, this means:
1. **Not sending FIN** after response — TCP connection stays open
2. **Socket remains in ESTABLISHED state** — both sides keep listening
3. **Continuous read loop** instead of close after one read

```java
// Request-Response: close after exchange
socket = connect()
write(request)
read(response)
close(socket)  // ← ends here

// Persistent: keep open
socket = connect()
while (socket.isOpen()) {
    if (hasDataToSend) write(data)
    if (hasDataToRead) read(data)
    // socket stays open
}
```

TCP connections stay open by default until explicitly closed with FIN packet.

## Links
- [[Persistent connections enable continuous bidirectional data flow]]
- [[Socket is OS object tool to use protocols like HTTP, WebSocket]]
- [[TCP provides reliable ordered error-checked data delivery over networks]]
- [[Networking MOC]]
