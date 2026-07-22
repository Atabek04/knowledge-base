---
aliases: [OAuth 2.0 scopes, scopes]
tags: [security, oauth, keycloak]
created: 2026-06-23
---

<mark style="background: #FFF3A3A6;">Scopes</mark> are strings a client includes in its authorization request to declare which resources or APIs it needs access to. The authorization server mints a token that covers only those scopes — nothing more. This is the primary mechanism [[OAuth 2.0 delegates authorization by issuing scoped access tokens without exposing credentials|OAuth 2.0]] uses to enforce the principle of least privilege on tokens.

### Standard OIDC scopes

[[OpenID Connect adds an identity layer on top of OAuth 2.0 via the ID token|OIDC]] defines a fixed set of scopes that map to well-known user claims:

- `openid` — required to trigger the OIDC flow; tells the server to return an ID token alongside the access token
- `profile` — name, family_name, given_name, preferred_username, picture, etc.
- `email` — email and email_verified claims
- `address` — address claim (structured postal address)
- `phone` — phone_number and phone_number_verified claims
- `offline_access` — requests a refresh token, allowing the client to act on the user's behalf while they are offline

---

### Custom scopes in Keycloak

Beyond the standard set, a realm defines its own scopes as [[A Keycloak client scope is a reusable bundle of mappers and roles shared across clients|client scopes]] — reusable bundles of [[A Keycloak protocol mapper writes a single claim into a token from user, role, or client data|protocol mappers]] that decide which claims a granted scope adds to the token. A [[A Keycloak client represents an application registered in a realm to delegate authentication|client]] assigns each as *default* or *optional*.

---

### How scopes flow through the protocol

The client sends the requested scopes in the authorization or token request:

```
GET /auth?response_type=code
         &client_id=my-app
         &scope=openid profile email
         &redirect_uri=https://app.example.com/callback
```

After the token is issued, the granted scopes appear inside the JWT under the `scope` claim (sometimes `scp` depending on the server):

```json
{
  "sub": "user-uuid",
  "scope": "openid profile email"
}
```

The resource server reads this claim to decide whether the incoming request carries the right access level.

---

### Scopes vs roles — a critical distinction

The most common confusion when moving from a role-based model to OAuth 2.0:

<mark style="background: #FF5582A6;">Scopes define what the **token** is permitted to reach — the delegated access boundary.</mark>

<mark style="background: #FF5582A6;">Roles define what the **user** may do within those resources.</mark>

Example: a user holds the `ROLE_ADMIN` [[Keycloak roles represent named permissions assigned to users, groups, or clients|role]], but a mobile app requests only `scope=openid profile`. That token cannot call the admin API — not because the user lacks the role, but because the token was never granted the scope to reach it. The roles are irrelevant until a token with the matching scope arrives at the resource server.

Think of scopes as the locked door and roles as the keys to the rooms behind it: without the right scope you never reach the door.

---

### Read more

- [[OAuth 2.0 delegates authorization by issuing scoped access tokens without exposing credentials]]
- [[OpenID Connect adds an identity layer on top of OAuth 2.0 via the ID token]]
- [[OAuth 2.0 grant types define how a client obtains an access token based on its trust level]]
- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[A Keycloak client scope is a reusable bundle of mappers and roles shared across clients]]
- [[A Keycloak protocol mapper writes a single claim into a token from user, role, or client data]]
- [[Keycloak roles represent named permissions assigned to users, groups, or clients]]
