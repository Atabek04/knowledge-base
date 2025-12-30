---
created: 2025-12-15
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# Server stores WebSocket connections because it cannot initiate connections to clients

In HTTP, server doesn't need to find clients — they come to it, get a response, connection closes.

In WebSocket, server must push data to clients anytime. But it **cannot create new connections** to them.

**Why server can't connect to clients:**

1. **No public IP** — clients are behind NAT/firewall with private IPs like `192.168.1.5`
2. **Dynamic IPs** — mobile clients change IP addresses constantly
3. **Not listening** — clients don't run servers, no port is open
4. **Firewall blocks** — client OS rejects unsolicited incoming connections

**Solution:** Store the connection the client already opened.

Server maps each connection to user metadata (user ID, session, etc.). When it needs to push data, it uses the existing connection.

```java
Map<UserId, WebSocketSession> connections = new ConcurrentHashMap<>();

// Client connects
connections.put(userId, session);

// Server pushes to specific user
connections.get(userId).send(message);
```

## Links
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[Routers have private IP for LAN and public IP for internet]]
- [[WebSocket MOC]]
