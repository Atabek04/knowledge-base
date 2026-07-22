---
aliases: [Keycloak user, Keycloak users]
tags: [keycloak, security, oauth]
created: 2026-07-01
---

A <mark style="background: #FFF3A3A6;">Keycloak user</mark> is an account for a real person that lives inside a [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration|realm]]. It holds who the person is — username, email, password, profile attributes — and the [[Keycloak roles represent named permissions assigned to users, groups, or clients|roles]] that decide what they may do.

This is the entity you reach through the **Users** page in the Admin console, and it is <mark style="background: #FF5582A6;">a different thing from a client</mark>, which has its own **Clients** page. The two pages exist because they model two different actors in the same login.

---

### User vs client — who is who

A [[A Keycloak client represents an application registered in a realm to delegate authentication|client]] is an *application*; a user is a *person*. They meet during login:

```
User (person) ──logs into──▶ Client (app) ──validated by──▶ Realm (Keycloak)
```

- A **client** identifies with a `client_id` (+ secret if confidential) and asks Keycloak to authenticate someone — or authenticates *as itself*.
- A **user** identifies with credentials (password, OTP, passkey) and is the *someone* being authenticated.

So configuring an **app** (redirect URIs, secret, scopes) happens on the Clients page; managing a **person** (create account, reset password, assign roles, enable MFA) happens on the Users page.

---

### What a user record holds

- <mark style="background: #ADCCFFA6;">Identity</mark> — username, email, first/last name.
- <mark style="background: #ADCCFFA6;">Credentials</mark> — password, plus any second factor (OTP secret, WebAuthn passkey).
- **Attributes** — arbitrary key/value pairs (e.g. `department`, `phone`) that a [[A Keycloak protocol mapper writes a single claim into a token from user, role, or client data|protocol mapper]] can copy into a token claim.
- **Role mappings** — realm and client roles granted directly or via a group.

A user may live natively in Keycloak's database, or be federated from an external store (LDAP / Active Directory) — either way it surfaces as a user in the realm.

---

### The service account — a client that owns a user

The one place the two concepts touch: enabling **Service Accounts** on a confidential client makes Keycloak auto-create a hidden user named <mark style="background: #FFF3A3A6;">`service-account-<clientId>`</mark>.

That lets the *application itself* carry roles and act with no human present (the [[OAuth 2.0 grant types define how a client obtains an access token based on its trust level|Client Credentials Grant]]). It is still a user row — you assign it roles like any other — but it represents the app, not a person.

<mark style="background: #ADCCFFA6;">Takeaway:</mark> a client can *own* a user, but the concepts stay distinct — that is why they never share a page.

---

### Read more

- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration]]
- [[Keycloak roles represent named permissions assigned to users, groups, or clients]]
- [[A Keycloak protocol mapper writes a single claim into a token from user, role, or client data]]
- [[OAuth 2.0 grant types define how a client obtains an access token based on its trust level]]
