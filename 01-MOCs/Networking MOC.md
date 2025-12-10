---
created: 2025-12-08
tags: [moc]
---

# Networking MOC

Concepts for understanding network communication patterns, protocols, and real-time data exchange. Covers communication fundamentals, TCP protocol details, HTTP protocol features, and WebSocket for bidirectional communication.

## Communication Patterns

- [[Request-response communication requires new requests for each data exchange]] — traditional client-server model with independent interactions
- [[Persistent connections enable continuous bidirectional data flow]] — always-open connections for real-time communication
- [[HTTP request-response model prevents server-initiated data push]] — why HTTP can't efficiently push updates
- [[Polling repeatedly requests updates to simulate real-time communication]] — inefficient pattern for real-time scenarios

## Protocol Foundations

- [[TCP provides reliable ordered error-checked data delivery over networks]] — transport layer protocol fundamentals
- [[HTTP and WebSocket both run over TCP using three-way handshake]] — shared TCP foundation for different protocols

## TCP Protocol Deep Dive

- [[TCP MOC]] — detailed navigation for TCP fundamentals

## HTTP Protocol

- [[HTTP Keep-Alive reuses TCP connections across multiple requests]] — connection reuse in HTTP/1.1

## WebSocket Protocol

- [[WebSocket MOC]] — detailed navigation for WebSocket specifics

## Connection Management

- [[Connection pooling reuses connections at application level to reduce overhead]] — application-level connection reuse patterns

## Practice

- [[Networking|04-Flashcards/Networking]] — spaced repetition cards for communication patterns
- [[TCP|04-Flashcards/TCP]] — spaced repetition cards for TCP protocol fundamentals
- [[WebSocket|04-Flashcards/WebSocket]] — spaced repetition cards for WebSocket protocol

## External Resources

- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [RFC 6455 - The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)
- [RFC 793 - TCP Specification](https://datatracker.ietf.org/doc/html/rfc793)
- [TCP/IP Illustrated, Vol. 1](https://www.amazon.com/TCP-Illustrated-Vol-Addison-Wesley-Professional/dp/0201633469)
