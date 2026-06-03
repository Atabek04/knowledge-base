> Write reliable, maintainable tests

---

## Progress

- [ ] JUnit 5 fundamentals
- [ ] Mockito
- [ ] TDD approach
- [ ] Integration testing
- [ ] TestContainers

---

## Topics

### JUnit 5 Fundamentals
- [ ] Test lifecycle (@BeforeAll, @BeforeEach, @AfterEach, @AfterAll)
- [ ] Assertions (assertEquals, assertTrue, assertThrows, assertAll)
- [ ] AssertJ — fluent assertions (assertThat)
- [ ] @Test, @DisplayName, @Disabled
- [ ] @Nested test classes
- [ ] @ParameterizedTest (ValueSource, CsvSource, MethodSource)
- [ ] @RepeatedTest
- [ ] Assumptions
- [ ] Test ordering

### Mockito
- [ ] Creating mocks (@Mock, mock())
- [ ] Stubbing (when...thenReturn, doReturn...when)
- [ ] Verification (verify, times, never, atLeast)
- [ ] Argument matchers (any, eq, argThat)
- [ ] Argument captors
- [ ] @InjectMocks
- [ ] Spies (@Spy)
- [ ] BDD style (given...willReturn)

### Test-Driven Development
- [ ] Red-Green-Refactor cycle
- [ ] Writing tests first
- [ ] Test naming conventions
- [ ] Arrange-Act-Assert pattern
- [ ] Given-When-Then pattern
- [ ] Test isolation

### Integration Testing
- [ ] @SpringBootTest
- [ ] @WebMvcTest (controller tests)
- [ ] @DataJpaTest (repository tests)
- [ ] @MockBean
- [ ] TestRestTemplate, WebTestClient
- [ ] MockMvc — HTTP layer testing without a server
- [ ] Test profiles and configuration

### TestContainers
- [ ] Container lifecycle
- [ ] PostgreSQL container
- [ ] Redis container
- [ ] Kafka container
- [ ] @Container and @Testcontainers
- [ ] Reusable containers

### Contract Testing
- [ ] Consumer-Driven Contract testing — concept
- [ ] Pact — consumer test, pact file, provider verification
- [ ] Spring Cloud Contract — DSL, stub generation

### Testing Best Practices
- [ ] Test pyramid (unit > integration > e2e)
- [ ] Test coverage (meaningful coverage vs 100%)
- [ ] Testing anti-patterns
- [ ] Testing private methods (don't)
- [ ] Flaky tests
- [ ] Test data builders
- [ ] Test doubles — mock vs stub vs spy vs fake vs dummy
- [ ] Property-based testing (jqwik)

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **JUnit in Action** — Manning | 🟡 Important | ⏳ |

---

## Project Tasks

**E-Commerce:** Build test suite
- [ ] Unit tests for ProductService
- [ ] Mock repository in service tests
- [ ] Integration tests for ProductController
- [ ] Repository tests with @DataJpaTest
- [ ] TestContainers for PostgreSQL integration tests

---

## Related
- [[Java MOC]]
- [[Spring Ecosystem - MOC]]
