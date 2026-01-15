---
created: 2025-12-30
tags: [flashcards/networking]
---

# Networking Flashcards

Comprehensive flashcards for networking concepts from the Networking MOC. Covers communication patterns, OSI model layers, network devices, and connection management.

---

## Communication Patterns

What is the difference between request-response communication and persistent connection communication?
?
**Request-response:** Client **initiates** a request, server **responds**, connection **closes** (or pools for reuse). Each interaction is **independent** and follows a **lifecycle**: establish → request → response → close.

**Persistent connection:** Connection stays **open continuously**. Either party can send data **anytime** without initiating a new request. Enables **true real-time** bidirectional communication.

---

---

Why does HTTP's request-response model prevent server-initiated data push?
?
HTTP is fundamentally built on **client-initiated requests**. The server can **only respond** to requests it receives — it cannot **send data** unless the client asks first. This is an **architectural constraint**, not a bug. The protocol was designed for **document retrieval**, not real-time bidirectional scenarios.

---

What problem does polling solve, and why is it inefficient?
?
**Polling** allows clients to simulate real-time updates by **repeatedly asking** the server "do you have updates?" at fixed intervals. 
This is inefficient because: 
(1) **Wasted requests** — most polls return "no new data"; 
(2) **Latency** — client waits for next poll interval to get updates; 
(3) **Scalability** — thousands of clients polling = thousands of unnecessary connections; 
(4) **Battery drain** — mobile devices constantly request.

**WebSocket eliminates polling** by using persistent connections where the server **pushes updates immediately**.

---

How do persistent connections enable real-time communication?
?
Persistent connections keep the **TCP connection open continuously** instead of closing after each exchange. This allows **either party** (client or server) to send data **anytime** without establishing a new connection. The **connection costs** (three-way handshake, setup overhead) are paid **once** instead of repeatedly. Data flows **bidirectionally** in real-time as needed.

---

## OSI Model - Layer 1: Physical

How does the Physical Layer encode bits for transmission?
?
The **Physical Layer** converts **digital bits** into **physical signals** suitable for different media:

**Copper cables:** Uses **voltage levels** (e.g., high voltage = 1, low = 0) with encoding schemes like **NRZ** (Non-Return to Zero) or **Manchester encoding**.

**Fiber optic cables:** Uses **light pulses** transmitted via **LED** or **laser**.

**Wireless:** Uses **radio wave modulation** (frequency/amplitude variations) to represent bits.

All three encoding methods transmit the **same digital data** in different physical forms.
<!--SR:!2026-01-06,1,235-->

---

---

## OSI Model - Layer 2: Data Link

How does the Data Link Layer encapsulate data?
?
The **Data Link Layer** wraps **packets** (from Layer 3) into **frames** by adding **headers and trailers**:

**Structure:** [MAC header] + [payload/packet] + [Frame Check Sequence (FCS)]

**MAC header** contains **source and destination MAC addresses** for local network forwarding.

**FCS trailer** contains a **checksum** to detect frame corruption.

The combination of all three creates a **frame** ready for transmission on the local network.

---

---

What is a MAC address and what purpose does it serve?
?
A **MAC address** (Media Access Control) is a **permanent 48-bit identifier** burned into network hardware during manufacturing. Format: **AA:BB:CC:DD:EE:FF** (six pairs of hexadecimal digits).

**Characteristics:** **Non-configurable**, **unique per network interface** (NIC), used for **local network communication** only.

**Purpose:** Identifies devices on the **same LAN** for **Layer 2 switching**. Routers use **IP addresses** for inter-network routing, but switches use **MAC addresses** for local forwarding.

---

---

Why does the Data Link Layer use Frame Check Sequence?
?
**Frame Check Sequence (FCS)** is a **checksum** calculated by the sender and appended to each frame. The **receiver recalculates** the checksum and **compares** it to the received FCS.

**Purpose:** Detects **corrupted frames** caused by electrical interference, noise, or signal degradation.

**Important limitation:** FCS **detects errors but doesn't correct them**. If a frame is corrupted, it is **discarded**. **Higher layers** (TCP) request **retransmission** of lost frames.

---

---

## OSI Model - Layer 3: Network

How does the Network Layer create packets?
?
The **Network Layer** wraps **segments** (from Layer 4 / TCP) into **packets** by adding **IP headers** containing:

**Source IP address:** Where the data originates.

**Destination IP address:** Where the data should go.

The **combination of segment + IP headers = packet**.

**Packets are routable** across the **internet** because routers examine **IP addresses** to forward packets toward their destination.

---

---

How do IP addresses flow hierarchically from IANA to individual networks?
?
IP allocation follows a **hierarchical structure**:

**IANA** (Internet Assigned Numbers Authority) manages the **global IP address space**.

**IANA → RIRs** (Regional Internet Registries) → **RIRs → ISPs** (Internet Service Providers) → **Your router** → Devices on your LAN.

Each level **subdivides** the address space and allocates **blocks** to the next level. This **hierarchical structure** enables **efficient routing** — routers only need to know routes to **networks**, not individual devices.

---

---

What is the difference between private and public IP addresses, and how does NAT relate to them?
?
**Public IP addresses** are **globally unique** across the internet, assigned by your ISP, and used for **internet-facing** communication. Example: your home router's external IP.

**Private IP addresses** are **reusable** within local networks (e.g., 192.168.1.0-192.168.1.255), not routable on the internet. All devices on your home LAN typically use private IPs.

**NAT (Network Address Translation)** allows **multiple private IPs** to share a **single public IP**. Your router maintains a **NAT table** mapping private addresses to the public IP, translating outgoing requests and routing responses back to the correct device.

---

---

## OSI Model - Layer 4: Transport

How does the Transport Layer segment data and add TCP headers?
?
The **Transport Layer** breaks **large application data** into manageable **segments** based on **Maximum Segment Size (MSS)** (typically ~1460 bytes, accounting for TCP/IP headers).

Each **segment** includes a **TCP header** with:

**Source and destination port numbers** (identify processes/services).

**Sequence numbers** (track individual bytes for ordering).

**Flags** (SYN, ACK, FIN — control connection state).

**Checksum** (error detection).

The **result is called a segment** (for TCP) or **datagram** (for UDP). On the receiving side, TCP **reassembles** segments in the **correct order** using sequence numbers.

---

---

## Network Devices

How do switches differ from routers?
?
**Switches:**
- **Layer 2** (Data Link) devices.
- Forward frames **within a LAN** by reading **MAC addresses**.
- Maintain a **MAC address table** (port → MAC mapping).
- All ports are on the **same network** (same IP subnet).
- Forward frames **only to the specific destination port**.

**Routers:**
- **Layer 3** (Network) devices.
- Forward packets **between different networks** by reading **IP addresses**.
- Maintain a **routing table** (network → next-hop mapping).
- Connect **different networks** with **different IP subnets**.
- Forward packets toward the **destination network**.

**Summary:** Switch = MAC within LAN; Router = IP between networks.

---

---

What does a home router do?
?
A **home router** is a **combo device** combining three functions:

**Router (Layer 3):** Reads **IP addresses**, forwards packets between your **LAN** and the **internet** (ISP connection).

**Switch (Layer 2):** Provides multiple **Ethernet ports**, uses **MAC addresses** to forward frames **within your LAN**.

**Wireless Access Point (AP):** Broadcasts **Wi-Fi signal** allowing **wireless devices** to connect to the **LAN** without Ethernet cables.

A single ISP box provides all three: **routing between networks**, **switching within LAN**, and **wireless connectivity**.

---

---

## Connection Management

What is connection pooling and why do applications use it?
?
**Connection pooling** is an **application-level pattern** that maintains a **pool of reusable connections** instead of creating new connections for each request.

**Process:** (1) **Borrow** a connection from the pool; (2) **Use** it for a request; (3) **Return** it to the pool.

**Examples:** **HikariCP** for database connections, **Apache HttpClient** for HTTP connections.

**Benefits:** Avoids **expensive connection setup** (three-way handshake, authentication, resource allocation). Improves **application performance** by reusing established connections.

**Note:** Connection pooling is **application-level**. **HTTP Keep-Alive** (covered below) is **protocol-level** connection reuse.

---

---

How does HTTP Keep-Alive enable connection reuse?
?
**HTTP Keep-Alive** is an **HTTP/1.1 feature** that prevents the server from sending a **FIN** (termination) signal after responding. The **Connection header** (default: Keep-Alive in HTTP/1.1) signals the connection should remain open.

**Without Keep-Alive:** Each request requires a **new TCP three-way handshake** (expensive setup).

**With Keep-Alive:** The **same TCP connection** is reused for **multiple HTTP requests** to the **same server**. The connection only closes due to **timeout** or explicit close.

**Trade-off:** Improves performance for same-server requests, but the connection eventually closes, and the server must manage **connection limits**.
<!--SR:!2026-01-06,1,235-->

---

---

## Protocol Foundations

How are HTTP and WebSocket similar at the network level?
?
Both **HTTP** and **WebSocket** share the **same TCP foundation**:

(1) Both establish connections using **TCP's three-way handshake**.

(2) Both send data over the **same TCP connection**.

Think of **TCP as the highway**, and **HTTP/WebSocket as traffic rules**.

**Where they differ:**

**HTTP:** **Request-response** protocol with **HTTP headers and methods** (GET, POST). Server **cannot initiate** communication.

**WebSocket:** Starts as **HTTP upgrade handshake**, then switches to **WebSocket protocol** with **frames** (not HTTP messages). Enables **bidirectional** communication.

The difference emerges **after connection establishment** — same TCP foundation, different protocols and communication patterns.
<!--SR:!2026-01-06,1,235-->

---

---

## Cloze Drilling: Essential Terminology

The ==Physical== Layer converts bits into **electrical**, **optical**, or **radio signals**.

---

A **MAC address** is a ==permanent 48-bit identifier== in format ==AA:BB:CC:DD:EE:FF== burned into network hardware.

---

The ==Data Link== Layer adds ==MAC address headers== and ==Frame Check Sequence== to create **frames**.
<!--SR:!2026-01-08,3,255!2000-01-01,1,250!2000-01-01,1,250-->

---

The ==Network== Layer adds **IP addresses** to create **packets** for routing across networks.

---

The ==Transport== Layer breaks data into **segments** with ==TCP headers== containing **port numbers**, **sequence numbers**, and **flags**.

---

**Switches** use ==MAC addresses== for **Layer 2** forwarding; **routers** use ==IP addresses== for **Layer 3** forwarding.

---

**HTTP Keep-Alive** prevents the ==FIN== signal to reuse the **TCP connection** across **multiple HTTP requests**.
