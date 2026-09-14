---
aliases: ["@PreAuthorize", method security Spring]
tags: [spring, security, keycloak]
created: 2026-06-23
---

<mark style="background: #FFF3A3A6;">`@PreAuthorize`</mark> is Spring Security's annotation for enforcing access control at the method level using Spring Expression Language (SpEL). It evaluates the given expression before the method executes and throws `AccessDeniedException` if the check fails.

This pairs naturally with Keycloak: once [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects|JwtAuthenticationConverter]] converts `realm_access.roles` from the JWT into `ROLE_X` `GrantedAuthority` objects, `@PreAuthorize` can check them with the same expressions you already know from URL-level security.

---

### Enabling method security

Add <mark style="background: #FFF3A3A6;">`@EnableMethodSecurity`</mark> to your security configuration class. In Spring Security 6 (Spring Boot 3) this replaces the old `@EnableGlobalMethodSecurity(prePostEnabled = true)`, which was deprecated in 5.6 and removed in 6.

```java
@Configuration
@EnableWebSecurity
@EnableMethodSecurity   // prePostEnabled = true is the default — no attribute needed
public class SecurityConfig {
    // SecurityFilterChain bean here
}
```

<mark style="background: #FF5582A6;">Do not mix `@EnableGlobalMethodSecurity` with Spring Boot 3 — it no longer exists on the classpath.</mark>

---

### hasRole vs hasAuthority

Both expressions check the `GrantedAuthority` collection on the current `Authentication`, but they differ in prefix handling.

| Expression | What Spring checks | Use when |
|---|---|---|
| `hasRole('admin')` | `ROLE_admin` | Role names come from Keycloak lowercase |
| `hasRole('ADMIN')` | `ROLE_ADMIN` | Role names were upcased in the converter |
| `hasAuthority('ROLE_admin')` | `ROLE_admin` (exact) | You want to be explicit, no prefix added |

<mark style="background: #FFF3A3A6;">`hasRole()` automatically prepends `ROLE_` to the string you pass.</mark> `hasAuthority()` does not — the string must match the authority exactly as stored.

<mark style="background: #FF5582A6;">Role names are case-sensitive end-to-end.</mark> Keycloak emits role names exactly as configured in the realm (default is lowercase). If your converter does `"ROLE_" + role` without `.toUpperCase()`, then `hasRole("admin")` matches but `hasRole("ADMIN")` does not.

---

### Common SpEL expressions

```java
// single role
@PreAuthorize("hasRole('admin')")
public List<UserDto> getAllUsers() { ... }

// any of several roles
@PreAuthorize("hasAnyRole('admin', 'moderator')")
public void banUser(Long id) { ... }

// explicit authority (no prefix added)
@PreAuthorize("hasAuthority('ROLE_admin')")
public void deleteRealm(String name) { ... }

// bind to the authenticated principal — #param must match method argument name
@PreAuthorize("#username == authentication.name")
public UserDto getProfile(String username) { ... }

// delegate to a Spring bean — useful for complex or data-level checks
@PreAuthorize("@accessPolicy.canEdit(#postId, authentication)")
public void updatePost(Long postId, PostDto dto) { ... }
```

<mark style="background: #ADCCFFA6;">The `@beanName.method(#arg)` form lets you move complex authorization logic into a dedicated Spring component instead of embedding it in SpEL strings.</mark>

---

### Where to put @PreAuthorize

The annotation works on any Spring-managed bean method — controller, service, or repository layer.

Putting it only on controllers protects the HTTP entry point but leaves service methods callable from other internal code without any check. <mark style="background: #ADCCFFA6;">Annotating service methods is cleaner and provides defense in depth</mark>: the security rule lives next to the business logic it protects, and any caller — HTTP, messaging, scheduled job — gets the same enforcement.

A common pattern is to annotate the service method as the authoritative guard and omit the annotation on the controller, keeping controllers as thin delegators.

---

### How it connects to Keycloak

After [[Spring Security OAuth2 Resource Server validates JWTs issued by Keycloak without legacy adapters|Spring's resource server]] validates the incoming JWT signature, `JwtAuthenticationConverter` reads `realm_access.roles` and emits one `GrantedAuthority` per role with the `ROLE_` prefix. From that point, `@PreAuthorize("hasRole('admin')")` works exactly as it does with any other authority source — no Keycloak-specific API involved.

The [[RBAC in Keycloak grants access by mapping roles to users or groups inside a realm|RBAC model in Keycloak]] maps realm roles to users; this annotation is the enforcement point on the Spring side.

---

### Read more

- [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects]]
- [[RBAC in Keycloak grants access by mapping roles to users or groups inside a realm]]
- [[Spring Security OAuth2 Resource Server validates JWTs issued by Keycloak without legacy adapters]]
