---
aliases: [Spring context cache, ApplicationContext reuse in tests]
---

Every Spring integration test needs a live `ApplicationContext` — a fully wired Spring container with beans, datasources, and configurations. Booting one takes 10–30 seconds. The `ContextCache` is Spring's mechanism for sharing that cost across tests.

### How the cache works

Spring Test keeps a static `ContextCache` keyed by the full configuration signature of each test: the set of `@ContextConfiguration` classes, active profiles (`@ActiveProfiles`), property overrides (`@DynamicPropertySource`), and mocked beans (`@MockBean`).

<mark style="background: #FFF3A3A6;">If two test classes have an identical key, they share the same `ApplicationContext` — Spring boots it once and reuses it for all tests in both classes.</mark>

If any element of the key differs, Spring starts a second context. Two contexts in a suite of 20 test classes means two cold boots instead of one.

---

### What breaks context reuse

#### `@MockBean` is the most common offender

`@MockBean` injects a Mockito mock into the Spring context. Because the mock is part of the configuration key, <mark style="background: #FF5582A6;">adding `@MockBean` in even one test class forces a new context for that class</mark> — it can no longer share with the clean context.

**Fix:** move mocking to the test method with `@SpyBean` on the shared base class, or use `WireMock` / `MockMvc` at the HTTP boundary instead of mocking Spring beans.

#### `@DynamicPropertySource` location

A `@DynamicPropertySource` method on a test class changes the key even if it registers the same properties as the shared base. Centralise it in the shared base class so all subclasses inherit without polluting their own key.

#### Multiple `@ActiveProfiles` combinations

`@ActiveProfiles("integration")` and `@ActiveProfiles("integration", "kafka")` produce different keys and different contexts. Use a single profile for all integration tests unless the configurations genuinely diverge.

---

### The shared base class pattern

The standard fix is a single abstract base class that all integration tests extend:

```kotlin
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@ActiveProfiles("integration")
abstract class IntegrationTestBase {

    @DynamicPropertySource
    companion object {
        @JvmStatic
        fun overrideProperties(registry: DynamicPropertyRegistry) {
            // Testcontainers URLs go here — shared across all subclasses
        }
    }
}
```

<mark style="background: #BBFABBA6;">All subclasses inherit the same key → one context boot for the entire integration test suite.</mark> Each test class simply extends `IntegrationTestBase` and adds test methods.

---

### Why this matters in CI

A suite with 15 integration test classes and no shared base may boot 15 separate Spring contexts.

At 15–30 seconds per boot, that alone adds 3–7 minutes of pure infrastructure overhead before a single assertion runs.

Consolidating to one shared context typically cuts integration test wall-clock time by 50–70%.

### Read more

- [[Testcontainers singleton pattern starts containers once per JVM by using a static initializer]]
- [[CI test pipeline splits unit and integration tests into parallel jobs to minimize feedback time]]
- [[DevOps - MOC]]
