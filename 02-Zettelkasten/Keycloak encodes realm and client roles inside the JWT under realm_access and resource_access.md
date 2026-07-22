---
aliases: [Keycloak JWT claims, realm_access, resource_access]
tags: [keycloak, jwt, security, tokens]
created: 2026-06-23
---

When Keycloak issues an [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip|access token]], it packs role information into two custom claims: <mark style="background: #FFF3A3A6;">`realm_access`</mark> for realm-wide roles and <mark style="background: #FFF3A3A6;">`resource_access`</mark> for client-specific roles. These claims live in the JWT payload alongside standard OIDC claims like `sub`, `iss`, and `exp`.

Understanding this structure is essential for Spring Security integration, because Spring's default JWT support does not know to look in `realm_access.roles` — it has to be told explicitly.

### Decoded JWT payload

A typical Keycloak access token payload looks like this:

```json
{
  "sub": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "iss": "https://keycloak.example.com/realms/myrealm",
  "azp": "my-client",
  "sid": "9f8e7d6c-5b4a-3210-fedc-ba9876543210",
  "preferred_username": "john.doe",
  "email": "john.doe@example.com",
  "exp": 1750000300,
  "iat": 1750000000,
  "jti": "f1e2d3c4-b5a6-7890-1234-567890abcdef",
  "typ": "Bearer",
  "realm_access": {
    "roles": ["offline_access", "uma_authorization", "admin"]
  },
  "resource_access": {
    "my-client": {
      "roles": ["view", "edit"]
    },
    "account": {
      "roles": ["manage-account"]
    }
  }
}
```

---

### Standard claims

<mark style="background: #ADCCFFA6;">These claims are defined by RFC 7519 and OpenID Connect</mark> — Keycloak emits all of them in a default configuration.

#### sub — Subject
The unique identifier for the user within the realm. It is a UUID and is stable across sessions — safe to use as a foreign key in your database.

#### iss — Issuer
The URL of the Keycloak realm that signed the token. Spring Security uses this to fetch the JWKS endpoint and verify the signature automatically.

#### azp — Authorized Party
<mark style="background: #FFF3A3A6;">`azp` identifies which client requested this token</mark> — the "authorized party" that initiated the OAuth flow. Useful when one resource server needs to verify the token was issued to a specific client.

#### sid — Session ID
Identifies the Keycloak user session. Replaced `session_state` in <mark style="background: #FF5582A6;">Keycloak 25 — `session_state` was removed from access tokens in 25.0.0</mark>; use `sid` going forward.

#### exp / iat / jti
Standard expiry, issued-at, and JWT ID claims. `jti` is a unique token identifier useful for revocation tracking.

#### preferred_username / email
Convenience claims for display purposes. `preferred_username` is not guaranteed to be unique across realms — use `sub` as the canonical user identifier in application code.

---

### Role claims

#### realm_access
<mark style="background: #FFF3A3A6;">`realm_access.roles`</mark> carries the roles assigned to the user at the realm level — roles that apply across all clients in this realm. These are the [[Keycloak roles represent named permissions assigned to users, groups, or clients|realm roles]] configured in Keycloak Admin under Realm roles.

#### resource_access
<mark style="background: #FFF3A3A6;">`resource_access`</mark> is a map from client ID to a `roles` array. Each entry holds the [[Keycloak roles represent named permissions assigned to users, groups, or clients|client roles]] the user has for that specific client. The key is the exact `clientId` string configured in Keycloak.

The `account` entry in `resource_access` is always present — it represents the built-in Keycloak account management client.

---

### Why Spring needs a custom converter

Spring Security's `oauth2ResourceServer().jwt()` validates the token signature and expiry correctly out of the box. What it does not do is map role claims to `GrantedAuthority` objects — because Spring expects roles in a top-level `roles` or `authorities` claim, not nested inside `realm_access`.

<mark style="background: #FF5582A6;">Without a custom converter, `hasRole("admin")` will always return false</mark> even if the JWT contains `realm_access.roles: ["admin"]`.

The fix is a [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects|`JwtAuthenticationConverter`]] that reads `realm_access.roles`, prefixes each role with `ROLE_`, and returns them as `SimpleGrantedAuthority` objects. Spring Security then calls this converter on every request before evaluating `@PreAuthorize` expressions.

This is a one-time wiring step — after that, `hasRole("admin")` and `hasAuthority("ROLE_admin")` work as expected throughout the application.

### Read more

- [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip]]
- [[Keycloak roles represent named permissions assigned to users, groups, or clients]]
- [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects]]
- [[Keycloak issues three token types — Access Token, Refresh Token, and ID Token]]
