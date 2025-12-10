---
created: 2025-12-08
tags: [networking/patterns]
sr-due:
sr-interval:
sr-ease:
---

# Polling repeatedly requests updates to simulate real-time communication

**Polling** is a workaround pattern to simulate real-time updates when using HTTP's request-response model.

The client repeatedly sends requests at fixed intervals asking "do you have updates?" For example, sending `GET /api/messages` every 5 seconds to check for new messages.

This is **inefficient** for several reasons:

**1. Wasted requests:** Most polls return "no updates" but still consume bandwidth and server resources.

**2. Latency:** If messages arrive 4 seconds after a poll, the client waits up to 5 more seconds to discover them.

**3. Scalability problems:** If 10,000 clients poll every 5 seconds, the server handles 2,000 requests per second—even when there are no updates.

**4. Resource consumption:** Network bandwidth, server CPU, and battery (on mobile) are all wasted on unnecessary requests.

Polling is better than nothing for basic real-time scenarios, but it's inherently inefficient compared to true push mechanisms.

WebSocket eliminates the need for polling by enabling the server to push updates immediately.

## Links

- [[HTTP request-response model prevents server-initiated data push]]
- [[WebSocket eliminates polling by enabling server push]]
- [[Networking MOC]]
