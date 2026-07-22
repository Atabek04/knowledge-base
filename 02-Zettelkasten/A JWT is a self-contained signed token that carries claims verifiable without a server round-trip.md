---
aliases: [JWT, JSON Web Token]
tags: [security, jwt, tokens, keycloak]
created: 2026-06-23
---

A <mark style="background: #FFF3A3A6;">JSON Web Token (JWT)</mark> is a compact, URL-safe string that bundles identity and permission claims directly inside itself. Because the token is cryptographically signed, any party holding the right key can verify its authenticity and integrity without calling back to the issuer. That makes it fundamentally different from opaque tokens, which are meaningless strings that require a server round-trip to validate.

### Structure

A JWT is three base64url-encoded segments joined by dots: `header.payload.signature`.

#### Header

The header is a JSON object describing the token's type and the algorithm used to sign it.

```json
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "abc123"
}
```

- `alg` — the signing algorithm (`RS256`, `HS256`, etc.)
- `typ` — always `"JWT"`
- `kid` — key ID, used by the verifier to look up the correct public key when the issuer rotates keys

#### Payload

The payload carries <mark style="background: #FFF3A3A6;">claims</mark> — statements about the subject and the token itself. RFC 7519 defines a set of standard registered claims:

| Claim | Meaning |
|-------|---------|
| `sub` | Subject — who the token is about (user ID) |
| `iss` | Issuer — who created the token |
| `aud` | Audience — intended recipients |
| `exp` | Expiration time (Unix timestamp) |
| `nbf` | Not before — earliest valid time |
| `iat` | Issued at time |
| `jti` | JWT ID — unique identifier for this token |

Everything outside these registered names is a custom claim (e.g., `realm_access.roles` in Keycloak).

#### Signature

The signature is computed over `base64url(header) + "." + base64url(payload)` using the algorithm declared in the header. It is what makes the token tamper-evident — changing even one byte in the payload invalidates the signature.

---

### RS256 vs HS256

The choice of algorithm determines who can verify the token.

<mark style="background: #ADCCFFA6;">**RS256 (asymmetric)**</mark> uses an RSA key pair. The issuer signs with its private key; any consumer verifies with the corresponding public key. The public key is safe to publish (e.g., via a JWKS endpoint). This is the standard choice for distributed systems because resource servers never need access to any secret.

<mark style="background: #FFF3A3A6;">**HS256 (symmetric)**</mark> uses a single shared secret for both signing and verifying. Every party that needs to verify must hold the same secret, which creates a key-distribution and trust problem at scale. Better suited for closed, single-service scenarios.

| | RS256 | HS256 |
|-|-------|-------|
| Key type | RSA key pair | Shared secret |
| Who can verify | Anyone with the public key | Anyone with the secret |
| Key distribution | Safe — public key is public | Risky — secret must be shared |
| Typical use | Distributed microservices, public IdPs | Internal single-service auth |

---

### Why "self-contained"

A resource server receiving a JWT can verify it <mark style="background: #FFF3A3A6;">locally</mark> without contacting the issuer. The steps are:

1. Decode the header to find `alg` and `kid`.
2. Fetch the issuer's public key (once, then cache it — e.g., from the JWKS endpoint).
3. Verify the signature using that key.
4. Check `exp`, `nbf`, and `iss` against expected values.

If all checks pass, the token is valid. No network call to the authorization server is needed per request. This is the core scalability advantage of JWTs over opaque tokens, where every request would require [[Token introspection validates a token by querying the authorization server instead of verifying locally|introspection]].

The tradeoff: a JWT is valid until `exp`, even if the issuer has since revoked the session. Revocation requires either short expiry times, a blocklist check, or falling back to introspection for sensitive operations.

---

### Base64url encoding

Each segment uses <mark style="background: #FFF3A3A6;">base64url</mark> — the standard base64 alphabet with `+` replaced by `-` and `/` replaced by `_`, and with padding (`=`) stripped. This makes the token safe to embed in URLs and HTTP headers without percent-encoding.

Base64url is *encoding*, not *encryption*. The header and payload are fully readable by anyone who holds the token. Never put sensitive data (passwords, PII) in a JWT payload.

---

### Read more

- [[Keycloak issues three token types — Access Token, Refresh Token, and ID Token]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
- [[Token introspection validates a token by querying the authorization server instead of verifying locally]]
- [[OAuth 2.0 delegates authorization by issuing scoped access tokens without exposing credentials]]
