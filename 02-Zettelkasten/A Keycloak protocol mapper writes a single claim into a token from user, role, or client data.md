---
aliases: [protocol mapper, Keycloak protocol mapper, token mapper]
tags: [keycloak, security, oidc, jwt]
created: 2026-06-30
---

When you build a JWT by hand, you decide every claim — you write `claims.put("email", user.getEmail())` for each field. In Keycloak you write none of that code; a <mark style="background: #FFF3A3A6;">protocol mapper</mark> takes its place: one rule that reads a piece of data and writes it into the token as a single claim.

The name says what it does — it *maps* internal data (a user attribute, a role, a group) into a claim for the OIDC *protocol's* token. One mapper = one claim = the declarative equivalent of a single `claims.put(...)` line.

A mapper is attached either to a single [[A Keycloak client represents an application registered in a realm to delegate authentication|client]], or — more often — to a reusable [[A Keycloak client scope is a reusable bundle of mappers and roles shared across clients|client scope]] shared across clients, so common claims like `email` are defined once instead of recreated on every client.

---

### Nothing lands in a token without a mapper

This is the rule that explains most "why is my claim missing?" confusion: <mark style="background: #FF5582A6;">if no mapper produces a claim, that claim is simply absent from the token</mark> — even if the underlying data exists on the user. A token's contents are exactly the union of what its mappers emit, nothing more.

---

### Built-in mappers do the common claims

The claims you see in a standard Keycloak token are produced by mappers that ship by default:

| Mapper | Claim it writes |
|---|---|
| realm roles | `realm_access.roles` |
| client roles | `resource_access.<client-id>.roles` |
| email, given name, family name | `email`, `given_name`, `family_name` |
| audience | adds a value to `aud` |
| groups | `groups` |

So the <mark style="background: #ADCCFFA6;">role claims are not magic</mark> — a built-in *realm roles* mapper and *client roles* mapper put the [[Keycloak roles represent named permissions assigned to users, groups, or clients|assigned roles]] there. Disable those mappers and the role arrays vanish from the token.

---

### Custom mappers add your own claims

When an app needs a field Keycloak doesn't emit by default, you add a mapper for it. The most common is the <mark style="background: #FFF3A3A6;">User Attribute mapper</mark>: store `department=payments` on the user, add a User Attribute mapper, and the token gains:

```json
{
  "department": "payments"
}
```

The resource server can then read `department` straight from the validated JWT — no extra lookup.

---

### Read more

- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[A Keycloak client scope is a reusable bundle of mappers and roles shared across clients]]
- [[Keycloak roles represent named permissions assigned to users, groups, or clients]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
- [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip]]
- [[Keycloak issues three token types — Access Token, Refresh Token, and ID Token]]
- See also:
    - [[Sparse fieldsets let clients request only needed fields reducing payload size]]
