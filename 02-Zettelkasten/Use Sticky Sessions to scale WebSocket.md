You store WebSocket connections of client:

```java
// Pseudo-code structure
class WebSocketServer {
    // Store all active connections
    Map<String, WebSocketSession> connections = new ConcurrentHashMap<>();

    // When client connects
    onConnect(WebSocketSession session) {
        String userId = authenticate(session);
        connections.put(userId, session);
        notifyUserOnline(userId);
    }
}
```

You have all payload inside this connection.

Everything seems fine, until you decide scale horizontally…

---

### Problem you'll have after horizontal scaling

![[scaling_issue_websocket.png]]

Your initial request can go to `Server A`, and all connection and payload data will be stored in that instance.

But after some time when you again send request, Load Balancer may redirect you to `Server B`

Now, at this point, you lost your connection and payload data.

---

### Solution

You should use **Sticky Sessions** mechanism.

You simply ***stick*** your session to particular server instance
So your Load Balancer nows to which instance, it should redirect incoming request.

You add filter to your Load Balancer.
You should check for `serverId` inside your Cookies :luc_cookie:

If it's empty, assign it:

```java
Cookie[] cookies = req.getCookies();
String serverId = getServerIdFromCookies(cookies);

if (serverId == null) {
    // First request - assign this server
    serverId = "server-" + InetAddress.getLocalHost().getHostName();
    res.addCookie(new Cookie("SERVER_ID", serverId));
}
```

---

### Sticky Sessions can't help with Cross-Server communication

We have here another issue.
For that please read more about here:
- [[For Cross-Server communication for WebSocket you need message brokers]]
