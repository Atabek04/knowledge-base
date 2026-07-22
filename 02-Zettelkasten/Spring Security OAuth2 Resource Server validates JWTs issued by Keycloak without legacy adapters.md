---
aliases: [Spring Resource Server, OAuth2 Resource Server, oauth2ResourceServer]
tags: [spring, keycloak, security, jwt]
created: 2026-06-23
---

Spring Boot 3 + Spring Security 6 can validate Keycloak-issued JWTs natively using the <mark style="background: #FFF3A3A6;">OAuth2 Resource Server support built into Spring Security</mark> — no Keycloak-specific adapter needed. The old `keycloak-spring-boot-adapter` and `keycloak-spring-security-adapter` are <mark style="background: #FF5582A6;">deprecated and removed from Keycloak 25+ — never use them in Spring Boot 3 projects</mark>. Instead, one dependency and a few lines of configuration are all that is required.

### Dependency

Add the OAuth2 resource server starter to `pom.xml`:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-oauth2-resource-server</artifactId>
</dependency>
```

This pulls in `spring-security-oauth2-resource-server` and the Nimbus JOSE+JWT library for local JWT verification.

---

### Configuration via `application.yml`

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: http://localhost:8080/realms/my-realm
```

<mark style="background: #FFF3A3A6;">`spring.security.oauth2.resourceserver.jwt.issuer-uri`</mark> points to the Keycloak realm URL (not the Keycloak root, not the token endpoint — the realm itself).

#### How OIDC discovery works

When the first inbound request carries a Bearer token, Spring Security fetches the <mark style="background: #ADCCFFA6;">OIDC discovery document at `{issuer-uri}/.well-known/openid-configuration`</mark>. That document contains a `jwks_uri` field pointing to Keycloak's public key set. Spring Security fetches those keys and caches them locally. Every subsequent JWT is verified locally against the cached keys — no round-trip to Keycloak per request.

This means <mark style="background: #BBFABBA6;">application startup is NOT coupled to Keycloak availability</mark>. The discovery fetch is deferred until the first JWT arrives. One edge case: if you manually define a `JwtDecoder` bean that eagerly calls `JwtDecoders.fromIssuerLocation()` at construction time, startup will fail if Keycloak is down — avoid this.

---

### `SecurityFilterChain` bean

```java
@Configuration
@EnableWebSecurity
@EnableMethodSecurity   // replaces deprecated @EnableGlobalMethodSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer(oauth2 -> oauth2
                .jwt(Customizer.withDefaults())
            )
            .sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            )
            .csrf(csrf -> csrf.disable()); // correct for stateless Bearer-token APIs

        return http.build();
    }
}
```

<mark style="background: #FFF3A3A6;">`.oauth2ResourceServer(oauth2 -> oauth2.jwt(Customizer.withDefaults()))`</mark> activates JWT validation using the `issuer-uri` configured above. `WebSecurityConfigurerAdapter` was removed in Spring Boot 3 — `SecurityFilterChain` bean is the only valid pattern.

`csrf.disable()` is intentional and correct here: CSRF attacks rely on session cookies. A stateless API that only accepts Bearer tokens has no session to hijack.

<mark style="background: #FF5582A6;">`@EnableGlobalMethodSecurity` was removed in Spring Security 6 — use `@EnableMethodSecurity` instead.</mark> `prePostEnabled = true` is the default, so no attribute is needed.

---

### Role extraction from Keycloak JWTs

By default, Spring Security maps JWT `scope` claims to `SCOPE_*` authorities, which is useless for Keycloak role-based access. You need a custom converter that reads [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access|`realm_access.roles`]] from the token payload.

```java
@Component
public class KeycloakJwtRolesConverter implements Converter<Jwt, Collection<GrantedAuthority>> {

    @Override
    public Collection<GrantedAuthority> convert(Jwt jwt) {
        List<GrantedAuthority> authorities = new ArrayList<>();

        // Realm roles
        Map<String, Object> realmAccess = jwt.getClaimAsMap("realm_access");
        if (realmAccess != null) {
            Object rolesObj = realmAccess.get("roles");
            if (rolesObj instanceof List<?> rawList) {
                rawList.stream()
                    .filter(String.class::isInstance)
                    .map(String.class::cast)
                    .map(role -> new SimpleGrantedAuthority("ROLE_" + role))
                    .forEach(authorities::add);
            }
        }

        // Client roles (resource_access.<clientId>.roles)
        Map<String, Object> resourceAccess = jwt.getClaimAsMap("resource_access");
        if (resourceAccess != null) {
            resourceAccess.forEach((clientId, clientData) -> {
                if (clientData instanceof Map<?, ?> clientMap) {
                    Object rolesObj = clientMap.get("roles");
                    if (rolesObj instanceof List<?> rawList) {
                        rawList.stream()
                            .filter(String.class::isInstance)
                            .map(String.class::cast)
                            .map(role -> new SimpleGrantedAuthority("ROLE_" + role))
                            .forEach(authorities::add);
                    }
                }
            });
        }

        return authorities;
    }
}
```

Wire the converter into `SecurityFilterChain` via `JwtAuthenticationConverter`:

```java
@Bean
public JwtAuthenticationConverter jwtAuthenticationConverter(
        KeycloakJwtRolesConverter rolesConverter) {
    var converter = new JwtAuthenticationConverter();
    converter.setJwtGrantedAuthoritiesConverter(rolesConverter);
    return converter;
}
```

Then reference it in the filter chain:

```java
.jwt(jwt -> jwt.jwtAuthenticationConverter(jwtAuthenticationConverter(rolesConverter)))
```

#### Case sensitivity gotcha

<mark style="background: #FF5582A6;">Role names are case-sensitive end-to-end.</mark> Keycloak emits role names exactly as configured in the realm (lowercase by default, e.g. `admin`). The converter above emits `ROLE_admin`. `hasRole("admin")` in `@PreAuthorize` checks for `ROLE_admin` — this matches. `hasRole("ADMIN")` checks for `ROLE_ADMIN` — this does NOT match a lowercase Keycloak role. Keep the case consistent between the realm configuration and your authorization expressions.

#### Unchecked cast safety

The `instanceof List<?>` pattern with `.filter(String.class::isInstance)` avoids raw `ClassCastException` if Keycloak sends a non-standard token structure. Never cast directly from `Object` to `List<String>` without an instance check.

---

### Method-level security with `@PreAuthorize`

```java
@RestController
@RequestMapping("/api/admin")
public class AdminController {

    @GetMapping("/users")
    @PreAuthorize("hasRole('admin')")
    public List<UserDto> listUsers() {
        return userService.findAll();
    }
}
```

`hasRole('admin')` is equivalent to `hasAuthority('ROLE_admin')` — Spring Security prepends `ROLE_` automatically. The [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects|custom converter]] must emit `ROLE_admin` for this to match.

---

### Deprecated adapters — do not use

| Artifact | Status |
|---|---|
| `keycloak-spring-boot-starter` | Deprecated, removed in Keycloak 25+ |
| `keycloak-spring-security-adapter` | Deprecated, removed in Keycloak 25+ |
| `spring-boot-starter-oauth2-resource-server` | Current standard |

<mark style="background: #FF5582A6;">Any guide or Stack Overflow answer that references `KeycloakWebSecurityConfigurerAdapter` is outdated — this class no longer exists in Keycloak's supported libraries.</mark>

---

### ### Read more

- [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
- [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects]]
- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[Token introspection validates a token by querying the authorization server instead of verifying locally]]
