---
created: 2025-12-08
tags: [moc]
---

Transmission Control Protocol — reliable, ordered, and error-checked data delivery. Deep dive into TCP protocol mechanics including connection establishment, data transmission, and stream abstraction.

## Fundamentals

- [[TCP provides reliable ordered error-checked data delivery over networks|TCP: reliable, ordered, error-checked delivery]]
- [[Single port handles multiple TCP connections via unique socket tuples|One port, many connections via socket tuples]]

## Connection Lifecycle

- [[TCP three-way handshake establishes connection with SYN-SYN-ACK-ACK|Three-way handshake: SYN, SYN-ACK, ACK]]
- [[SYN synchronizes Initial Sequence Numbers between hosts|SYN synchronizes Initial Sequence Numbers]]
- [[ACK acknowledges receipt and specifies next expected sequence number|ACK confirms receipt, names the next sequence]]
- [[FIN terminates TCP connections through graceful shutdown handshake|FIN gracefully terminates the connection]]
- [[Either side can initiate TCP connection termination with FIN|Either side can initiate FIN termination]]
- [[HTTP Keep-Alive prevents FIN signal to reuse TCP connection|Keep-Alive suppresses FIN to reuse the connection]]

## Data Transmission

- [[TCP sequence numbers track individual bytes for ordering and completeness|Sequence numbers track bytes for ordering]]
- [[TCP packets carry data chunks with headers and payload|Packets carry header + payload chunks]]
- [[Maximum Transmission Unit limits packet size on network links|MTU limits packet size on a link]]

## Stream Abstraction

- [[TCP stream abstraction hides packetization from applications|Stream abstraction hides packetization]]
- [[UDP preserves message boundaries unlike TCP streams|UDP preserves message boundaries (unlike TCP)]]

## Security

- [[Initial Sequence Number randomization prevents TCP sequence prediction attacks|ISN randomization blocks sequence-prediction attacks]]

## Higher-Level Protocols

- [[HTTP and WebSocket both run over TCP using three-way handshake|HTTP and WebSocket both run over TCP]]

## Relationships

- [[Networking MOC]] — parent navigation hub for all networking concepts

## Practice

- [[TCP|04-Flashcards/TCP]] — spaced repetition cards for TCP fundamentals

## External Resources

- [RFC 793 - Transmission Control Protocol](https://datatracker.ietf.org/doc/html/rfc793)
- [TCP/IP Guide - TCP Specification](http://www.tcpipguide.com/free/t_TCPIPTransmissionControlProtocolTCP.htm)
