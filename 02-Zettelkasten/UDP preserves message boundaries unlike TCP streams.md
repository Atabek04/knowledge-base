---
created: 2025-12-08
tags: [networking/protocols]
sr-due:
sr-interval:
sr-ease:
---

# UDP preserves message boundaries unlike TCP streams

This note compares **stream-oriented** (TCP) and **message-oriented** (UDP) protocols.

**Stream-oriented (TCP):**
- Data is treated as a **continuous byte stream** with no boundaries.
- If you send "Hello" then "World", the receiver might read "HelloWorld" or "Hel" then "loWorld"—no message boundaries preserved.
- The application must define its own message boundaries if needed.

**Message-oriented (UDP):**
- Data is treated as **discrete messages** (datagrams).
- If you send "Hello" then "World", they arrive as two separate messages.
- Message boundaries are **preserved by the protocol**.
- However, UDP packets can be lost, arrive out of order, or arrive multiple times (no reliability guarantees).

**Key point:** TCP is stream-oriented at the API level (continuous bytes) but still uses packets underneath. The packets are just hidden from you by TCP's abstraction.

WebSocket runs on TCP, so it inherits the stream-oriented behavior. However, WebSocket adds its own message framing on top to preserve message boundaries for applications.

## Links

- [[TCP stream abstraction hides packetization from applications]]
- [[TCP MOC]]
