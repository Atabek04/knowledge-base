---
aliases: [token introspection, RFC 7662]
tags: [keycloak, security, tokens, oauth]
created: 2026-06-23
---

Token introspection is the alternative to local JWT verification: instead of validating a token's signature and claims yourself, you ask the authorization server "is this token still valid?" and it answers. This is standardized in <mark style="background: #FFF3A3A6;">RFC 7662</mark> and works for any token type — including opaque tokens that carry no readable claims at all.

The key distinction from [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip|local JWT validation]] is that introspection requires a network call on every request, but in return it reflects the server's current knowledge, not a snapshot baked into the token at issuance.

### Introspection endpoint

Keycloak exposes introspection at:

```
POST /realms/{realm}/protocol/openid-connect/token/introspect
```

The caller must authenticate as a <mark style="background: #FFF3A3A6;">confidential client</mark> using Basic auth — the resource server itself acts as a client here:

```bash
curl -X POST \
  https://keycloak.example.com/realms/myrealm/protocol/openid-connect/token/introspect \
  -H "Authorization: Basic $(echo -n 'client_id:client_secret' | base64 -w 0)" \
  -d "token=<the_access_token>"
```

Keycloak also accepts credentials in the POST body (`client_secret_post`) if the client is not configured for Basic auth.

---

### Response shape

A valid, active token returns:

```json
{
  "active": true,
  "scope": "openid profile email",
  "username": "john.doe",
  "client_id": "my-app",
  "exp": 1719100800,
  "sub": "a1b2c3d4-...",
  "iss": "https://keycloak.example.com/realms/myrealm",
  "token_type": "Bearer"
}
```

An invalid or revoked token returns just:

```json
{ "active": false }
```

The <mark style="background: #FFF3A3A6;">`active` boolean</mark> is the only field guaranteed by RFC 7662. All other fields (`scope`, `username`, `exp`, etc.) are optional extensions — Keycloak includes them, but do not assume they exist when writing spec-compliant code.

---

### When to use introspection

Two scenarios make introspection the right choice over local validation:

**Opaque tokens** — if the authorization server issues a random string instead of a JWT, there are no claims to read locally. Introspection is the only option.

**Real-time revocation** — a <mark style="background: #ADCCFFA6;">JWT stays cryptographically valid until its `exp` claim passes</mark>, even if the user logs out or an admin disables the account. Introspection asks the server right now, so a revoked session is caught immediately. This matters for high-security endpoints (admin actions, payment flows) where a 5-minute window of post-logout validity is unacceptable.

---

### Tradeoff: introspection vs local JWT validation

| Dimension | Local JWT validation | Token introspection |
|---|---|---|
| Latency | Zero network calls | One HTTP call per request |
| Revocation | Stale until `exp` | Real-time |
| Works with opaque tokens | No | Yes |
| Auth server availability | Not required per request | Required per request |
| Complexity | JWKS key rotation to handle | Simple HTTP call |

<mark style="background: #FF5582A6;">For most microservices, local JWT validation is preferred for performance.</mark> Introspection adds latency that compounds at scale — a service handling 1 000 req/s makes 1 000 extra HTTP calls per second to Keycloak. Reserve introspection for cases where revocation currency genuinely matters, or where the token is opaque.

The [[Spring Security OAuth2 Resource Server validates JWTs issued by Keycloak without legacy adapters|Spring Security resource server]] supports both modes: `issuer-uri` triggers local JWKS-based validation, while `introspection-uri` switches to the RFC 7662 flow.

---

### Read more

- [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip]]
- [[Keycloak issues three token types — Access Token, Refresh Token, and ID Token]]
- [[Spring Security OAuth2 Resource Server validates JWTs issued by Keycloak without legacy adapters]]
