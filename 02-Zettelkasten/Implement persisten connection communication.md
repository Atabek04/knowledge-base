---
created: 2025-12-12
tags:
  - networking/websocket
  - networking/socket
sr-due:
sr-interval:
sr-ease:
---
### Persistent connection implemented in protocol level

So it's not implemented in application level.

In protocol layer it's implemented by:
1. **Not closing the TCP connection after response**
2. <mark style="background: #ABF7F7A6;">**Keeping the socket open** in waiting/listening state</mark>

so what's the socket ??
## Links
[[Persistent connections enable continuous bidirectional data flow]]
[[Socket is]]