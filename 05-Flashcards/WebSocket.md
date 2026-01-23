---
created: 2025-01-05
tags: [flashcards, flashcards/networking, flashcards/websocket]
---

# WebSocket Flashcards

## Core Fundamentals

What problem does WebSocket solve that HTTP's request-response model cannot address?
?
**HTTP** prevents **server-initiated data push** — the server must wait for the client to request data. **WebSocket** maintains a **persistent bidirectional connection** allowing the server to push data to clients independently without waiting for requests.

---

How does WebSocket's persistent connection enable real-time applications?
?
By keeping a **TCP connection open continuously**, both client and server can send data at any time without waiting for requests. This eliminates the need for the client to repeatedly poll the server for updates.

---

Why is **polling** inefficient for real-time communication?
?
**Polling** requires the client to repeatedly send requests asking "Do you have updates?" at intervals. This wastes bandwidth with unnecessary requests, introduces latency (updates arrive only after the next poll), and creates scalability problems when many clients poll simultaneously.

---

What is **full-duplex** communication in the context of WebSocket?
?
**Full-duplex** means both the client and server can send and receive data **simultaneously and independently**. Either party can transmit at any time without coordinating with the other, unlike **half-duplex** (alternating directions) or **simplex** (one-way only).

---

How does HTTP Keep-Alive differ from WebSocket bidirectional communication?
?
**HTTP Keep-Alive** reuses the **TCP connection** across multiple requests but still follows the **request-response pattern** (client initiates, server responds). **WebSocket** provides true **bidirectional communication** where either party can send data independently without pairing requests and responses.

---

Persistent connections enable ==continuous bidirectional data flow== between client and server for real-time applications.

---

## Protocol & Upgrade Process

What is the sequence of the WebSocket upgrade handshake?
?
1. Client sends **HTTP request** with **Upgrade: websocket** and **Connection: Upgrade** headers
2. Server validates and responds with **HTTP 101 Switching Protocols**
3. Same **TCP connection** switches from HTTP to WebSocket protocol
4. Both parties can now exchange WebSocket **frames** bidirectionally
<!--SR:!2026-01-06,1,226-->

---

Why must WebSocket start as an HTTP request instead of directly using WebSocket frames?
?
**Firewalls, proxies, and intermediate network devices** only allow traffic on ports 80 and 443 with HTTP protocol. Direct WebSocket frames would be blocked as malformed or non-HTTP traffic. The HTTP upgrade handshake works because it is **valid HTTP**, so proxies allow it through before switching protocols.

---

What is the design rationale for WebSocket to reuse HTTP instead of creating its own dedicated port?
?
Reusing **HTTP ports (80/443)** solves deployment problems: firewalls don't need reconfiguration, proxies already allow the traffic, and there's no network infrastructure change required. A **dedicated WebSocket port would create massive adoption barriers** — enterprises wouldn't open new ports, preventing WebSocket deployment.

---

How do WebSocket and HTTP both rely on the same foundation for connection establishment?
?
Both **HTTP and WebSocket run over TCP** and use the **TCP three-way handshake** to establish the initial connection. The difference is not in how the connection is created, but in what **protocol pattern** runs over the TCP connection after it's established.

---

WebSocket uses ==ws:== for unencrypted connections (port 80) and ==wss:== for encrypted connections (port 443).
<!--SR:!2026-01-06,1,226!2000-01-01,1,250-->

---

Why is the initial WebSocket upgrade request "valid HTTP" critical for proxy compatibility?
?
**HTTP proxies** inspect and validate traffic. If the upgrade request is valid HTTP, the proxy allows it through. Once the proxy sees the **101 Switching Protocols** response, it switches to **pass-through mode** (just forwarding bytes) without further protocol inspection. Without valid HTTP format, the proxy would reject it as malformed.

---

WebSocket ==piggybacking== works because it starts as valid HTTP, allowing it to traverse existing network infrastructure before switching protocols.

---

What three modes do HTTP proxies operate in during WebSocket connection establishment?
?
1. **HTTP mode** — Proxies inspect and validate the upgrade request as valid HTTP, then allow it
2. **Switching protocols mode** — Upon seeing HTTP 101, proxies switch away from HTTP inspection
3. **Pass-through mode** — Proxies forward all subsequent data as opaque byte streams without protocol inspection

---

## Efficiency & Performance

What is the bandwidth advantage of WebSocket frames over HTTP requests?
?
**HTTP requests** include **headers (200+ bytes per request)** even for small messages. **WebSocket frames** have **minimal overhead (2-10 bytes)** for control information. This dramatically reduces bandwidth, especially for applications sending frequent small messages.

---

Why does WebSocket eliminate HTTP header overhead while HTTP Keep-Alive cannot?
?
**HTTP Keep-Alive** reuses the TCP connection but still requires **HTTP headers in every message** (per HTTP protocol). **WebSocket** switches to a **binary frame format** with tiny overhead, sending only control bits and payload without HTTP headers, providing significant bandwidth savings.

---

How do proxies handle the WebSocket upgrade request differently during the handshake?
?
During upgrade, the proxy operates in **HTTP mode**, inspecting the **HTTP 101 Switching Protocols** response. Once it sees this, the proxy switches to **transparent pass-through**, forwarding all subsequent WebSocket frames as opaque bytes without protocol parsing or modification.

---

WebSocket achieves ==high efficiency== by eliminating redundant HTTP headers in post-upgrade communication, requiring only ==2-10 byte frame overhead== per message instead of 200+ bytes.

---

## Frame Structure

What is the basic unit of WebSocket communication and how does it differ from HTTP?
?
The **frame** is the basic unit — **binary data chunks** with control information. Unlike **HTTP messages** which are **text-based** with headers, **frames are binary structures** (2-14 bytes header + payload). After upgrade, only frames are exchanged, not HTTP.
<!--SR:!2026-01-06,1,226-->

---

What information does a WebSocket frame contain?
?
**Frame header (2-14 bytes):**
- **FIN bit** — indicates if this is the final frame or if more frames follow
- **Opcode** — specifies frame type (text 0x1, binary 0x2, close 0x8, ping 0x9, pong 0xA)
- **MASK bit** — indicates if payload is masked
- **Payload length** — size of data; uses extended fields if > 125 bytes

Plus the **payload data** itself.

---

What is the purpose of the **FIN** bit in WebSocket frames?
?
The **FIN bit** indicates whether a frame is the final frame of a message or a continuation. A message can be split across multiple frames for streaming large data. **FIN=1** signals the receiver that all frames for this message have arrived.
<!--SR:!2026-01-06,1,226-->

---

WebSocket frames use ==opcodes== to indicate frame type, such as 0x1 for text, 0x2 for binary, and 0x8 for close frames.

---

Why must client-to-server frames be masked but server-to-client frames must not be?
?
**Masking requirement prevents cache poisoning attacks**: malicious JavaScript could craft WebSocket frames that intermediate proxies/caches misinterpret as HTTP requests, poisoning cached responses. The masking requirement for client frames ensures this cannot happen. **Server frames don't need masking** because servers aren't compromised by JavaScript.

---

What is the masking algorithm used in WebSocket frames?
?
**Masking is XORing** the payload with a **randomly chosen 32-bit key**. Each byte of payload is XORed with the corresponding byte of the repeating key. The receiver uses the same key (transmitted in the frame header) to reverse the operation and recover the original payload.
<!--SR:!2026-01-06,1,226-->

---

WebSocket frames sent from client to server ==must be masked==, while server-to-client frames ==must not be masked== to prevent cache poisoning attacks.
<!--SR:!2026-01-06,1,230!2000-01-01,1,250-->

---

How does WebSocket handle payloads larger than 125 bytes in frame structure?
?
The **payload length field** uses **variable encoding**: 7-bit length for payloads ≤ 125 bytes, 16-bit extended field for 126-65535 bytes, and 64-bit extended field for larger payloads. This allows the frame header to remain compact for small messages while supporting arbitrary-sized payloads.

---

## Connection Lifecycle

What are the four lifecycle states of a WebSocket connection?
?
1. **CONNECTING (0)** — Upgrade handshake in progress; cannot send data
2. **OPEN (1)** — Connection active; both parties can send/receive
3. **CLOSING (2)** — Close handshake initiated; awaiting completion
4. **CLOSED (3)** — Connection fully closed; resources cleaned up
<!--SR:!2026-01-06,1,226-->

---

What restrictions apply when a WebSocket connection is in the **CONNECTING** state?
?
In **CONNECTING**, the **HTTP upgrade handshake is in progress**. The connection is not yet usable, so **no data can be sent or received**. Applications must wait for the **onopen** event before attempting to send messages.

---

What capabilities are available when a WebSocket connection reaches the **OPEN** state?
?
In **OPEN** state, the **upgrade handshake is complete** and the connection is active. Both client and server can **freely send and receive data** at any time. Messages are delivered reliably through the established **TCP connection**.
<!--SR:!2026-01-06,1,226-->

---

What does the **CLOSING** state indicate about a WebSocket connection?
?
**CLOSING** means a **close handshake has been initiated** by one party. The connection is still open but winding down — the initiator has sent a close frame and is awaiting acknowledgment from the other side. No new messages should be sent; the application should wait for **CLOSED** state.

---

How do applications check if a WebSocket connection is ready to send messages?
?
Applications check the **readyState property** before sending:
```javascript
if (socket.readyState === WebSocket.OPEN) {
  socket.send(message);
}
```
**OPEN (value 1)** is the only safe state for sending. Other states (0, 2, 3) indicate the connection is not ready.

---

The WebSocket ==readyState== property tracks connection lifecycle phase: CONNECTING (0), OPEN (1), CLOSING (2), CLOSED (3).

---

## Connection Management

What is the purpose of **Ping-Pong frames** in WebSocket?
?
**Ping-Pong frames** are **control frames** for connection health monitoring: detect dead connections (no response = dead), prevent idle timeouts by proving the connection is alive, and measure **round-trip time**. Either side can send a **ping**, and the receiver must respond with a **pong**.

---

How does the Ping-Pong heartbeat mechanism detect dead connections?
?
One side sends a **ping frame** at regular intervals. The other side **must immediately respond with a pong frame**. If the pong never arrives within a timeout period, the connection is assumed **dead** and should be closed. No pong = no heartbeat = connection lost.

---

Why is the WebSocket close handshake a two-sided protocol instead of abruptly terminating?
?
A **graceful close handshake** ensures both sides agree the connection is ending. The initiator sends a **close frame**, the receiver acknowledges with its own **close frame**, then both sides close the **TCP connection**. This allows final messages to be delivered and prevents data loss from abrupt disconnection.

---

WebSocket close status code ==1000== indicates normal closure, ==1001== indicates going away (server shutdown/page navigation), and ==1006== indicates abnormal closure.

---

What is the sequence of the WebSocket close handshake?
?
1. **Initiator sends close frame** — contains optional close code and reason
2. **Receiver receives close frame** — must send its own close frame in response
3. **Both sides wait** — for acknowledgment and any final data
4. **Both sides close TCP connection** — connection fully terminated

---

What information can be included in a WebSocket close frame?
?
A **close frame** can include:
- **Close status code** (16-bit) — standard codes like 1000, 1001, 1002, 1006, 1011
- **Close reason** (optional UTF-8 text) — human-readable explanation for closing

Status codes indicate the reason for closure (normal, protocol error, server error, etc.).

---

How does a WebSocket connection reaching **CLOSED** differ from **CLOSING**?
?
**CLOSING** means the **close handshake has been initiated** but not yet complete. **CLOSED** means the **close handshake is fully complete** and the **TCP connection is terminated**. In CLOSED state, resources are cleaned up and no further communication is possible.

---

WebSocket ==ping== frames can be sent by either side to check if the connection is alive; the receiver ==must== respond with ==pong==.
<!--SR:!2000-01-01,1,250!2026-01-06,1,230!2000-01-01,1,250-->

---

## Browser WebSocket API

How do you create a WebSocket connection in JavaScript?
?
Use the **WebSocket constructor** with a URL:
```javascript
const socket = new WebSocket('ws://example.com/chat');
const socket = new WebSocket('wss://example.com/chat'); // secure
```
The browser initiates the HTTP upgrade handshake immediately. The connection progresses through states until **onopen** fires.

---

What is the difference between **ws://** and **wss://** WebSocket schemes?
?
**ws://** uses an **unencrypted WebSocket connection** over **port 80** (same as HTTP). **wss://** uses a **secure TLS-encrypted WebSocket connection** over **port 443** (same as HTTPS). **wss:// is required for sensitive data** to prevent eavesdropping.

---

What are the four event handlers available on a WebSocket instance?
?
1. **onopen** — Fires when the **upgrade handshake completes** and connection enters **OPEN** state
2. **onmessage** — Fires when **data arrives** from the other side
3. **onerror** — Fires when an **error occurs** (connection failed, protocol violation, etc.)
4. **onclose** — Fires when the **connection closes** after handshake or gracefully

---

What data types can the **onmessage** event handler receive?
?
The **event.data** property contains the received data in one of three formats:
- **String** — text frames are delivered as strings
- **Blob** — binary data can be received as Blob objects
- **ArrayBuffer** — binary data can also be received as typed arrays

The sender determines the data type; the receiver gets it in the format sent.

---

What properties does the **onclose** event include?
?
The **onclose event** includes:
- **event.code** — numeric close status code (1000, 1001, 1006, etc.)
- **event.reason** — string explanation from the close frame
- **event.wasClean** — boolean indicating graceful close (true) vs abnormal (false)

---

WebSocket's ==send()== method transmits both ==text== (strings, JSON) and ==binary== data (ArrayBuffer, Blob, TypedArray).
<!--SR:!2026-01-06,1,226!2000-01-01,1,250!2000-01-01,1,250-->

---

What data types can be passed to the **send()** method?
?
The **send()** method accepts:
- **Strings** — encoded as text frames: `socket.send('hello')`
- **JSON objects** — convert to string: `socket.send(JSON.stringify({type: 'msg'}))`
- **ArrayBuffer** — binary data: `socket.send(buffer)`
- **Blob** — binary files: `socket.send(blob)`
- **TypedArray** — like Uint8Array: `socket.send(uint8array)`

---

Why can applications only send data when the WebSocket connection is in the **OPEN** state?
?
**OPEN** is the only state where the connection is active and ready for bidirectional communication. In **CONNECTING**, the handshake isn't complete. In **CLOSING/CLOSED**, the connection is terminated or terminating. Sending in other states would fail or be ignored.
<!--SR:!2026-01-08,3,266-->

---

What event indicates that a WebSocket connection has successfully completed the upgrade handshake?
?
The **onopen event** fires when the **HTTP 101 Switching Protocols exchange completes** and the connection enters the **OPEN state**. This is the signal that **bidirectional communication is now possible** and **send()** can be called safely.

---

## Server-Side Patterns

Why must servers store WebSocket connections instead of initiating them to clients?
?
**Clients establish the connections to servers** due to network architecture (NAT, firewalls, dynamic IPs). Servers **cannot initiate connections to clients** because clients aren't listening on a known address. The server must **store the client connections** clients opened and use them to push data back.

---

How does a server push data to a specific client using WebSocket?
?
The server maintains a **data structure mapping client identifiers to WebSocket connections** (e.g., `Map<UserId, WebSocketSession>`). When pushing data to a client, the server **retrieves the stored connection and calls send()** on it:
```javascript
clients.get(userId).send(JSON.stringify(message));
```

---

What architectural challenges arise from servers not being able to initiate connections to clients?
?
Servers must **maintain an in-memory registry** of all connected clients, handle **connection cleanup when clients disconnect**, manage **broadcast patterns** (sending to multiple clients), and deal with **state synchronization** (keeping track of which clients are connected). This is fundamentally different from traditional request-response where connections are transient.

---

WebSocket connections on the server ==must be stored== in a ==data structure== (Map, Set, list) keyed by client identifier to enable ==bidirectional communication== and ==message broadcasting==.
<!--SR:!2000-01-01,1,250!2000-01-01,1,250!2026-01-07,2,246!2000-01-01,1,250-->

---
