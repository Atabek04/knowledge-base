---
aliases: [JsonMergePatch, PATCH partial update, RFC 7396]
created: 2026-05-21
tags: [api, rest, http]
---

**PUT replaces the entire resource.** If a client sends only `{"email": "new@email.com"}` via PUT, every other field not included in the body is silently set to null.
This makes PUT dangerous for partial updates — it is semantically "replace", not "change".

**PATCH is the correct verb for partial updates.**
RFC 7396 defines `application/merge-patch+json` as the standard content type.
The server applies only the fields present in the patch document; absent fields are untouched.

```
PATCH /users/42
Content-Type: application/merge-patch+json

{"email": "new@email.com"}
```

Only `email` changes. `username`, `phone`, `address` — untouched.

**Spring implementation with `JsonMergePatch`:**
```java
@PatchMapping(value = "/users/{id}", consumes = "application/merge-patch+json")
public ResponseEntity<UserResponse> patchUser(
        @PathVariable Long id,
        @RequestBody JsonMergePatch patch) {

    User existing = userService.findById(id);
    UserRequest current = UserRequest.from(existing);

    JsonNode patched = patch.apply(objectMapper.valueToTree(current));
    UserRequest updated = objectMapper.treeToValue(patched, UserRequest.class);

    return ResponseEntity.ok(UserResponse.from(userService.update(id, updated)));
}
```

**Why it matters:**
- Accidental data loss from missing fields becomes structurally impossible
- Clients send minimal payloads — no need to fetch the full resource before changing one field
- `application/merge-patch+json` is the RFC standard — clients and proxies already understand it

---

**Read more:**
- [[Idempotency key prevents duplicate processing when clients retry failed requests]]
- [[API Design - MOC]]
