---
created: 2025-12-30
tags: [flashcards/tcp]
---

# TCP Flashcards

Comprehensive flashcards for TCP protocol concepts from the TCP MOC. Covers fundamentals, connection lifecycle, data transmission, stream abstraction, and security.

---

## Fundamentals

What are the three key guarantees that TCP provides?
?
**Reliability:** TCP detects **lost packets** via **sequence numbers** and **ACKs**, and **automatically retransmits** missing data.

**Ordered delivery:** TCP numbers **every byte** with **sequence numbers**, allowing the receiver to **reassemble** packets in the **correct order** even if they arrive out of sequence.

**Error-checked delivery:** TCP adds a **checksum** to every segment, allowing the receiver to **detect corruption** and **discard corrupted segments** (higher layers request retransmission).

These three guarantees make TCP **reliable and predictable** for applications like email, file transfer, and web browsing.
<!--SR:!2026-01-06,1,230-->

---

---

How does a single port handle multiple TCP connections simultaneously?
?
TCP uses a **4-tuple** (socket) to identify each unique connection:

**(Source IP, Source Port, Destination IP, Destination Port)**

Example: Port 80 (HTTP) can simultaneously handle:
- (192.168.1.10:12345, 198.51.100.1:80) — Client A
- (192.168.1.11:12346, 198.51.100.1:80) — Client B
- (192.168.1.12:12347, 198.51.100.1:80) — Client C

Each combination is **unique**, so the server can maintain **multiple connections** on the **same port**. This is called **port multiplexing**. The **transport layer** uses the **4-tuple** to route incoming segments to the correct process.
<!--SR:!2026-01-06,1,230-->

---

---

## Connection Lifecycle

What are the three steps in TCP's three-way handshake?
?
**Step 1 (SYN):** Client sends a segment with the **SYN flag set** and its **Initial Sequence Number (ISN)**, e.g., X. This says "I want to connect, starting from sequence number X."

**Step 2 (SYN-ACK):** Server receives the SYN, **acknowledges X** (with ACK=X+1), sends its own **ISN** (e.g., Y), and sets the **SYN flag** to synchronize. This says "I received your X, and I'm starting from sequence number Y."

**Step 3 (ACK):** Client receives the SYN-ACK, **acknowledges Y** (with ACK=Y+1), and sends an ACK segment (no more SYN flag). This says "I received your Y, ready for Y+1."

After these **three steps**, both sides have **synchronized sequence numbers** and the connection is **established**.
<!--SR:!2026-01-08,3,250-->

---

---

Why do both client and server send sequence numbers during the handshake?
?
**Sequence numbers** form the foundation of TCP's **reliability and ordering**. Each side must independently **choose a random starting sequence number** to:

(1) Avoid **sequence prediction attacks** — an attacker cannot forge packets if the ISN is **random and unpredictable**.

(2) **Track data bytes** — each side knows what data the other has received based on **ACK numbers**.

(3) **Handle packet reordering** — if packets arrive out of order, sequence numbers allow **reassembly in correct order**.

The **SYN handshake** synchronizes these starting numbers so both sides agree on what **byte numbers** mean for that connection.
<!--SR:!2026-01-06,1,230-->

---

---

What does the ACK flag communicate?
?
The **ACK flag** signals **acknowledgment** — confirmation that the sender has **received data successfully**.

**ACK number = N** means: "I have successfully received all bytes **up to and including byte N-1**. The **next byte I expect is N**."

Example: If the receiver gets bytes 0-999, it sends ACK=1000 (expecting byte 1000 next).

**Important for reliability:** ACK signals are how TCP implements **reliable delivery**. If the sender doesn't receive an **ACK for sent data**, it **retransmits**. The **ACK number** tells the sender exactly how much data was received.

**Note:** The **SYN flag consumes one sequence number**, so if SYN=X, the first data byte after SYN starts at X+1.
<!--SR:!2026-01-06,1,230-->

---

---

How does TCP's three-way handshake differ from the connection termination process?
?
**Three-way handshake (connection establishment):**
- **Two exchange** of SYN and SYN-ACK messages.
- **Synchronizes sequence numbers**.
- **Result:** Connection ready for data.

**Four-way handshake (graceful termination):**
- **FIN (Finish) flag** replaces SYN.
- **Each direction closes independently** — either side can initiate.
- Steps: (1) Client sends FIN; (2) Server ACKs FIN; (3) Server sends FIN; (4) Client ACKs.
- **Important:** Data can continue flowing **after FIN** in the opposite direction (**half-closed state**).

**Why graceful?** Both sides confirm termination, preventing **data loss** if one side closes unexpectedly.
<!--SR:!2026-01-06,1,230-->

---

---

How does the FIN flag enable graceful TCP connection shutdown?
?
**FIN (Finish) flag** signals "I'm done sending data" without abruptly closing the connection.

**Graceful shutdown process:**

(1) **Initiator sends FIN:** "I'm finished; I won't send more data."

(2) **Receiver ACKs FIN:** "I received your FIN."

(3) **Receiver sends FIN:** "I'm done too."

(4) **Initiator ACKs FIN:** "Connection closed."

**Why graceful:** The **receiver can still send data** after receiving FIN (**half-closed state**). The sender waits for the receiver's FIN before closing. This prevents **data loss** if one side closes prematurely.

**Alternative:** **RST flag** (reset) abruptly closes without graceful shutdown (used only for errors).
<!--SR:!2026-01-06,1,230-->

---

---

Why is either side able to initiate TCP termination?
?
TCP connections are **bidirectional and symmetrical** — both client and server have **full capabilities** to send and receive data.

**Server-initiated termination scenarios:**
- Server detects an **error** and closes.
- Server reaches a **resource limit** and closes idle connections.
- Server is **shutting down gracefully** and closes all connections.

**Client-initiated termination scenarios:**
- User **closes the application**.
- Connection becomes **idle** and client closes to free resources.

**Key principle:** Either side can send **FIN** because TCP doesn't distinguish **initiator** from **responder** — once established, the connection is **fully bidirectional**.

**Applications must handle** unexpected closures from either end (e.g., server disconnection while client is active).
<!--SR:!2026-01-06,1,230-->

---

---

How does HTTP Keep-Alive reuse TCP connections?
?
**HTTP Keep-Alive** prevents the **FIN signal** by using the **Connection: Keep-Alive** header (default in HTTP/1.1). After responding, the **server doesn't close the TCP connection**.

**Process:**
(1) Client sends HTTP request over **new TCP connection**.
(2) Server sends HTTP response.
(3) **Connection stays open** (no FIN).
(4) Client sends **another HTTP request** over the **same TCP connection**.
(5) Server sends response, connection remains open.
(6) Eventually connection **times out** or is explicitly closed.

**Benefits:** Avoids **expensive three-way handshake** for each request, improving performance for **same-server** requests.

**Cost:** Server must manage **connection limits** — too many idle connections waste resources.
<!--SR:!2026-01-06,1,230-->

---

---

## Data Transmission

What is the purpose of TCP sequence numbers?
?
**Sequence numbers** track **individual bytes** in the data stream. Each byte has a unique sequence number, enabling three key functions:

**Ordering:** If packets arrive **out of order**, TCP uses sequence numbers to **reassemble in correct order**. Example: Receives bytes 500-599, then 400-499 — reorders them correctly.

**Completeness detection:** Sequence numbers reveal **missing bytes**. If expecting byte 1000 but receive 1001-1099, the gap shows bytes 1000 is missing — request retransmission.

**Duplicate detection:** If the receiver sees **duplicate sequence numbers**, the segment is discarded (already processed).

**Example:** Sending 1000 bytes starting at sequence 5000. Bytes are numbered 5000-5999. Receiver sending ACK=6000 means "received all bytes up to 5999, expecting 6000 next."
<!--SR:!2026-01-06,1,230-->

---

---

What exactly is a TCP packet and how does it relate to segments?
?
A **TCP packet** is a **chunk of data** transmitted over the network containing two parts:

**Headers:** **Metadata** including source/destination ports, sequence numbers, flags (SYN, ACK, FIN), checksum, and other control information.

**Payload:** The **actual data** being transmitted.

**Terminology note:** Networking often calls TCP packets **"segments"** to distinguish them from **network-layer packets** (which include IP headers). The **network layer** wraps the **TCP segment** into a **packet** by adding IP headers.

**Analogy:** Shipping a 1000-page book by splitting it into 10 boxes of 100 pages each. Each box = **packet** (headers/metadata + 100 pages/payload).

**Important:** The **network layer automatically segments** data based on **Maximum Transmission Unit (MTU)** — the application doesn't manually split data.
<!--SR:!2026-01-06,1,230-->

---

---

How does Maximum Transmission Unit limit packet size and affect performance?
?
**MTU (Maximum Transmission Unit)** is the **maximum frame size** a network link can transmit. **Typical MTU: 1500 bytes**.

**MTU accounting:**
- **20 bytes:** TCP header
- **20 bytes:** IP header
- **1460 bytes:** Actual data payload

**Example:** Sending 5000 bytes requires **at least 4 packets:**
- Packet 1: 1460 bytes
- Packet 2: 1460 bytes
- Packet 3: 1460 bytes
- Packet 4: 620 bytes

**Smaller MTU = more packets** → more overhead and slower performance.

**Larger MTU = fewer packets** → better performance but larger individual packet loss.

**Path MTU Discovery:** Systems probe the network to find the **smallest MTU** on the path and adjust segment size accordingly.
<!--SR:!2026-01-06,1,230-->

---

---

## Stream Abstraction

Why does TCP appear as a continuous stream rather than discrete packets to applications?
?
TCP implements a **stream abstraction** — applications see a **continuous byte flow** instead of individual packets. This **illusion** hides the underlying **packetization**.

**At network level:** Data travels in **discrete packets** (e.g., 1500 bytes each), independently routable and potentially arriving **out of order** or with **gaps**.

**At application level:** TCP guarantees appear as a **continuous stream** using:

(1) **Sequence numbers** to identify individual bytes.

(2) **ACKs** to confirm receipt.

(3) **Reordering logic** to rearrange out-of-order packets.

(4) **Retransmission** for lost packets.

**Example:** Application calls `read()` and gets "Hello World" as a continuous string, not caring that it arrived in three separate packets of sizes 3, 5, and 6 bytes.

**Trade-off:** Stream abstraction simplifies application programming but hides message boundaries — applications must define their own boundaries (e.g., HTTP uses headers, WebSocket uses frames).
<!--SR:!2026-01-06,1,230-->

---

---

How does TCP's stream model differ from UDP's message model?
?
**TCP (Stream-oriented):**
- Data is a **continuous byte sequence**.
- **No message boundaries** preserved — if you send "Hello" + "World" in two writes, receiver might read "HelloWorld" in one read, or "H" + "elloWorld" in two reads.
- Application must **define boundaries** (e.g., HTTP uses **\r\n\r\n** to separate headers from body).
- **Reliable and ordered**.

**UDP (Message-oriented):**
- Data is **discrete datagrams** with **preserved boundaries**.
- Each datagram is independent — if you send "Hello" and "World" in two datagrams, receiver gets **exactly two separate messages**, never mixed.
- No need to define boundaries; **message boundaries are automatic**.
- **Unreliable** — datagrams can be lost, duplicated, or reordered.

**Real-world example:** **WebSocket** adds **framing** on top of TCP to recover message boundaries, combining TCP's **reliability** with **message preservation**.
<!--SR:!2026-01-06,1,230-->

---

---

## Security

Why is Initial Sequence Number randomization important?
?
**ISN (Initial Sequence Number)** is the **starting sequence number** each side chooses during the three-way handshake. **ISN must be random**, not predictable.

**Attack scenario without randomization:**
- Attacker observes a few ISNs and **predicts the next one**.
- Attacker **forges TCP segments** with the predicted ISN.
- Victim accepts the **forged segments as legitimate**.
- Attacker **hijacks the connection** and injects malicious data (e.g., "DELETE FROM users" in a database connection).

**Randomization prevents this:**
- ISN is **cryptographically random**.
- Attacker **cannot predict** the next ISN.
- **Forged segments are rejected** because they don't match the actual ISN.

**Modern TCP** uses **pseudorandom number generators** to ensure ISN unpredictability, making **TCP sequence hijacking attacks** extremely difficult.
<!--SR:!2026-01-06,1,230-->

---

---

## Higher-Level Protocols

How do HTTP and WebSocket rely on TCP as their foundation?
?
Both **HTTP** and **WebSocket** are **application-layer protocols** built **on top of TCP**.

**Shared TCP capabilities:**

Both use **TCP's three-way handshake** for connection establishment.

Both benefit from **TCP's reliability** (retransmission, ordering, error-checking).

Both send **application data** over **TCP's stream abstraction**.

**HTTP characteristics:**
- **Request-response** pattern.
- Relies on TCP's **reliability** for guaranteed delivery of HTTP headers and bodies.
- Server **cannot initiate** — must wait for client requests.

**WebSocket characteristics:**
- Starts as **HTTP upgrade handshake** (uses HTTP on TCP).
- Then switches to **WebSocket protocol** for **bidirectional** communication.
- Relies on TCP for **delivery guarantees**.

**Key insight:** TCP provides the **reliable transport foundation**. The difference is the **application protocol** (HTTP headers/methods vs. WebSocket frames) and **communication pattern** (request-response vs. bidirectional).
<!--SR:!2026-01-06,1,230-->

---

---

## Cloze Drilling: Flags and Technical Terms

The ==SYN== flag **synchronizes** **Initial Sequence Numbers** between client and server during connection establishment.
<!--SR:!2026-01-06,1,230-->

---

The ==ACK== flag **acknowledges** receipt and specifies the ==next expected sequence number==.
<!--SR:!2026-01-06,1,230!2026-01-06,1,230-->

---

The ==FIN== flag **gracefully terminates** TCP connections through a **four-way handshake**.
<!--SR:!2026-01-08,3,250-->

---

A **TCP connection** is identified by a ==4-tuple==: **Source IP**, **Source Port**, **Destination IP**, **Destination Port**.
<!--SR:!2026-01-06,1,230-->

---

The **three-way handshake** consists of ==SYN==, ==SYN-ACK==, and ==ACK== messages.
<!--SR:!2026-01-06,1,230!2026-01-06,1,230!2026-01-06,1,230-->

---

**Sequence numbers** are ==byte-level==, enabling TCP to detect **missing bytes** and **reorder** out-of-order packets.
<!--SR:!2026-01-06,1,230-->

---

The **TCP stream abstraction** uses ==sequence numbers==, ==ACKs==, and ==reordering logic== to hide **underlying packetization**.
<!--SR:!2026-01-08,3,250!2026-01-06,1,230!2026-01-06,1,230-->

---

**ISN randomization** prevents ==TCP sequence prediction attacks== that could lead to **connection hijacking**.
<!--SR:!2026-01-06,1,230-->
