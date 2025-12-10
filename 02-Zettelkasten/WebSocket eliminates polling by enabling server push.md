---
created: 2025-12-08
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket eliminates polling by enabling server push

**Polling** was the workaround for HTTP's limitation: the server cannot send data unless the client requests it first.

With WebSocket, the server can **push data immediately** whenever it's available. The client doesn't need to repeatedly ask "do you have updates?"

This eliminates all the inefficiencies of polling:

**1. No wasted requests:** The server only sends data when there's something to send.

**2. Minimal latency:** Updates arrive instantly, not after waiting for the next poll interval.

**3. Scalable:** The server handles only messages with actual data, not thousands of empty polls.

**4. Energy efficient:** Especially on mobile, eliminating wasted polling reduces battery consumption.

For a chat application:
- **HTTP Polling:** Client asks every 2 seconds. In 100 seconds, 50 requests for messages + 45 "no new messages" responses.
- **WebSocket:** Client asks once (during upgrade). Messages arrive instantly when posted. One request + N actual messages, no wasted polls.

WebSocket's server push capability transforms how real-time applications are built, enabling true event-driven communication.

## Links

- [[Polling repeatedly requests updates to simulate real-time communication]]
- [[HTTP request-response model prevents server-initiated data push]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[WebSocket MOC]]
