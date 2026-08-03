---
aliases: [Testcontainers singleton, shared containers in tests]
---

Testcontainers starts a real Docker container for each test class by default. If 15 test classes each start their own PostgreSQL container, that is 15 container startups — each taking 5–15 seconds — before a single test runs.

The singleton pattern eliminates this by starting containers once per JVM and reusing them for the entire test run.

### How the singleton pattern works

Declare containers as `static` fields on a shared object or companion object. The JVM's class-loading guarantee ensures the initializer runs exactly once, no matter how many test classes reference it.

```kotlin
object SharedTestContainers {
    val postgres: PostgreSQLContainer<*> = PostgreSQLContainer("postgres:16")
        .withDatabaseName("test_db")
        .withUsername("test")
        .withPassword("test")

    val redis: RedisContainer = RedisContainer(DockerImageName.parse("redis:7"))

    init {
        // Start both in parallel — saves ~30s vs sequential startup
        listOf(postgres, redis).parallelStream().forEach { it.start() }
    }
}
```

<mark style="background: #FFF3A3A6;">Any test class that references `SharedTestContainers.postgres` triggers class loading, which runs `init {}` exactly once.</mark> Subsequent test classes find the containers already running and skip the startup cost.

---

### Wiring into Spring's `@DynamicPropertySource`

The shared base class reads the running container's mapped ports and feeds them to Spring:

```kotlin
@DynamicPropertySource
companion object {
    @JvmStatic
    fun overrideProperties(registry: DynamicPropertyRegistry) {
        registry.add("spring.datasource.url") { SharedTestContainers.postgres.jdbcUrl }
        registry.add("spring.data.redis.host") { SharedTestContainers.redis.host }
        registry.add("spring.data.redis.port") { SharedTestContainers.redis.firstMappedPort.toString() }
    }
}
```

This connects to the [[Spring ApplicationContext cache determines how many times the JVM boots Spring during a test suite|context cache]] — the same `DynamicPropertySource` on the same base class means all subclasses share one context and one set of containers.

---

### Why `forkCount > 1` breaks the singleton

<mark style="background: #FF5582A6;">Maven Surefire/Failsafe with `forkCount > 1` launches multiple JVM processes.</mark> Each JVM has its own class loader — the static initializer runs once *per JVM*, not once total. Ten forks = ten container startups, defeating the pattern entirely.

**Fix:** keep `forkCount=1` (default) for integration tests. Use JUnit 5's `parallel` execution *within* the single JVM (`junit.jupiter.execution.parallel.enabled=true`) for fine-grained concurrency without breaking container sharing.

---

### Parallel container startup

Multiple containers can start concurrently using Java's parallel streams:

```kotlin
listOf(postgres, redis, wiremock).parallelStream().forEach { it.start() }
```

Sequential startup of three containers may take 45 seconds; parallel startup takes ~15 seconds (the duration of the slowest container). <mark style="background: #BBFABBA6;">This alone can shave 30 seconds off every CI run.</mark>

### Read more

- [[Spring ApplicationContext cache determines how many times the JVM boots Spring during a test suite]]
- [[CI test pipeline splits unit and integration tests into parallel jobs to minimize feedback time]]
- [[DevOps - MOC]]
