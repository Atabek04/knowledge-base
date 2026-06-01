# Spring Ecosystem — MOC

> **Phase 4** of [[00 - IT Career - MOC]]
> Master the Spring Framework

---

## Progress

- [ ] Spring Core (DI, IoC, AOP)
- [ ] Spring Boot
- [ ] Spring Data JPA
- [ ] Spring Web (REST APIs)
- [ ] Spring Validation
- [ ] Spring Security

---

## Topics

### Spring Core
- [ ] Inversion of Control (IoC) container
- [ ] Dependency Injection (constructor, setter, field)
- [ ] Bean lifecycle
- [ ] Bean scopes (singleton, prototype, request, session)
- [ ] @Component, @Service, @Repository, @Controller
- [ ] @Configuration and @Bean
- [ ] @Autowired and @Qualifier
- [ ] Profiles (@Profile)
- [ ] Properties and @Value
- [ ] SpEL (Spring Expression Language)

### Aspect-Oriented Programming (AOP)
- [ ] Cross-cutting concerns
- [ ] Aspects, Join points, Pointcuts
- [ ] Advice types (@Before, @After, @Around)
- [ ] @Aspect and @EnableAspectJAutoProxy
- [ ] Logging, security, transaction aspects

### Spring Boot
- [ ] Auto-configuration
- [ ] Starters
- [ ] application.properties / application.yml
- [ ] @SpringBootApplication
- [ ] Actuator endpoints
- [ ] Health checks
- [ ] Custom configuration properties (@ConfigurationProperties)
- [ ] Embedded servers

### Spring Data JPA
- [ ] Repository interfaces (JpaRepository, CrudRepository)
- [ ] Query methods (findBy, countBy, existsBy)
- [ ] @Query annotation (JPQL, native)
- [ ] Pagination and sorting
- [ ] Specifications for dynamic queries
- [ ] Auditing (@CreatedDate, @LastModifiedDate)
- [ ] Custom repository implementations

### Spring Web (REST APIs)
- [ ] @RestController and @RequestMapping
- [ ] HTTP methods (@GetMapping, @PostMapping, etc.)
- [ ] @PathVariable, @RequestParam, @RequestBody
- [ ] Response entities and status codes
- [ ] Exception handling (@ExceptionHandler, @ControllerAdvice)
- [ ] Request/Response DTOs
- [ ] Content negotiation
- [ ] CORS configuration
- [[Spring SseEmitter and Flux ServerSentEvent hold response open like FastAPI StreamingResponse]] — SSE streaming: imperative (SseEmitter) vs reactive (Flux)

### Spring Validation
- [ ] Bean Validation (JSR-380)
- [ ] @Valid and @Validated
- [ ] Built-in constraints (@NotNull, @Size, @Email, etc.)
- [ ] Custom validators
- [ ] Validation groups
- [ ] Error handling and messages

### Spring Security
- [ ] Authentication vs Authorization
- [ ] SecurityFilterChain
- [ ] UserDetailsService
- [ ] Password encoding (BCrypt)
- [ ] JWT authentication
- [ ] OAuth2 / OIDC basics
- [ ] Method security (@PreAuthorize, @Secured)
- [ ] CORS and CSRF
- [ ] Role-based access control

### Spring Cloud (Microservices)
- [ ] Spring Cloud Config
- [ ] Spring Cloud Gateway
- [ ] Service Discovery (Eureka)
- [ ] Load balancing
- [ ] Circuit breaker integration
- [ ] Distributed tracing (Sleuth/Micrometer)

---

## Russian Curriculum (Модуль 10)

### Безопасность
- [ ] Аутентификация и авторизация
- [ ] OAuth 2.0 / OIDC
- [ ] JWT tokens
- [ ] Защита API

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Spring in Action** — Craig Walls | 🔴 Critical | ⏳ |
| **Spring Security in Action** — Manning | 🟡 Important | ⏳ |

---

## Project Tasks

**E-Commerce Stage 1-4:**
- [ ] Set up Spring Boot project with dependencies
- [ ] Configure PostgreSQL connection
- [ ] Implement REST endpoints for products
- [ ] Add validation for product creation/updates
- [ ] Implement user registration and login
- [ ] Add JWT authentication
- [ ] Secure endpoints with role-based access

---

## Related
- [[Java MOC]]
- [[Databases - MOC]]
- [[API Design - MOC]]
- [[00 - IT Career - MOC]]
