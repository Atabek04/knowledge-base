## Scenario

![[cross_server_communication_issue_websocket.png]]

Ayub wants to send message to Zayid.
But Zayid is being served in another server instance.

So in order to solve that, we should have message broker.
We can use `Redis` for Pub/Sub model.

We gonna create channels (kinda queues) for each user.
When one instance publishes message, other gonna receive it.
Then check do they have that user's connection.
If yes, they gonna send message.

```java
// Server 1: Client A sends message to Client B
public void sendMessage(String fromUser,
					String toUser,
					String message) {
    // Publish to Redis channel
    redisTemplate.convertAndSend("ws:user:" + toUser, message);
    // ALL server instances listening to this channel receive it
}

// Server 2: Subscribed to Redis, receives message, sends to Client B
@RedisListener(topics = "ws:user:*")
public void onMessage(String channel, String message) {
    String userId = extractUserId(channel); // "clientB"
    WebSocketSession session = localSessions.get(userId);
    if (session != null) {
        session.sendMessage(new TextMessage(message));
        // Send to Client B
    }
}
```

![[redis_cross_server_communication_websocket.png]]
