---
created: 2025-12-08
tags: [flashcards/tcp]
---

# TCP Flashcards

What does **TCP** stand for and what are its three key guarantees?
**TCP** stands for **Transmission Control Protocol**. Its three guarantees are: **reliability** (data arrives), **ordering** (data arrives in sequence), and **error-checking** (corruption detection and recovery).

---

What is the **TCP three-way handshake** and what sequence of flags does it use?
The three-way handshake establishes a connection: **Step 1 (SYN):** Client sends SYN with sequence number X. **Step 2 (SYN-ACK):** Server responds with ACK=X+1 and its own sequence Y. **Step 3 (ACK):** Client sends ACK=Y+1. Both sides now know each other's starting sequence numbers.

---

What does **SYN** stand for and what is its primary purpose?
**SYN** stands for **"Synchronize."** Its purpose is to **synchronize the Initial Sequence Numbers (ISN)** between two hosts so both sides know the starting point for the other side's data stream.

---

What does **ACK** stand for and what does **ACK=X+1** mean?
**ACK** stands for **"Acknowledgment."** It confirms receipt of data. **ACK=X+1** means "I received your data ending at sequence X (adding 1 because SYN consumes one sequence number), and I'm expecting the next byte to start at sequence X+1."

---

What does **FIN** stand for and what is its purpose?
**FIN** stands for **"Finish."** It signals that a host has no more data to send and wants to close the connection gracefully. Unlike abruptly dropping the connection, FIN allows both sides to acknowledge closure.

---

What is a **TCP sequence number** and why is it needed?
A **sequence number** is attached to each byte of data. TCP needs sequence numbers for three reasons: **ordering** (reorder out-of-order packets), **completeness** (detect missing data), and **duplicate detection** (ignore duplicate packets).

---

Does **TCP** use ==packet-level== or ==byte-level== sequence numbers?
TCP uses ==byte-level== sequence numbers. Each individual byte gets its own number, not each packet.

---

What is a **packet** in network communication?
A **packet** is a chunk of data transmitted over the network. Large data is broken into smaller packets based on the **Maximum Transmission Unit (MTU)**. Each packet contains a header (source/dest/sequence) and payload (actual data).

---

What is the **Maximum Transmission Unit (MTU)** and what is a typical size?
The **MTU** is the maximum size a packet can be (~==1500 bytes== typical). Headers take ~==40 bytes==, leaving ~==1460 bytes== for payload. Larger data is split across multiple packets.

---

What is the difference between **stream-oriented** (TCP) and **message-oriented** (UDP) protocols?
**Stream-oriented (TCP):** Data is continuous bytes with no boundaries. Messages don't preserve boundaries. **Message-oriented (UDP):** Data is discrete messages with preserved boundaries. However, UDP has no reliability guarantees.

---

How does the **TCP stream abstraction** work?
TCP presents data as a ==continuous== byte flow to applications. Underneath, it breaks data into packets that travel independently and possibly arrive out of order. TCP uses sequence numbers, acknowledgments, and reordering to make the packetized reality look like a continuous stream.

---

Why does **TCP use random Initial Sequence Numbers (ISN)**?
Random ISN ==prevents sequence prediction attacks== where attackers might guess the next connection's ISN and inject forged data. Randomness makes each connection's starting point unpredictable.

---

What is ==reliability== in TCP?
==Reliability== means ==data arrives==. TCP automatically retransmits lost packets.

---

What is ==ordering== in TCP?
==Ordering== means ==data arrives== in the same ==sequence== it was sent. TCP reorders out-of-order packets before delivering to the application.

---

What is ==error-checking== in TCP?
==Error-checking== means TCP ==detects== and ==recovers== from corrupted data.

---

SYN ==synchronizes== Initial Sequence Numbers between hosts.

---

ACK indicates the ==next sequence number== the receiver is expecting.

---

FIN signals ==no more data== and initiates graceful ==connection closure==.

---
