---
aliases: [client scope, Keycloak client scope, default client scope, optional client scope]
tags: [keycloak, security, oidc, jwt]
created: 2026-06-30
---

A [[A Keycloak protocol mapper writes a single claim into a token from user, role, or client data|protocol mapper]] writes one claim into a token. But most apps want the same common claims — `email`, name, roles — so defining those mappers by hand on every [[A Keycloak client represents an application registered in a realm to delegate authentication|client]] would be endless duplication. A <mark style="background: #FFF3A3A6;">client scope</mark> solves that: it is a named, reusable bundle of mappers (and role scope) that you attach to many clients at once.

The name fits: a client scope <mark style="background: #ADCCFFA6;">scopes</mark> what ends up in a client's token, and the same bundle is reused *across* clients. Define `email` once inside the `email` scope, attach it to twenty clients, and all twenty emit the `email` claim.

---

### A token is assembled from many scopes

A client does not have "one rule" — it has <mark style="background: #FFF3A3A6;">several client scopes assigned</mark>, plus optionally its own dedicated mappers. The claims in its token are the **union** of every mapper across all of them.

Keycloak ships built-in scopes that cover the usual claims:

| Built-in scope | What its mappers add |
|---|---|
| `profile` | name, username, locale, … |
| `email` | `email`, `email_verified` |
| `roles` | `realm_access.roles`, `resource_access.*.roles` |
| `web-origins` | allowed CORS origins |

So the role claims you saw earlier come from the built-in `roles` scope — remove that scope from a client and its token carries no role arrays.

---

### Default vs optional scopes

Each scope is attached to a client as one of two kinds:

- <mark style="background: #FFF3A3A6;">Default scope</mark> — always applied; its claims are in every token the client gets.
- <mark style="background: #FFF3A3A6;">Optional scope</mark> — applied only when the client explicitly asks for it via the OAuth [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access|`scope` request parameter]] (e.g. `scope=openid profile phone`). If the client never requests `phone`, those claims stay out.

This is the lever for keeping tokens small: put rarely-needed claims in optional scopes so they're only emitted on demand.

---

### Why different clients carry different claims

Every user lives in <mark style="background: #ADCCFFA6;">one user store</mark> — their attributes don't change per app. What changes is *which scopes each client has*. `order-service` might be assigned `roles` only; `admin-portal` gets `profile` + `email` + `roles`. Same user, same login, but each client's token carries exactly the claims its scopes emit — no more, no less.

---

### How to organize mappers into scopes

<mark style="background: #FFF3A3A6;">Group mappers by concern, not one scope per mapper.</mark> That is exactly how the built-ins are split — `profile`, `email`, `roles`, `address`, `phone` are each a coherent set of claims that tend to be requested together. The dividing rule:

- A claim **reused across clients** → put its mapper in a shared scope (a new one, or an existing concern-scope).
- A claim **only one client needs** → attach the mapper directly to that client, no scope.
- A claim **rarely needed** → an optional scope, so it is emitted only on request.

<mark style="background: #FF5582A6;">Don't dump custom mappers into the default scopes.</mark> Defaults apply to *every* client, so doing that leaks claims to clients that don't need them and bloats every token. The guiding principle is the opposite — <mark style="background: #ADCCFFA6;">minimize the token: include only what each client actually needs</mark>.

---

### What happens when scopes collide

A client's token is the **union** of all its assigned scopes' mappers — but only when claim names don't clash:

- <mark style="background: #ADCCFFA6;">Distinct claim names → union.</mark> Every non-colliding claim from every scope appears together.
- <mark style="background: #FF5582A6;">Same claim name in two mappers → not merged.</mark> Keycloak keeps only *one* value and silently drops the other — a known, acknowledged limitation, not a union. Avoid it with unique, descriptive claim names.
- **Same data under different claim names** → two separate claims, no conflict.
- **Duplicate mapper *names*** (distinct from claim names) → break some admin REST endpoints, which assume mapper names are unique.

---

### Read more

- [[A Keycloak protocol mapper writes a single claim into a token from user, role, or client data]]
- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
- [[Keycloak issues three token types — Access Token, Refresh Token, and ID Token]]
