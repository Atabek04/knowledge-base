---
created: 2025-12-08
tags: [moc]
---

# WebSocket MOC

Full-duplex communication protocol for real-time applications over a single TCP connection. 
Covers WebSocket protocol mechanics, problem-solving capabilities, and comparisons with HTTP alternatives.

## Phase 1: Foundations

### Network Communication Basics
- Client-Server Communication Models
- HTTP Protocol Review
- TCP/IP Essentials

### WebSocket Fundamentals
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]] — persistent bidirectional communication + use cases
- [[HTTP request-response model prevents server-initiated data push]] — problem that WebSocket solves
- [[Polling repeatedly requests updates to simulate real-time communication]] — inefficient pattern WebSocket replaces
- [[Persistent connections enable continuous bidirectional data flow]] — connection pattern that enables real-time updates

### WebSocket vs HTTP
- [[HTTP Keep-Alive reuses TCP connections across multiple requests]] — HTTP/1.1 connection reuse vs WebSocket bidirectionality

## Phase 2: Protocol Deep Dive

### Connection Establishment
- [[WebSocket upgrades HTTP connection to enable bidirectional communication]] — upgrade handshake and protocol switching
- [[HTTP and WebSocket both run over TCP using three-way handshake]] — TCP foundation and connection establishment
- [[WebSocket eliminates HTTP header overhead after initial handshake]] — efficiency benefit over HTTP Keep-Alive
- [[WebSocket can't start directly without HTTP upgrade]] — why HTTP upgrade is required
- [[WebSocket designed to reuse HTTP to be compatible and for deployment simplicity]] — design rationale
- [[WebSocket piggybacking works, because initial request is valid]] — proxy compatibility mechanism
- [[Designing WebSocket with its own port creates massive problems]] — alternative design trade-offs
- [[HTTP proxies operate in three modes for different traffic types]] — proxy behavior during upgrade

### Frame Structure
- [[WebSocket frames are binary data chunks, not HTTP requests]] — post-upgrade data format
- [[Frame is the basic unit of WebSocket communication]] — frame vs HTTP message
- [[WebSocket frames use binary structure with opcodes and flags]] — binary frame anatomy with FIN, opcode, MASK
- [[Masking is XORing the payload]] — masking algorithm with 32-bit key

### Connection Management
- [[WebSocket connection progresses through four lifecycle states]] — CONNECTING, OPEN, CLOSING, CLOSED
- [[WebSocket readyState property tracks connection lifecycle phase]] — checking current state
- [[Ping-Pong frames detect dead connections and prevent timeouts]] — heartbeat mechanism
- [[WebSocket close handshake is for graceful shutdown]] — graceful termination protocol
- [[WebSocket close status codes indicate termination reason]] — standard status codes (1000-1011)

## Phase 3: Implementation

### Client-Side WebSockets
- [[Browser WebSocket API is JS interface to create and manage connections]] — creating WebSocket instances
- [[WebSocket has four event handlers]] — onopen, onmessage, onerror, onclose
- [[WebSocket send method transmits text and binary data]] — sending strings, JSON, ArrayBuffer, Blob

### Server-Side WebSockets
- [[Server stores WebSocket connections because it cannot initiate connections to clients]] — why and how to manage client connections
- Scaling Considerations
- Load Balancing

## Phase 4: Advanced Topics

### Security
- WSS (WebSocket Secure)
- Authentication & Authorization
- Common Vulnerabilities

### Performance & Optimization
- Message Compression
- Backpressure Handling
- Resource Management

### Real-World Patterns
- Reconnection Strategies
- Message Queuing
- Broadcasting Patterns

## Relationships

- [[Networking MOC]] — parent navigation hub for all networking concepts

## Practice

- [[WebSocket Flashcards|04-Flashcards/WebSocket]] — spaced repetition cards for WebSocket protocol

## External Resources

- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [RFC 6455 - The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)
