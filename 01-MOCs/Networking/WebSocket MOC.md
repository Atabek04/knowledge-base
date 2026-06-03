---
created: 2025-12-08
tags: [moc]
---

Full-duplex communication protocol for real-time applications over a single TCP connection. 
Covers WebSocket protocol mechanics, problem-solving capabilities, and comparisons with HTTP alternatives.

## Phase 1: Foundations

### Network Communication Basics
- Client-Server Communication Models
- HTTP Protocol Review
- TCP/IP Essentials

### WebSocket Fundamentals
- [[WebSocket maintains persistent TCP connection for bidirectional messaging|WebSocket: persistent TCP for bidirectional messaging]]
- [[HTTP request-response model prevents server-initiated data push|HTTP can't push server-initiated data]]
- [[Polling repeatedly requests updates to simulate real-time communication|Polling simulates real-time by repeated requests]]
- [[Persistent connections enable continuous bidirectional data flow|Persistent connections enable continuous bidirectional flow]]

### WebSocket vs HTTP
- [[HTTP Keep-Alive reuses TCP connections across multiple requests|HTTP Keep-Alive reuses TCP across requests]]

## Phase 2: Protocol Deep Dive

### Connection Establishment
- [[WebSocket upgrades HTTP connection to enable bidirectional communication|WebSocket upgrades an HTTP connection to go bidirectional]]
- [[HTTP and WebSocket both run over TCP using three-way handshake|HTTP and WebSocket both run over TCP]]
- [[WebSocket eliminates HTTP header overhead after initial handshake|WebSocket drops HTTP header overhead post-handshake]]
- [[WebSocket can't start directly without HTTP upgrade|WebSocket can't start without an HTTP upgrade]]
- [[WebSocket designed to reuse HTTP to be compatible and for deployment simplicity|WebSocket reuses HTTP for compatibility and deployment]]
- [[WebSocket piggybacking works, because initial request is valid|WebSocket piggybacks because the initial request is valid]]
- [[Designing WebSocket with its own port creates massive problems|A dedicated WebSocket port creates problems]]
- [[HTTP proxies operate in three modes for different traffic types|HTTP proxies operate in three modes]]

### Frame Structure
- [[WebSocket frames are binary data chunks, not HTTP requests|WebSocket frames are binary chunks, not HTTP]]
- [[Frame is the basic unit of WebSocket communication|Frame is the basic unit of WebSocket]]
- [[WebSocket frames use binary structure with opcodes and flags|Frame anatomy: FIN, opcode, MASK]]
- [[Masking is XORing the payload|Masking XORs the payload with a 32-bit key]]

### Connection Management
- [[WebSocket connection progresses through four lifecycle states|Four lifecycle states: CONNECTING, OPEN, CLOSING, CLOSED]]
- [[WebSocket readyState property tracks connection lifecycle phase|readyState tracks the lifecycle phase]]
- [[Ping-Pong frames detect dead connections and prevent timeouts|Ping-Pong frames detect dead connections]]
- [[WebSocket close handshake is for graceful shutdown|Close handshake = graceful shutdown]]
- [[WebSocket close status codes indicate termination reason|Close status codes (1000-1011) give the reason]]

## Phase 3: Implementation

### Client-Side WebSockets
- [[Browser WebSocket API is JS interface to create and manage connections|Browser WebSocket API manages connections]]
- [[WebSocket has four event handlers|Four event handlers: onopen, onmessage, onerror, onclose]]
- [[WebSocket send method transmits text and binary data|send() transmits text and binary (JSON, ArrayBuffer, Blob)]]

### Server-Side WebSockets
- [[Server stores WebSocket connections because it cannot initiate connections to clients|Server stores connections; it can't initiate to clients]]
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

## External Resources

- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [RFC 6455 - The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)
