---
created: 2025-12-08
tags: [moc]
---

Concepts for understanding network communication patterns, protocols, and real-time data exchange. Covers communication fundamentals, TCP protocol details, HTTP protocol features, and WebSocket for bidirectional communication.

## Communication Patterns

- [[Request-response communication requires new requests for each data exchange|Request-response needs a new request per exchange]]
- [[Persistent connections enable continuous bidirectional data flow|Persistent connections enable continuous bidirectional flow]]
- [[HTTP request-response model prevents server-initiated data push|HTTP can't push server-initiated data]]
- [[Polling repeatedly requests updates to simulate real-time communication|Polling simulates real-time by repeated requests]]

## OSI Model Layers

### Layer 1: Physical
- [[Physical Layer encodes bits as electrical optical or radio signals|L1 Physical: bits as electrical/optical/radio signals]]

### Layer 2: Data Link
- [[Data Link Layer encapsulates packets into frames with MAC headers|L2 Data Link: packets into frames with MAC headers]]
- [[MAC address is a permanent 48-bit identifier burned into network hardware|MAC address: permanent 48-bit hardware ID]]
- [[Frame Check Sequence detects corrupted frames using checksum comparison|Frame Check Sequence detects corruption via checksum]]

### Layer 3: Network
- [[Network Layer wraps segments into packets by adding IP addresses|L3 Network: segments into packets with IP addresses]]
- [[IP addresses flow hierarchically from IANA through RIRs and ISPs|IP allocation flows IANA → RIRs → ISPs]]
- [[Routers have private IP for LAN and public IP for internet|Routers: private LAN IP, public internet IP (NAT)]]

### Layer 4: Transport
- [[Transport Layer breaks data into segments with TCP headers|L4 Transport: data into segments with TCP headers]]
- [[TCP provides reliable ordered error-checked data delivery over networks|TCP: reliable, ordered, error-checked delivery]]

## Protocol Foundations

- [[HTTP and WebSocket both run over TCP using three-way handshake|HTTP and WebSocket both run over TCP]]

## TCP Protocol Deep Dive

- [[TCP MOC]] — detailed navigation for TCP fundamentals

## HTTP Protocol

- [[HTTP Keep-Alive reuses TCP connections across multiple requests|HTTP Keep-Alive reuses TCP across requests]]

## WebSocket Protocol

- [[WebSocket MOC]] — detailed navigation for WebSocket specifics

## Network Devices

- [[Switches forward frames within a LAN by reading MAC addresses|Switches forward frames by MAC within a LAN]]
- [[Home router combines router switch and wireless access point|Home router = router + switch + access point]]

## Connection Management

- [[Connection pooling reuses connections at application level to reduce overhead|Connection pooling reuses connections to cut overhead]]

## Practice

- [[Networking|04-Flashcards/Networking]] — spaced repetition cards for communication patterns
- [[TCP|04-Flashcards/TCP]] — spaced repetition cards for TCP protocol fundamentals
- [[WebSocket Flashcards|04-Flashcards/WebSocket]] — spaced repetition cards for WebSocket protocol

## External Resources

- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [RFC 6455 - The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)
- [RFC 793 - TCP Specification](https://datatracker.ietf.org/doc/html/rfc793)
- [TCP/IP Illustrated, Vol. 1](https://www.amazon.com/TCP-Illustrated-Vol-Addison-Wesley-Professional/dp/0201633469)
