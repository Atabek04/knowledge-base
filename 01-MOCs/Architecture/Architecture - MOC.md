> Build maintainable, scalable systems

---

## Progress

- [ ] Clean Code principles
- [ ] Refactoring
- [ ] Enterprise patterns
- [ ] Monolith → Modular Monolith
- [ ] Microservices introduction
- [ ] DDD basics

---

## Topics

### Reliability

- [[A fault is a component deviating from spec while a failure is the system no longer serving users|Fault vs failure — you engineer the arrow between them, not the fault rate]]
- [[Redundancy only defeats faults that fail independently so it cannot save you from a shared bug|Redundancy assumes independent failure, which shared code violates]]
- [[A systematic software fault is a dormant wrong assumption about the environment|Software faults are latent wrong assumptions, so there is no failure rate to plan against]]
- [[Deliberately triggering faults is the only way to exercise error-handling code that otherwise never runs|Chaos engineering — untested recovery code is a guess, not a mechanism]]
- [[Preventing a fault beats tolerating it only when no cure exists|Tolerate what you can cure, prevent what you cannot]]
- [[An interface too restrictive to work with gets bypassed, moving the risk somewhere with no guardrails|Restrictive interfaces relocate risk instead of removing it]]

### Scalability and Performance

- [[Scalability is not a property of a system but a question about a specific direction of growth|Scalability — name the growing load parameter before proposing anything]]
- [[Fan-out on write trades expensive writes for cheap reads and fan-out on read does the reverse|Fan-out on write vs read — pay at write time or at read time]]
- [[Response time is what the client sees while latency is only the time a request spends waiting|Response time vs latency — different quantities, different fixes]]
- [[Response time is a distribution so percentiles describe it and the mean does not|Response time is a distribution, so the mean hides who waited]]
- [[Tail latency is a business metric because the slowest requests belong to your heaviest users|Tail latency selects for your most valuable customers]]
- [[Tail latency amplification makes the user-visible p99 worse than any single service behind it|Each extra hop worsens the user-visible p99, even at constant per-service latency]]
- [[Queueing delay is invisible to server-side metrics and to closed-loop load generators|Queueing hides from server metrics and self-throttling load tests]]
- [[Averaging percentiles is meaningless so aggregate response times by adding histograms|Never average p99s — add histograms and recompute]]
- [[There is no generic scalable architecture because scaling is built around which operations are common|No magic scaling sauce — the design encodes which operations are common]]
- [[Stateless services distribute easily but stateful ones do not, so scale up until forced to distribute|Scale up vs out — the stateless/stateful split decides it]]

### Maintainability

- [[The majority of software cost falls in maintenance, so design targets the engineers who arrive later|Most software cost is maintenance, so the maintainer is the real user]]
- [[Good operations can work around bad software but good software cannot survive bad operations|Operability — good ops rescue bad software, never the reverse]]
- [[Simplicity means removing accidental complexity, not removing functionality|Simplicity removes accidental complexity, not features]]
- [[Abstraction is the main tool against accidental complexity but good abstractions are hard to find|Abstraction is the tool against complexity, and it is hard to get right]]
- [[Evolvability is agility at the data system level and it rides on simplicity|Evolvability is bought through simplicity, never pursued directly]]

### Clean Code
- [ ] Meaningful names
- [ ] Small functions (single responsibility)
- [ ] Comments (when and when not)
- [ ] Formatting and consistency
- [ ] Error handling
- [ ] Boundaries
- [ ] Unit tests (F.I.R.S.T. principles)
- [ ] Classes (SRP, cohesion)

### Refactoring
- [ ] Code smells
  - [ ] Long methods
  - [ ] Large classes
  - [ ] Primitive obsession
  - [ ] Feature envy
  - [ ] Data clumps
- [ ] Refactoring techniques
  - [ ] Extract method/class
  - [ ] Replace conditional with polymorphism
  - [ ] Introduce parameter object
  - [ ] Pull up / Push down
- [ ] Safe refactoring with tests

### Architectural Styles

#### Monolith
- [ ] Layered architecture
- [ ] Pros and cons
- [ ] When monolith is right
- [ ] Monolith to microservices migration

#### Modular Monolith
- [ ] Module boundaries
- [ ] Internal vs external APIs
- [ ] Shared kernel
- [ ] Package by feature vs by layer
- [ ] Preparing for future split

#### Microservices
- [ ] Service boundaries
- [ ] Data ownership
- [ ] Inter-service communication
- [ ] Service discovery
- [ ] API Gateway
- [ ] Decomposition strategies
- [ ] Microservices tradeoffs

#### Hexagonal & Clean Architecture
- [ ] Hexagonal architecture (Ports & Adapters)
- [ ] Clean Architecture — the dependency rule
- [ ] Layered vs hexagonal trade-offs

### Domain-Driven Design
- [ ] Ubiquitous language
- [ ] Bounded contexts
- [ ] Context mapping
- [ ] Entities and Value Objects
- [ ] Aggregates and Aggregate Roots
- [ ] Domain events
- [ ] Repositories
- [ ] Application vs Domain services

### Architecture Decision Records
- [ ] ADR format
- [ ] Documenting decisions
- [ ] Status and consequences
- [ ] Templates

---

## Russian Curriculum

### Модуль 2: Монолит
- [ ] Архитектура монолита
- [ ] Слои приложения
- [ ] Паттерны проектирования

### Модуль 4: Микросервисы
- [ ] Декомпозиция
- [ ] Границы сервисов
- [ ] API Gateway
- [ ] Service Discovery

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Clean Code** — Robert Martin | 🔴 Critical | ⏳ |
| **Refactoring** — Martin Fowler | 🟡 Important | ⏳ |
| **Enterprise Application Patterns** — Fowler | 🟡 Important | ⏳ |

---

## Project Tasks

**E-Commerce Stage 8-9:**
- [ ] Identify bounded contexts (Product, Order, User, Payment)
- [ ] Define module boundaries in monolith
- [ ] Extract Product Service
- [ ] Extract Order Service
- [ ] Implement API Gateway
- [ ] Add Service Discovery

---

## Related
- [[Design Patterns - MOC]]
- [[Microservices Patterns - MOC]]
- [[System Design - MOC]]
- [[Soft Skills & Leadership - MOC]]
