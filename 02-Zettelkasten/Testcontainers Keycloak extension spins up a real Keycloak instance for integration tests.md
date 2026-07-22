---
aliases: [Testcontainers Keycloak, Keycloak integration tests, KeycloakContainer]
tags: [spring, keycloak, testing, testcontainers]
created: 2026-06-23
---

The `testcontainers-keycloak` library by dasniko lets you boot a real Keycloak instance inside a Docker container for `@SpringBootTest` tests. This tests the <mark style="background: #FFF3A3A6;">full JWT validation pipeline</mark> — token issuance, OIDC discovery, signature verification — none of it is mocked. It is the only way to catch mismatches between your [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access|JWT role claims]] and your [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects|authority converter]] before production.

### Dependency

Add to your `pom.xml` (always check https://github.com/dasniko/testcontainers-keycloak/releases for the latest version — do not pin a version from external sources without verifying):

```xml
<dependency>
    <groupId>com.github.dasniko</groupId>
    <artifactId>testcontainers-keycloak</artifactId>
    <version>${testcontainers-keycloak.version}</version>
    <scope>test</scope>
</dependency>
```

The core class is <mark style="background: #FFF3A3A6;">`KeycloakContainer`</mark> from `dasniko.testcontainers.keycloak`.

---

### Container setup and realm import

Define the container as a static field so Testcontainers starts it once per test class (JUnit 5 `@Container` + `@Testcontainers`):

```java
@Testcontainers
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class AdminApiIntegrationTest {

    @Container
    static KeycloakContainer keycloak = new KeycloakContainer()
            .withRealmImportFile("test-realm.json");
```

<mark style="background: #FFF3A3A6;">`withRealmImportFile("test-realm.json")`</mark> loads the file from the test classpath (`src/test/resources/`) and imports it at container startup. The realm JSON is the same export format Keycloak produces from the admin UI — it carries users, clients, roles, and client secrets in one file.

#### Realm JSON export tip

Export from a local Keycloak dev instance: Admin UI → Realm Settings → Action → Partial export. Include clients and roles. Strip production secrets before committing.

---

### Wiring the Spring context via DynamicPropertySource

<mark style="background: #ADCCFFA6;">`@ServiceConnection` does not exist for Keycloak</mark> (only databases, Redis, and a handful of other containers have auto-configuration in `spring-boot-testcontainers`). You must override the property manually:

```java
@DynamicPropertySource
static void keycloakProperties(DynamicPropertyRegistry registry) {
    registry.add(
        "spring.security.oauth2.resourceserver.jwt.issuer-uri",
        () -> keycloak.getAuthServerUrl() + "/realms/test-realm"
    );
}
```

Spring Security fetches the <mark style="background: #FFF3A3A6;">OIDC discovery document</mark> (`{issuer-uri}/.well-known/openid-configuration`) on the first inbound JWT — not at startup. So the application context boots successfully even before Keycloak finishes initializing, as long as the container is up by the time the first test sends a request.

<mark style="background: #FF5582A6;">Gotcha:</mark> if you define a custom `JwtDecoder` bean that calls `JwtDecoders.fromIssuerLocation()` eagerly inside the constructor, startup will fail if the container is not yet ready. Stick to property-based configuration to keep discovery lazy.

---

### Obtaining a test access token

Your tests need a real Bearer token issued by the containerized Keycloak. POST to the token endpoint with the `client_credentials` grant (for service-to-service tests) or the `password` grant (for user-specific role tests):

```java
private String obtainAccessToken(String clientId, String clientSecret) {
    String tokenUrl = keycloak.getAuthServerUrl()
            + "/realms/test-realm/protocol/openid-connect/token";

    MultiValueMap<String, String> form = new LinkedMultiValueMap<>();
    form.add("grant_type", "client_credentials");
    form.add("client_id", clientId);
    form.add("client_secret", clientSecret);

    var response = new RestTemplate().postForEntity(
            tokenUrl,
            new HttpEntity<>(form, new HttpHeaders()),
            Map.class
    );

    return (String) response.getBody().get("access_token");
}

private HttpHeaders bearerHeader(String token) {
    HttpHeaders headers = new HttpHeaders();
    headers.setBearerAuth(token);
    return headers;
}
```

<mark style="background: #FF5582A6;">Fragile pattern:</mark> string-concatenating `/protocol/openid-connect/token` onto the issuer URI works for standard Keycloak deployments but breaks if the URL has a trailing slash or Keycloak changes its path structure. A more robust alternative is to read `token_endpoint` from the OIDC discovery document, or build the URL from `keycloak.getAuthServerUrl()` directly (as shown above) rather than from the Spring property.

---

### Minimal test

```java
@Test
void shouldReturnOkWithAdminRole() {
    String token = obtainAccessToken("admin-client", "admin-secret");

    var response = restTemplate.exchange(
        "/api/admin/users",
        HttpMethod.GET,
        new HttpEntity<>(bearerHeader(token)),
        String.class
    );

    assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
}

@Test
void shouldReturnForbiddenWithoutAdminRole() {
    String token = obtainAccessToken("readonly-client", "readonly-secret");

    var response = restTemplate.exchange(
        "/api/admin/users",
        HttpMethod.GET,
        new HttpEntity<>(bearerHeader(token)),
        String.class
    );

    // client without admin role → 403
    assertThat(response.getStatusCode()).isEqualTo(HttpStatus.FORBIDDEN);
}
```

<mark style="background: #FF5582A6;">Common bug:</mark> naming a test `shouldReturnForbiddenWithoutAdminRole` but asserting `HttpStatus.OK` — the test passes when it should catch a security misconfiguration. Always match the assertion to the test name.

---

### Role name case sensitivity

<mark style="background: #FF5582A6;">Role names are case-sensitive end-to-end.</mark> Keycloak defaults to lowercase role names (e.g. `admin`). The [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects|role converter]] emits `"ROLE_" + role` preserving the original case, so:

- `hasRole("admin")` → checks `ROLE_admin` ✓ matches Keycloak default
- `hasRole("ADMIN")` → checks `ROLE_ADMIN` ✗ does NOT match

Define role names consistently in the realm JSON and your `@PreAuthorize` expressions.

---

### Safer cast in the role converter

The unchecked cast from `Object` to `List<String>` inside a custom `JwtGrantedAuthoritiesConverter` will throw `ClassCastException` if Keycloak sends a non-standard token. Prefer:

```java
Object rolesObj = realmAccess.get("roles");
if (!(rolesObj instanceof List<?> rawList)) {
    return List.of();
}
List<String> roles = rawList.stream()
    .filter(String.class::isInstance)
    .map(String.class::cast)
    .collect(Collectors.toList());
```

---

### CSRF note

Disabling CSRF (`csrf.disable()`) is correct for a stateless REST API using Bearer tokens — CSRF attacks require a session cookie, which a resource server does not issue. Never disable CSRF on a session-based application.

---

### Read more

- [[Spring Security OAuth2 Resource Server validates JWTs issued by Keycloak without legacy adapters]]
- [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration]]
- [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
