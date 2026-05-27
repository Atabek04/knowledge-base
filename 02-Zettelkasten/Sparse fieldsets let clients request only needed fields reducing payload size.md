---
aliases: [sparse fieldsets, field selection, fields query parameter]
created: 2026-05-21
tags: [api, rest, performance, mobile]
---

A list endpoint returns every field on every object, always.
A mobile client rendering a name list downloads 15 fields per record and discards 13 of them.
On slow connections, that wasted bandwidth adds up fast.

**Sparse fieldsets** expose a `?fields=` query parameter.
The server filters the response to include only the requested fields.
Clients that don't send the parameter receive the full response — backwards compatible by default.

```
GET /users?fields=id,name
[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
```

**Spring implementation:**
```java
@GetMapping("/users")
public ResponseEntity<Page<Map<String, Object>>> getUsers(
        Pageable pageable,
        @RequestParam(required = false) Set<String> fields) {

    return ResponseEntity.ok(userService.findAll(pageable).map(user -> {
        Map<String, Object> full = Map.of(
            "id",        user.getId(),
            "name",      user.getName(),
            "email",     user.getEmail(),
            "role",      user.getRole(),
            "createdAt", user.getCreatedAt()
        );
        if (fields == null || fields.isEmpty()) return full;
        return full.entrySet().stream()
            .filter(e -> fields.contains(e.getKey()))
            .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }));
}
```

**Why it matters:**
- Response size can drop 80%+ for field-heavy resources on mobile
- A single endpoint serves all clients — no endpoint proliferation per use case
- This is the core idea behind GraphQL applied to REST with one query parameter

---

**Read more:**
- [[API Design - MOC]]
