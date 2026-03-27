# API Design — MOC

> Part of [[00 - IT Career - MOC]]
> Design robust, well-documented APIs

---

## Progress

- [ ] REST principles
- [ ] API versioning
- [ ] Error handling
- [ ] Documentation (OpenAPI)
- [ ] gRPC basics
- [ ] GraphQL basics

---

## Topics

### REST Fundamentals
- [ ] REST constraints (stateless, cacheable, uniform interface)
- [ ] Resource naming conventions
- [ ] HTTP methods semantics (GET, POST, PUT, PATCH, DELETE)
- [ ] Status codes (2xx, 3xx, 4xx, 5xx)
- [ ] Idempotency
- [ ] HATEOAS

### API Design Best Practices
- [ ] Resource-oriented design
- [ ] Consistent naming (plural nouns, kebab-case)
- [ ] Filtering, sorting, pagination
- [ ] Partial responses (field selection)
- [ ] Bulk operations
- [ ] Rate limiting headers
- [ ] API versioning strategies (URL, header, query param)

### Error Handling
- [ ] Standard error response format
- [ ] Problem Details (RFC 7807)
- [ ] Validation error responses
- [ ] Error codes and messages
- [ ] Localization

### Documentation
- [ ] OpenAPI / Swagger
- [ ] Springdoc OpenAPI
- [ ] API documentation best practices
- [ ] Examples and schemas
- [ ] Try-it-out functionality

### Authentication & Security
- [ ] API keys
- [ ] OAuth2 flows
- [ ] JWT tokens
- [ ] CORS
- [ ] Rate limiting
- [ ] Input validation

### gRPC
- [ ] Protocol Buffers (protobuf)
- [ ] Service definitions
- [ ] Unary vs streaming
- [ ] gRPC vs REST tradeoffs
- [ ] grpc-java and grpc-spring-boot-starter

### GraphQL
- [ ] Schema definition
- [ ] Queries and mutations
- [ ] Resolvers
- [ ] GraphQL vs REST
- [ ] When to use GraphQL
- [ ] graphql-java

---

## Russian Curriculum (Модуль 6)

### Межсервисное взаимодействие
- [ ] REST API
- [ ] gRPC
- [ ] GraphQL
- [ ] Message queues
- [ ] Event-driven architecture

---

## Project Tasks

**E-Commerce:** API implementation
- [ ] Design RESTful endpoints for all resources
- [ ] Implement OpenAPI documentation
- [ ] Add proper error responses
- [ ] Implement pagination for product listing
- [ ] Add API versioning (/v1/, /v2/)
- [ ] Consider gRPC for internal service communication

---

## Related
- [[Spring Ecosystem - MOC]]
- [[Distributed Systems - MOC]]
- [[00 - IT Career - MOC]]
