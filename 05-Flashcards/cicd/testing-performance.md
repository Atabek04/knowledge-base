# CI/CD — Testing Performance

#flashcard/deck/Tech-KB::DevOps::CI-Testing

---

What does Spring's `ContextCache` store, and why does it matter for test speed? #flashcard
?
Spring's `ContextCache` is a static map keyed by the full configuration signature of a test (context classes, profiles, `@MockBean` set, `@DynamicPropertySource`). When two test classes share an identical key, Spring boots the `ApplicationContext` **once** and reuses it for both. A single cold boot takes 10–30 seconds — a suite of 15 test classes with 15 unique keys adds up to 5–7 minutes of pure startup overhead before any assertion runs.

---

What elements of a test class make up the Spring `ContextCache` key? #flashcard
?
- `@ContextConfiguration` classes (or `@SpringBootTest` application class)
- `@ActiveProfiles` set
- `@DynamicPropertySource` method location and registered properties
- `@MockBean` set

Any difference in any element → new context entry → new JVM boot.

---

Why does `@MockBean` break context cache reuse? #flashcard
?
`@MockBean` replaces a real bean with a Mockito mock **inside the Spring context**. Because the mock is part of the configuration key, a test class with `@MockBean(UserService::class)` gets a different key than the base class without it. Spring must start a new context for that class. Even one `@MockBean` on one class can split your suite into two separate context instances.

---

What is the shared base class pattern for Spring integration tests, and what does it buy you? #flashcard
?
An abstract base class that all integration tests extend, carrying the shared configuration:

```kotlin
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@ActiveProfiles("integration")
abstract class IntegrationTestBase {
    companion object {
        @JvmStatic
        @DynamicPropertySource
        fun overrideProperties(registry: DynamicPropertyRegistry) { ... }
    }
}
```

All subclasses inherit the same `ContextCache` key → **one context boot** for the whole suite. Typical saving: 50–70% of integration test wall-clock time.

---

How does the Testcontainers singleton pattern work? #flashcard
?
Containers are declared as `static` fields on a shared Kotlin `object` (or Java static class). The JVM's class-loading guarantee ensures `init {}` runs **exactly once per JVM**, regardless of how many test classes reference the object.

```kotlin
object SharedTestContainers {
    val postgres = PostgreSQLContainer("postgres:16").also { it.start() }
    val redis = RedisContainer(DockerImageName.parse("redis:7")).also { it.start() }
}
```

Every test class that touches `SharedTestContainers.postgres` gets the already-running container — no second startup.

---

Why does `forkCount > 1` break the Testcontainers singleton? #flashcard
?
Each Maven fork is a separate JVM process with its own class loader. The static initializer runs **once per JVM**, so N forks = N container startups. With `forkCount=4` and four containers, that's 16 container startups instead of 4. Keep `forkCount=1` for integration tests and use JUnit 5's within-JVM parallel execution for concurrency instead.

---

How do you start multiple Testcontainers in parallel to reduce startup latency? #flashcard
?
Use Java's parallel streams on the container list in the singleton initializer:

```kotlin
init {
    listOf(postgres, redis, wiremock).parallelStream().forEach { it.start() }
}
```

Sequential start of three containers: ~45 seconds. Parallel start: ~15 seconds (the slowest container). Saves ~30 seconds on every CI run.

---

What is the difference between `mvn verify` and `mvn test-compile failsafe:integration-test failsafe:verify` in CI? #flashcard
?
`mvn verify` runs the full Maven lifecycle including the `package` phase, which assembles the JAR file. On a cold CI runner this takes 2–3 extra minutes before any test runs.

`mvn test-compile failsafe:integration-test failsafe:verify` skips packaging entirely — it only compiles sources and runs Failsafe. On a project with no deployment artifact needed for tests, this saves 2–3 minutes per CI run.

---

What does a two-job parallel CI structure look like for unit + integration tests in GitHub Actions? #flashcard
?
Two separate `jobs:` blocks that run concurrently:

```yaml
jobs:
  unit:
    timeout-minutes: 10
    steps:
      - run: mvn -B test          # Surefire only, no containers

  integration:
    timeout-minutes: 30
    steps:
      - run: docker pull postgres:16 & docker pull redis:7 & wait
      - run: mvn -B test-compile failsafe:integration-test failsafe:verify
```

Total CI time = `max(unit_duration, integration_duration)`, not their sum. Unit tests return feedback in ~1–2 min while integration tests continue independently.

---

Why should you pre-pull Docker images before running Testcontainers in CI? #flashcard
?
On a cold GitHub Actions runner, Testcontainers pulls the image on first `container.start()`, adding the pull latency to the test startup time. Pre-pulling in parallel before the test step hides that latency:

```yaml
- run: docker pull postgres:16 & docker pull redis:7 & wait
```

On a warm runner the images are already cached and the pull completes in seconds. On a cold runner the pull happens in the background while other setup steps run — avoiding a sequential stall when the first container starts.
