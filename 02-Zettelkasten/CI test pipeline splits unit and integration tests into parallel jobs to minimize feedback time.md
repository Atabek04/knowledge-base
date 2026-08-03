---
aliases: [CI test split, parallel CI jobs, unit vs integration in CI]
---

Running all tests in a single sequential job — unit tests first, then integration tests — means a developer waits for the slowest stage before seeing any result. Splitting into parallel jobs returns fast feedback from unit tests in 1–2 minutes while integration tests continue running independently.

### The two-job structure

Unit tests and integration tests have fundamentally different resource requirements:

| Property | Unit tests | Integration tests |
|---|---|---|
| Docker containers | None | PostgreSQL, Redis, etc. |
| Startup overhead | None | 15–45 seconds per JVM boot |
| Parallelism risk | Safe — pure functions | Unsafe with `forkCount > 1` |
| Typical duration | 30s – 2 min | 5–15 min |

<mark style="background: #FFF3A3A6;">Running them as separate parallel jobs means the unit test job finishes in 1–2 minutes regardless of how long integration tests take.</mark> A failing unit test surfaces immediately without waiting for containers to start.

---

### GitHub Actions example

```yaml
jobs:
  unit:
    name: Unit tests
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v5
        with:
          java-version: "21"
          distribution: temurin
          cache: maven
      - name: Run unit tests
        working-directory: api
        run: mvn -B test

  integration:
    name: Integration tests
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v5
        with:
          java-version: "21"
          distribution: temurin
          cache: maven
      - name: Pre-pull container images
        run: |
          docker pull postgres:16 &
          docker pull redis:7 &
          wait
      - name: Run integration tests
        working-directory: api
        # Skip the package phase — avoids ~2–3 min of jar assembly
        run: mvn -B test-compile failsafe:integration-test failsafe:verify
```

Both jobs run concurrently. Total CI wall-clock = `max(unit_duration, integration_duration)`, not their sum.

---

### Maven: separating unit and integration tests

Maven Surefire runs unit tests (`mvn test`). Maven Failsafe runs integration tests (`mvn verify` or directly via `failsafe:integration-test`).

<mark style="background: #FFF3A3A6;">Convention-based separation by class name suffix:</mark>

```xml
<!-- Surefire: exclude IT classes -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <excludes>
            <exclude>**/*IT</exclude>
            <exclude>**/*IntegrationTest*</exclude>
        </excludes>
        <parallel>classes</parallel>
        <threadCount>2</threadCount>
    </configuration>
</plugin>

<!-- Failsafe: only IT classes, single fork to protect Testcontainers singleton -->
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-failsafe-plugin</artifactId>
    <configuration>
        <includes>
            <include>**/*IT</include>
            <include>**/*IntegrationTest</include>
        </includes>
        <forkCount>1</forkCount>
        <reuseForks>true</reuseForks>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>integration-test</goal>
                <goal>verify</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

<mark style="background: #FF5582A6;">Never set `forkCount > 1` for integration tests</mark> — each fork is a new JVM and defeats the [[Testcontainers singleton pattern starts containers once per JVM by using a static initializer|Testcontainers singleton]].

---

### Skip `mvn verify` in CI — use goal invocation directly

`mvn verify` runs the full lifecycle including the `package` phase, which assembles the JAR (~2–3 minutes on a cold runner).

For CI integration tests, skip packaging entirely:

```bash
mvn -B test-compile failsafe:integration-test failsafe:verify
```

`test-compile` compiles sources and tests without packaging. `failsafe:integration-test` + `failsafe:verify` run only integration tests and collect results. <mark style="background: #BBFABBA6;">This alone saves 2–3 minutes per CI run.</mark>

---

### Pre-pulling Docker images

Container image pulls happen on first use. Pre-pulling in parallel before the tests start hides latency:

```yaml
- name: Pre-pull container images
  run: |
    docker pull postgres:16 &
    docker pull redis:7 &
    wait
```

On a warm GitHub Actions runner the images are cached — the `docker pull` completes in seconds and the containers start immediately when Testcontainers requests them.

### Read more

- [[Spring ApplicationContext cache determines how many times the JVM boots Spring during a test suite]]
- [[Testcontainers singleton pattern starts containers once per JVM by using a static initializer]]
- [[DevOps - MOC]]
