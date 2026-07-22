---
aliases: [RBAC Keycloak, role-based access control Keycloak]
tags: [keycloak, security, rbac, authorization]
created: 2026-06-23
---

<mark style="background: #FFF3A3A6;">RBAC (Role-Based Access Control)</mark> in Keycloak is a coarse-grained authorization model: an admin assigns named roles to users or groups, and anyone who holds a role gains everything that role permits — no further conditions checked.

The flow runs in three stages: role assignment in the admin console → role encoding into the JWT → role enforcement in Spring Security via `@PreAuthorize`.

---

### Assigning roles in the admin console

[[Keycloak roles represent named permissions assigned to users, groups, or clients|Keycloak roles]] come in two scopes:

- <mark style="background: #FFF3A3A6;">Realm roles</mark> — apply across the entire realm, independent of which client the user is accessing. Useful for global permissions like `ADMIN` or `SUPPORT`.
- <mark style="background: #FFF3A3A6;">Client roles</mark> — scoped to a specific client (e.g. `my-app`). Useful when the same user needs different permissions in different services.

Roles can be assigned directly to a user, or to a group — every member of the group inherits the group's roles. Keycloak also supports <mark style="background: #ADCCFFA6;">composite roles</mark>: a role that bundles other roles, so assigning the composite implicitly grants all contained roles at the token level.

---

### How roles land in the JWT

When a user authenticates, Keycloak encodes their assigned roles into the [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access|JWT claims]]:

```json
{
  "realm_access": {
    "roles": ["offline_access", "manager"]
  },
  "resource_access": {
    "my-app-client": {
      "roles": ["editor"]
    }
  }
}
```

Realm roles appear under `realm_access.roles`. Client roles appear under `resource_access.{client-id}.roles`. Both are plain string arrays — Spring reads them and converts them to `GrantedAuthority` objects.

---

### Wiring roles into Spring Security

Spring Security 6 validates the JWT automatically via `spring-boot-starter-oauth2-resource-server`, but it does not know how to navigate Keycloak's nested role claims out of the box. You need a custom [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects|JwtAuthenticationConverter]].

<mark style="background: #FF5582A6;">**Gotcha:** `JwtGrantedAuthoritiesConverter.setAuthoritiesClaimName("realm_access.roles")` does NOT work. That method expects a flat top-level claim name — there is no top-level key called `realm_access.roles`. Passing it silently produces zero granted authorities.</mark>

The correct approach navigates the nested map manually:

```java
@Bean
public JwtAuthenticationConverter jwtAuthenticationConverter() {
    JwtAuthenticationConverter converter = new JwtAuthenticationConverter();
    converter.setJwtGrantedAuthoritiesConverter(jwt -> {
        Map<String, Object> realmAccess = jwt.getClaimAsMap("realm_access");
        if (realmAccess == null) return List.of();
        @SuppressWarnings("unchecked")
        List<String> roles = (List<String>) realmAccess.get("roles");
        if (roles == null) return List.of();
        return roles.stream()
            .map(role -> new SimpleGrantedAuthority("ROLE_" + role))
            .collect(Collectors.toList());
    });
    return converter;
}
```

For client roles, dig one level deeper:

```java
Map<String, Object> resourceAccess = jwt.getClaimAsMap("resource_access");
if (resourceAccess == null) return List.of();
@SuppressWarnings("unchecked")
Map<String, Object> clientAccess = (Map<String, Object>) resourceAccess.get("my-app-client");
if (clientAccess == null) return List.of();
@SuppressWarnings("unchecked")
List<String> roles = (List<String>) clientAccess.get("roles");
```

---

### Enforcing roles in code

Once the converter populates `GrantedAuthority` objects (prefixed with `ROLE_`), [[Spring @PreAuthorize enforces method-level access control using Security Expression Language|@PreAuthorize]] checks them at the method level:

```java
@PreAuthorize("hasRole('manager')")
public OrderDto getOrder(Long id) { ... }
```

Spring Security automatically prepends `ROLE_` when you use `hasRole()`, so `hasRole('manager')` matches the authority `ROLE_manager`. If you use `hasAuthority()`, you must include the prefix explicitly: `hasAuthority('ROLE_manager')`.

---

### RBAC vs fine-grained authorization

RBAC is a blunt instrument: the role either grants full access or it doesn't. This is fine for most endpoints — `manager` can read all orders, `editor` can edit articles.

When you need <mark style="background: #ADCCFFA6;">attribute-based or resource-level control</mark> (e.g. "user can only edit *their own* orders", "access allowed only on weekdays"), RBAC runs out of steam. That is when [[Keycloak Authorization Services enable ABAC through fine-grained policies and permissions|Keycloak Authorization Services]] (UMA 2.0) take over — they evaluate policies (role, group, time, JavaScript) and issue a Requesting Party Token (RPT) that encodes fine-grained permissions.

A common hybrid: use RBAC for coarse access gates at the API level, and Authorization Services for resource-level decisions inside the service logic.

---

### Read more

- [[Keycloak roles represent named permissions assigned to users, groups, or clients]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
- [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects]]
- [[Spring @PreAuthorize enforces method-level access control using Security Expression Language]]
- [[Keycloak Authorization Services enable ABAC through fine-grained policies and permissions]]
