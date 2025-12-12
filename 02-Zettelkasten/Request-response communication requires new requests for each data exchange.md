---
created: 2025-12-08
tags:
  - networking/patterns
sr-due:
sr-interval:
sr-ease:

---

In **request-response communication**, the client sends a request to the server, the server processes it, and sends back a response. 
Then the connection typically **closes** or returns to **idle state**.

Each interaction is independent. 
To get new data, the client must send another request.

Think of it like sending a letter and waiting for a reply. 
Once you receive the reply, the conversation ends.

This pattern is the foundation of traditional client-server architecture. 
The client is always the initiator—the ==server cannot send data unless the client asks for it first==.

The connection lifecycle is therefore: ==establish → request → response → close (or pool)==.

## Links

- [[Persistent connections enable continuous bidirectional data flow]]
- [[HTTP request-response model prevents server-initiated data push]]
- [[Networking MOC]]
