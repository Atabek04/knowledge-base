---
aliases: [Resilience Patterns, Fault Tolerance]
---

> Keeping a service alive when the services it calls are slow or failing: theory first, then Resilience4j on Spring Boot 4.

**Teaching Progress:** next up is "A remote call can succeed, fail, or hang" (Foundations).

---

## Foundations: how remote calls fail

- [[A fault is a component deviating from spec while a failure is the system no longer serving users|Fault vs failure: a component breaks, the system may not]]
- [ ] A remote call can succeed, fail, or hang, and hanging is the worst outcome
- [ ] A slow dependency is more dangerous than a dead one because it holds threads
- [ ] Every remote call needs a timeout, or one slow dependency exhausts the caller's threads
- [ ] Connect, read and overall timeouts bound different phases of a call
- [ ] Timeout budgets must shrink down the call chain, or upstream gives up while downstream still works
- [ ] Retries only help with transient faults; a permanent fault just gets multiplied
- [ ] Exponential backoff spaces out retries so a struggling service gets room to recover
- [ ] Jitter randomises backoff so synchronised clients stop retrying in lockstep
- [ ] Retrying at every layer multiplies the load geometrically
- [[Idempotency key prevents duplicate processing when clients retry failed requests|Idempotency key: retries become safe]]
- [ ] A retry storm keeps a recovering service overloaded
- [ ] Cascading failure spreads when callers block on a failing dependency

## Circuit breaker theory

- [ ] A circuit breaker stops calls to a failing dependency so it can recover and the caller fails fast
- [ ] Closed state passes calls through and records their outcomes
- [ ] Open state rejects calls immediately until a wait duration expires
- [ ] Half-open state lets a few trial calls through to decide between closing and reopening
- [ ] Failure-rate threshold trips the breaker on errors, slow-call threshold trips it on latency
- [ ] Minimum number of calls stops a breaker tripping on a tiny sample
- [ ] Count-based sliding window judges the last N calls, time-based judges the last N seconds
- [ ] Which exceptions count as failures decides whether the breaker protects or misfires
- [ ] A fallback returns a degraded answer instead of an error while the circuit is open

## Related patterns and how they compose

- [ ] Bulkhead caps concurrent calls per dependency so one cannot drain every thread
- [ ] Semaphore bulkhead vs thread-pool bulkhead
- [ ] Rate limiter caps how many calls are made per period
- [ ] Time limiter bounds an async call's duration
- [[Load shedding drops excess requests to keep the core service alive|Load shedding: drop excess to keep the core alive]]
- [ ] Order of composition decides whether retries count against the breaker

## When to use a circuit breaker, and when not to

- [ ] A circuit breaker is redundant for in-process calls and local resources
- [ ] One breaker shared across all hosts trips on a single bad instance
- [ ] A fallback that calls another remote service just moves the failure
- [ ] Breaker thresholds tuned without real traffic data trip too early or never
- [ ] Recording client errors such as 4xx as failures opens the circuit on bad input

## Resilience4j in Spring Boot 4

- [ ] resilience4j-spring-boot4 2.4.0 is the Boot 4 module, pinned outside the BOM
- [ ] Spring Framework 7 native retry vs Resilience4j: when the built-in annotations are enough
- [ ] @CircuitBreaker wraps a bean method through an AOP proxy, so self-invocation bypasses it
- [ ] YAML instances configure a breaker by name under resilience4j.circuitbreaker
- [ ] recordExceptions and ignoreExceptions decide which errors move the failure rate
- [ ] A fallback method copies the signature plus one exception parameter
- [ ] Aspect order: by default Retry wraps CircuitBreaker, configurable per aspect
- [ ] Actuator exposes breaker state through health, metrics and circuitbreakerevents

## Testing and operating it

- [ ] CircuitBreakerRegistry lets a test force open, closed or half-open
- [ ] Simulating slow and failing downstreams in integration tests
- [ ] State-transition metrics feed alerts on a circuit that stays open
- [ ] A circuit opening is a symptom, so the alert points at the dependency

---

### Read more

- [[Microservices Patterns - MOC]]
- [[System Design - MOC]]
- [[Spring Ecosystem - MOC]]
- [[Distributed Systems - MOC]]
