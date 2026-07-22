---
aliases: [Keycloak roles]
tags: [keycloak, security, rbac, authorization]
created: 2026-06-23
---

In Keycloak, a <mark style="background: #FFF3A3A6;">role is a named permission label</mark> that you assign to users, groups, or clients — then check in your application to decide what that identity is allowed to do. This is Keycloak's primary mechanism for [[RBAC in Keycloak grants access by mapping roles to users or groups inside a realm|RBAC]].

A role is just a string your resource server reads from the JWT and maps to an access decision.

---

### Realm roles vs client roles

Keycloak has two scopes for roles, and confusing them is the most common mistake.

#### Realm roles

<mark style="background: #FFF3A3A6;">Realm roles are global within a realm</mark> — they exist at the top level of the [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration|realm]] and are not tied to any specific application.

When a user with a realm role gets a token, the role appears in the `realm_access.roles` array:

```json
{
  "realm_access": {
    "roles": ["admin", "user"]
  }
}
```

Once granted, a realm role applies across the entire realm regardless of which client the user logged in through.

#### Client roles

<mark style="background: #FFF3A3A6;">Client roles are scoped to a specific [[A Keycloak client represents an application registered in a realm to delegate authentication|client]]</mark> — they only make sense in the context of that one application.

When a user has client roles, they appear nested under each client ID in the token. A back-office admin in an e-commerce system might carry roles across several apps at once:

```json
{
  "resource_access": {
    "order-service": {
      "roles": ["read-orders", "write-orders"]
    },
    "billing-service": {
      "roles": ["approve-invoice"]
    },
    "admin-portal": {
      "roles": ["view-dashboard", "manage-users"]
    }
  }
}
```

Here `order-service` and `billing-service` are backend APIs, while `admin-portal` is the frontend the user logged in through. Each block's roles are <mark style="background: #ADCCFFA6;">scoped to that one client</mark>: `write-orders` means something only inside `order-service` — it is meaningless to `billing-service` or to the `admin-portal` UI. That is why `admin-portal` and `order-service` can each define their own role names without ever colliding.

These claim paths (`realm_access.roles` and `resource_access.<clientId>.roles`) are [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access|encoded into the JWT]] and are the exact strings your resource server must read.

---

### Which scope to use

In practice, most production setups use <mark style="background: #FFF3A3A6;">both</mark> — with a clear default rule:

- <mark style="background: #FFF3A3A6;">Client role by default.</mark> Keep each permission as narrowly scoped as possible. `read-orders` belongs on `order-service`, not in the global bucket — and a client role never leaks into another app's token.
- <mark style="background: #FFF3A3A6;">Realm role only for cross-app levels.</mark> Promote to a realm role when a permission spans services: org-wide tiers like `admin`, `manager`, `employee` that mean the same everywhere.

So realm roles are not for per-feature permissions — they exist for the handful of <mark style="background: #ADCCFFA6;">"who is this person in the org"</mark> levels that every app cares about.

---

### Composite roles

A <mark style="background: #FFF3A3A6;">composite role is a role that bundles other roles inside it</mark> — assigning the composite automatically grants all its members.

For example, a composite role `manager` could include `read-reports`, `write-reports`, and `approve-reports`. Assigning `manager` to a user grants all three without listing them individually.

Composites can mix realm roles and client roles inside the same bundle.

---

### Role mapping: users vs groups

You can attach roles to a user in two ways:

#### Direct mapping

Assign a role straight to a user. Simple, but hard to manage at scale — changing roles means updating each user individually.

#### Group-based mapping

<mark style="background: #ADCCFFA6;">Assign roles to a group, then add the user to that group.</mark> The user inherits all roles from every group they belong to. This is the preferred approach for production: manage roles once on the group, add/remove users without touching role assignments.

---

### Read more

- [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration]]
- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[RBAC in Keycloak grants access by mapping roles to users or groups inside a realm]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
