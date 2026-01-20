---
created: 2025-12-08
tags: [moc]
---

# TCP MOC

Transmission Control Protocol — reliable, ordered, and error-checked data delivery. Deep dive into TCP protocol mechanics including connection establishment, data transmission, and stream abstraction.

## Fundamentals

- [[TCP provides reliable ordered error-checked data delivery over networks]] — what TCP is and its three key guarantees
- [[Single port handles multiple TCP connections via unique socket tuples]] — port multiplexing and connection identification

## Connection Lifecycle

- [[TCP three-way handshake establishes connection with SYN-SYN-ACK-ACK]] — connection establishment process with synchronization
- [[SYN synchronizes Initial Sequence Numbers between hosts]] — SYN flag explained
- [[ACK acknowledges receipt and specifies next expected sequence number]] — ACK flag explained
- [[FIN terminates TCP connections through graceful shutdown handshake]] — connection termination with graceful closure
- [[Either side can initiate TCP connection termination with FIN]] — bidirectional termination capability
- [[HTTP Keep-Alive prevents FIN signal to reuse TCP connection]] — Keep-Alive mechanics and connection reuse

## Data Transmission

- [[TCP sequence numbers track individual bytes for ordering and completeness]] — byte-level numbering for data integrity
- [[TCP packets carry data chunks with headers and payload]] — packet structure and data segmentation
- [[Maximum Transmission Unit limits packet size on network links]] — MTU constraints and data splitting

## Stream Abstraction

- [[TCP stream abstraction hides packetization from applications]] — stream-oriented protocol concept
- [[UDP preserves message boundaries unlike TCP streams]] — stream-oriented vs message-oriented comparison

## Security

- [[Initial Sequence Number randomization prevents TCP sequence prediction attacks]] — ISN randomization for security

## Higher-Level Protocols

- [[HTTP and WebSocket both run over TCP using three-way handshake]] — protocols built on top of TCP foundation

## Relationships

- [[Networking MOC]] — parent navigation hub for all networking concepts

## Practice

- [[TCP|04-Flashcards/TCP]] — spaced repetition cards for TCP fundamentals

## External Resources

- [RFC 793 - Transmission Control Protocol](https://datatracker.ietf.org/doc/html/rfc793)
- [TCP/IP Guide - TCP Specification](http://www.tcpipguide.com/free/t_TCPIPTransmissionControlProtocolTCP.htm)
