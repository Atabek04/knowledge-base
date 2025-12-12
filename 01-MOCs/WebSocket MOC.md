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
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]] — core concept of persistent bidirectional communication
- [[WebSocket protocol enables real-time applications through persistent connections]] — high-level overview and use cases
- [[HTTP request-response model prevents server-initiated data push]] — problem that WebSocket solves
- [[WebSocket eliminates polling by enabling server push]] — replacing inefficient polling patterns
- [[Persistent connections enable continuous bidirectional data flow]] — connection pattern that enables real-time updates

### WebSocket vs HTTP
- [[HTTP Keep-Alive reuses TCP connections across multiple requests]] — HTTP/1.1 connection reuse vs WebSocket bidirectionality
- [[Polling repeatedly requests updates to simulate real-time communication]] — what WebSocket replaces

## Phase 2: Protocol Deep Dive

### Connection Establishment
- [[WebSocket upgrades HTTP connection to enable bidirectional communication]] — upgrade handshake and protocol switching
- [[HTTP and WebSocket both run over TCP using three-way handshake]] — TCP foundation and connection establishment
- [[WebSocket eliminates HTTP header overhead after initial handshake]] — efficiency benefit over HTTP Keep-Alive
- Upgrade Headers
- Protocol Negotiation

### Frame Structure
- Frame Anatomy
- Opcodes and Control Frames
- Masking and Security

### Connection Management
- Ping/Pong Mechanism
- Close Handshake
- Connection States

## Phase 3: Implementation

### Client-Side WebSockets
- Browser WebSocket API
- Event Handling
- Error Management

### Server-Side WebSockets
- Server Implementation Patterns
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

- [[WebSocket|04-Flashcards/WebSocket]] — spaced repetition cards for WebSocket protocol

## External Resources

- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [RFC 6455 - The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)
