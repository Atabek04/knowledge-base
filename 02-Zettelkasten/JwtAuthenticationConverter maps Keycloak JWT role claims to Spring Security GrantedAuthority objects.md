---
aliases: [JwtAuthenticationConverter, Keycloak role converter]
tags: [spring, keycloak, security, jwt]
created: 2026-06-23
---

Spring Security's default JWT converter looks for roles in the `scope` or `scp` claim. Keycloak puts realm roles in `realm_access.roles` — a completely different location. This mismatch means `@PreAuthorize("hasRole('admin')")` silently fails even when the user has the role in Keycloak, because Spring never finds it.

The fix is a custom `Converter<Jwt, Collection<GrantedAuthority>>` that reads `realm_access.roles` and wraps each role as a `SimpleGrantedAuthority`. You then plug it into a `JwtAuthenticationConverter` and register that as the token converter in your security config.

---

### Why the default converter fails

Spring's built-in <mark style="background: #FFF3A3A6;">`JwtGrantedAuthoritiesConverter`</mark> reads the `scope` or `scp` claim and emits `SCOPE_read`, `SCOPE_write`, etc. It knows nothing about Keycloak's `realm_access` structure.

When you call `hasRole("admin")`, Spring Security prepends `ROLE_` and looks for `ROLE_admin` in the granted authorities. Since the default converter never produced that authority, the check fails — no exception, no log line, just a 403.

<mark style="background: #FF5582A6;">Role names are case-sensitive end-to-end.</mark> If the Keycloak role is named `admin` (lowercase, which is the default), then `hasRole("admin")` checks for `ROLE_admin`. Using `hasRole("ADMIN")` would check for `ROLE_ADMIN` and never match. Keep the case consistent from Keycloak role creation all the way through `@PreAuthorize`.

---

### Custom converter — realm roles

```java
public class KeycloakRealmRoleConverter implements Converter<Jwt, Collection<GrantedAuthority>> {

    @Override
    public Collection<GrantedAuthority> convert(Jwt jwt) {
        Map<String, Object> realmAccess = jwt.getClaimAsMap("realm_access");
        if (realmAccess == null) {
            return List.of();
        }

        Object rolesObj = realmAccess.get("roles");
        if (!(rolesObj instanceof List<?> rawList)) {  // safe pattern-match cast
            return List.of();
        }

        return rawList.stream()
            .filter(String.class::isInstance)
            .map(String.class::cast)
            .map(role -> new SimpleGrantedAuthority("ROLE_" + role))
            .collect(Collectors.toList());
    }
}
```

<mark style="background: #BBFABBA6;">The `instanceof List<?> rawList` pattern avoids an unchecked cast.</mark> A plain `(List<String>)` cast would compile with a warning and throw `ClassCastException` if the claim structure is ever non-standard. The `filter(String.class::isInstance)` guard handles mixed-type lists defensively.

---

### Registering the converter in security config

```java
@Configuration
@EnableMethodSecurity          // replaces deprecated @EnableGlobalMethodSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf.disable())          // correct for stateless Bearer-token APIs
            .authorizeHttpRequests(auth -> auth
                .anyRequest().authenticated()
            )
            .oauth2ResourceServer(oauth2 -> oauth2
                .jwt(jwt -> jwt.jwtAuthenticationConverter(jwtAuthenticationConverter()))
            );
        return http.build();
    }

    @Bean
    public JwtAuthenticationConverter jwtAuthenticationConverter() {
        JwtAuthenticationConverter converter = new JwtAuthenticationConverter();
        converter.setJwtGrantedAuthoritiesConverter(new KeycloakRealmRoleConverter());
        return converter;
    }
}
```

<mark style="background: #FFF3A3A6;">`@EnableMethodSecurity`</mark> is the Spring Security 6 replacement for the removed `@EnableGlobalMethodSecurity(prePostEnabled = true)`. With it, `@PreAuthorize` and `@PostAuthorize` work out of the box — no extra attribute needed.

CSRF is correctly disabled here because this is a stateless REST API using Bearer tokens. CSRF attacks exploit session cookies; they cannot forge an `Authorization` header the attacker cannot read. Never disable CSRF on a session-based app.

---

### Adding client roles (resource_access)

Keycloak also places <mark style="background: #ADCCFFA6;">client-level roles under `resource_access.{clientId}.roles`</mark>, as explained in [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access|how Keycloak structures JWT role claims]]. If you need those too, extend the converter:

```java
@Override
public Collection<GrantedAuthority> convert(Jwt jwt) {
    List<GrantedAuthority> authorities = new ArrayList<>();

    // realm roles
    Map<String, Object> realmAccess = jwt.getClaimAsMap("realm_access");
    if (realmAccess != null && realmAccess.get("roles") instanceof List<?> realmRoles) {
        realmRoles.stream()
            .filter(String.class::isInstance)
            .map(r -> new SimpleGrantedAuthority("ROLE_" + r))
            .forEach(authorities::add);
    }

    // client roles
    Map<String, Object> resourceAccess = jwt.getClaimAsMap("resource_access");
    if (resourceAccess != null) {
        resourceAccess.forEach((clientId, clientData) -> {
            if (clientData instanceof Map<?, ?> clientMap
                    && clientMap.get("roles") instanceof List<?> clientRoles) {
                clientRoles.stream()
                    .filter(String.class::isInstance)
                    .map(r -> new SimpleGrantedAuthority("ROLE_" + r))
                    .forEach(authorities::add);
            }
        });
    }

    return authorities;
}
```

---

### Using the roles in @PreAuthorize

Once the converter runs, each Keycloak role `admin` becomes the Spring authority `ROLE_admin`. You can guard methods with [[Spring @PreAuthorize enforces method-level access control using Security Expression Language|`@PreAuthorize`]]:

```java
@PreAuthorize("hasRole('admin')")          // Spring prepends ROLE_ → checks ROLE_admin
public List<UserDto> getAllUsers() { ... }

@PreAuthorize("hasAuthority('ROLE_admin')") // explicit — equivalent, no prefix added
public List<UserDto> getAllUsers() { ... }
```

Both forms are equivalent when the authority string is `ROLE_admin`. Use `hasRole` for readability; use `hasAuthority` when the authority string doesn't follow the `ROLE_` convention.

---

### Read more

- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
- [[Spring Security OAuth2 Resource Server validates JWTs issued by Keycloak without legacy adapters]]
- [[Spring @PreAuthorize enforces method-level access control using Security Expression Language]]
- [[Keycloak roles represent named permissions assigned to users, groups, or clients]]
