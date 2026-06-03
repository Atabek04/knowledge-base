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
- [ ] Richardson Maturity Model
- [ ] Resource naming conventions
- [ ] HTTP methods semantics (GET, POST, PUT, PATCH, DELETE)
- [ ] Status codes (2xx, 3xx, 4xx, 5xx)
- [[Idempotency key prevents duplicate processing when clients retry failed requests|Idempotency key dedupes client retries]]
- [ ] HATEOAS
- [[Content-Type header tells receiver how to parse the HTTP body|Content-Type tells the receiver how to parse the body]]
- [[Content-Type common values grouped by purpose|Content-Type common values by purpose]]

### API Design Best Practices
- [ ] Resource-oriented design
- [ ] Consistent naming (plural nouns, kebab-case)
- [ ] Filtering, sorting, pagination
- [[Offset pagination slows at deep pages because the database scans and discards skipped rows|Offset pagination slows at deep pages]]
- [[Keyset pagination filters by the last seen key for stable performance at any depth|Keyset pagination: stable performance at any depth]]
- [[Cursor pagination hides the paging position inside an opaque token|Cursor pagination hides position in an opaque token]]
- [ ] Partial responses (field selection)
- [[Sparse fieldsets let clients request only needed fields reducing payload size|Sparse fieldsets (?fields=) cut payload size]]
- [[PATCH with JsonMergePatch updates only the fields present in the request leaving others unchanged|PATCH JsonMergePatch updates only sent fields (RFC 7396)]]
- [ ] Bulk operations
- [ ] Rate limiting headers
- [ ] API versioning strategies (URL, header, query param)
- [[ETag header enables optimistic concurrency by rejecting updates based on stale resource versions|ETag enables optimistic concurrency (If-Match / 412)]]

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
- [[CORS relaxes Same-Origin Policy to allow controlled cross-origin browser requests|CORS relaxes Same-Origin Policy for cross-origin requests]]
- [[CORS preflight uses OPTIONS request to authorize non-simple cross-origin calls|CORS preflight: OPTIONS authorizes non-simple calls]]
- [[Browser sends Origin header on cross-origin requests and on non-simple same-origin requests|Browser sends Origin on cross-origin (and non-simple) requests]]
- [ ] Rate limiting
- [ ] Input validation

### gRPC
- [ ] Protocol Buffers (protobuf)
- [ ] Service definitions
- [ ] Unary vs streaming
- [ ] gRPC vs REST tradeoffs
- [ ] grpc-java and grpc-spring-boot-starter
- [ ] Deadlines, retries, and interceptors
- [ ] Health checks and reflection

### GraphQL
- [ ] Schema definition
- [ ] Queries and mutations
- [ ] Resolvers
- [ ] GraphQL vs REST
- [ ] When to use GraphQL
- [ ] graphql-java
- [ ] Schema-first vs code-first
- [ ] Subscriptions
- [ ] DataLoader — N+1 problem in GraphQL
- [ ] Spring for GraphQL

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
- [[Security - MOC]]
