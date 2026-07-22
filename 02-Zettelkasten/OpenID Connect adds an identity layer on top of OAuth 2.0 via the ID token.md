---
aliases: [OIDC, OpenID Connect]
tags: [security, oidc, oauth, keycloak]
created: 2026-06-23
---

<mark style="background: #FFF3A3A6;">OAuth 2.0 is an authorization protocol — it tells a system *what* a client is allowed to do, not *who* the user is.</mark> An access token proves that someone granted permission, but it carries no guaranteed identity information you can rely on. OpenID Connect (OIDC) fills that gap by layering a thin identity protocol on top of OAuth 2.0.

The one-sentence rule: <mark style="background: #ADCCFFA6;">if you need to know WHO is logged in, use OIDC; if you only need to know WHAT they can do, OAuth 2.0 alone suffices.</mark>

### What OAuth 2.0 left out

[[OAuth 2.0 delegates authorization by issuing scoped access tokens without exposing credentials|OAuth 2.0]] was deliberately scoped to authorization. It defines how a client gets an access token representing granted permissions, but the spec says nothing about:

- what the access token's internal structure looks like
- how to retrieve the authenticated user's name or email
- how to verify the user's identity in a portable, interoperable way

Different providers therefore invented their own identity fields in the token, making apps that needed to know the user's identity non-portable across providers. OIDC standardizes exactly this.

---

### What OIDC adds

OIDC introduces three things on top of the OAuth 2.0 Authorization Code flow:

#### The ID Token

<mark style="background: #FFF3A3A6;">The ID Token is a signed JWT returned alongside the access token that carries the authenticated user's identity claims.</mark> It is meant for the *client*, not the resource server — you use it to know who logged in, not to call APIs.

Standard claims inside the ID Token:

| Claim | Meaning |
|---|---|
| `sub` | Stable, unique user identifier (never changes, even if username does) |
| `iss` | Issuer URL — who created the token (must be an HTTPS URL in production) |
| `aud` | Audience — the client ID this token was issued for |
| `iat` | Issued-at timestamp |
| `exp` | Expiry timestamp |
| `name` | Full display name |
| `email` | User's email address |
| `preferred_username` | Login name (mutable — do not use as a stable user key) |

<mark style="background: #FF5582A6;">Never use `preferred_username` or `email` as a stable user identifier — users can change them. Always key your database records on `sub`.</mark>

#### The UserInfo endpoint

The authorization server exposes a `/userinfo` endpoint. The client calls it with the access token to retrieve the same identity claims as the ID Token, plus any additional profile scopes requested. This is useful when you need claims that were omitted from the token to keep it small.

#### The discovery endpoint

<mark style="background: #FFF3A3A6;">Every OIDC provider publishes a self-describing metadata document at `/.well-known/openid-configuration`.</mark> It lists the issuer URL, authorization endpoint, token endpoint, JWKS URI (public keys), supported scopes, and more. Spring Security uses this endpoint automatically when you configure `issuer-uri` — it fetches the document on startup and resolves the JWKS URI to validate token signatures without any manual configuration.

---

### How it fits into the Authorization Code flow

OIDC is not a separate flow. It extends the existing Authorization Code flow with one change: the client includes `openid` in the `scope` parameter of the authorization request.

```
GET /authorize
  ?response_type=code
  &client_id=my-app
  &scope=openid profile email
  &redirect_uri=https://app.example.com/callback
  &code_challenge=...
  &code_challenge_method=S256
```

When `openid` is present, the token endpoint returns both an `access_token` and an `id_token`. Without it, you get only an access token — pure OAuth 2.0 authorization, no identity.

[[OAuth 2.0 scopes limit the set of resources an access token is permitted to access|Scopes]] like `profile` and `email` control which claims appear in the ID Token and at the UserInfo endpoint.

---

### Keycloak and the ID Token

[[Keycloak issues three token types — Access Token, Refresh Token, and ID Token|Keycloak issues all three token types]] when the `openid` scope is requested. The ID Token Keycloak issues also contains Keycloak-specific claims such as `realm_access.roles` and `resource_access.<client-id>.roles`, even though those are authorization claims and technically belong in the access token. <mark style="background: #ADCCFFA6;">[[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access|Keycloak role claims]] live under `realm_access`, not at the top level — a common source of bugs when writing Spring converters.</mark>

In production, ensure `KC_HOSTNAME` and your reverse proxy are configured with HTTPS. Keycloak mirrors the base URL scheme into the `iss` claim of every token — an `http://` issuer violates the OIDC spec and will cause Spring Security's issuer validation to fail.

---

### Read more

- [[OAuth 2.0 delegates authorization by issuing scoped access tokens without exposing credentials]]
- [[Keycloak issues three token types — Access Token, Refresh Token, and ID Token]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
- [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access]]
