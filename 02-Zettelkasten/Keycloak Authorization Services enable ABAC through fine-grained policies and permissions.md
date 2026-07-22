---
aliases: [Keycloak Authorization Services, ABAC Keycloak, fine-grained authorization]
tags: [keycloak, security, abac, authorization]
created: 2026-06-23
---

<mark style="background: #FFF3A3A6;">Authorization Services</mark> is Keycloak's answer to the question "what happens when role checks are not enough?" Where [[RBAC in Keycloak grants access by mapping roles to users or groups inside a realm|RBAC]] stops at "does the user have role X?", Authorization Services evaluates the resource being accessed, the operation requested, and any contextual attributes — this model is called <mark style="background: #FFF3A3A6;">Attribute-Based Access Control (ABAC)</mark>.

The system is built around four concepts: resources, scopes, policies, and permissions. Each concept is a separate object in Keycloak, and they compose together to answer a single question: "can this user perform this operation on this thing?"

---

### The Authorization Model

#### Resource

A <mark style="background: #FFF3A3A6;">resource</mark> is what is being protected — a URI, a data object, a feature flag. Examples: `/api/documents/{id}`, `Invoice`, `admin-panel`. Resources can be typed and owned (a document owned by a specific user is a different resource instance than one owned by another).

#### Scope

A <mark style="background: #FFF3A3A6;">scope</mark> defines what operation is being requested on that resource: `view`, `edit`, `delete`, `approve`. A resource can have multiple scopes. The combination `Document:edit` is more precise than any role can express.

#### Policy

A <mark style="background: #FFF3A3A6;">policy</mark> answers "who qualifies?" independently of any resource. Policies are reusable logic units:

- **Role Policy** — user must hold role `manager`
- **User Policy** — user must be a specific account (e.g. a service account)
- **Group Policy** — user must belong to group `/finance/senior`
- **Time Policy** — access only between 09:00–17:00 on weekdays
- **JavaScript Policy** — arbitrary JS expression; <mark style="background: #FF5582A6;">disabled by default, requires `--features=scripts` flag — verify flag name against your Keycloak version before enabling</mark>
- **Aggregated Policy** — combines other policies using a decision strategy: `Unanimous` (all must pass), `Affirmative` (any one passes), or `Consensus` (majority passes)

#### Permission

A <mark style="background: #FFF3A3A6;">permission</mark> is the glue: it binds a resource (optionally a scope) to one or more policies. "The `Document:edit` scope requires the `Is Owner` policy AND the `Business Hours` time policy" — that is a permission.

---

### PEP and PDP — Who Does the Work

Think of this like Spring Security's filter chain, but distributed.

The <mark style="background: #FFF3A3A6;">Policy Enforcement Point (PEP)</mark> lives in your application code. Before allowing an operation, the PEP calls Keycloak to ask for a decision. In practice this is an HTTP call to Keycloak's token endpoint requesting a <mark style="background: #ADCCFFA6;">Requesting Party Token (RPT)</mark> — a special access token that embeds the authorization decision.

The <mark style="background: #FFF3A3A6;">Policy Decision Point (PDP)</mark> is Keycloak itself. It receives the request (which resource, which scope, which user), evaluates every matching policy, applies the aggregation strategy, and returns `PERMIT` or `DENY`.

The flow:

```
Client → PEP (your service) → Keycloak PDP (evaluate policies) → RPT issued
PEP checks RPT → allow or reject the request
```

For simpler deployments, the `keycloak-policy-enforcer` library (groupId `org.keycloak`, artifactId `keycloak-policy-enforcer`) can act as the PEP automatically — but it requires manual wiring since the legacy Spring adapter was removed. Match the library version to the running Keycloak server version exactly.

---

### RBAC vs Authorization Services

<mark style="background: #ADCCFFA6;">RBAC</mark> (what [[RBAC in Keycloak grants access by mapping roles to users or groups inside a realm|Keycloak's role model]] gives you out of the box):

```
user has role → allow
```

Simple, fast, stateless — the JWT carries the roles and Spring Security's `hasRole()` checks them locally without any Keycloak round-trip.

<mark style="background: #ADCCFFA6;">ABAC via Authorization Services</mark>:

```
evaluate(resource + user attributes + scope + context) → allow / deny
```

Powerful, but every check is a network call to Keycloak (or a cached RPT). Use it when:
- Access depends on data ownership ("only the document's author can edit")
- Access depends on time, location, or other runtime context
- Policy must be changed without redeploying the application
- [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access|Scope-level]] granularity is required beyond what roles can express

The common **hybrid approach**: use RBAC (roles in JWT, checked by Spring Security) for coarse-grained access, and Authorization Services only for the resources that genuinely need fine-grained rules. This avoids the latency cost of a PDP call on every request.

---

### Spring Security Integration

Authorization Services does not use `JwtAuthenticationConverter` — that class only extracts roles from the JWT for standard RBAC. For ABAC you need the policy enforcer or a custom filter that exchanges the bearer token for an RPT.

For reference, the correct converter for Keycloak realm roles (used in the RBAC path) manually navigates the nested `realm_access` claim:

```java
@Bean
public JwtAuthenticationConverter jwtAuthenticationConverter() {
    JwtAuthenticationConverter converter = new JwtAuthenticationConverter();
    converter.setJwtGrantedAuthoritiesConverter(jwt -> {
        Map<String, Object> realmAccess = jwt.getClaimAsMap("realm_access");
        if (realmAccess == null) return List.of();
        @SuppressWarnings("unchecked")
        List<String> roles = (List<String>) realmAccess.get("roles");
        if (roles == null) return List.of();
        return roles.stream()
            .map(role -> new SimpleGrantedAuthority("ROLE_" + role))
            .collect(Collectors.toList());
    });
    return converter;
}
```

<mark style="background: #FF5582A6;">Do not use `setAuthoritiesClaimName("realm_access.roles")` — `realm_access` is a nested object in the JWT, not a flat top-level claim. Passing a dotted path string silently produces zero granted authorities.</mark>

For client roles the nesting is one level deeper — retrieve `resource_access` as a map, then dig into the client-id sub-map to get `roles`.

---

### Read more

- [[RBAC in Keycloak grants access by mapping roles to users or groups inside a realm]]
- [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access]]
- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
