---
aliases: [ETag, optimistic concurrency, If-Match, 412 Precondition Failed]
created: 2026-05-21
tags: [api, rest, http, concurrency]
---

**The lost update problem:** two clients load the same resource simultaneously.
Both modify it independently.
The second save silently overwrites the first — no error, no warning, data permanently lost.

**ETag (Entity Tag)** solves this with optimistic concurrency.
The server sends a version token in the `ETag` response header when serving a resource.
Clients include that token in the `If-Match` header when updating.
If the resource changed since the client loaded it, versions don't match → server rejects with **412 Precondition Failed**.

```
GET /products/1
→ ETag: "5"

PUT /products/1
If-Match: "5"
→ 200 OK (versions matched, update applied)

PUT /products/1
If-Match: "5"        ← stale, resource is now at version 6
→ 412 Precondition Failed
```

**Implementation:** map `ETag` to JPA's `@Version` field — no extra infrastructure needed.

```java
@GetMapping("/products/{id}")
public ResponseEntity<ProductResponse> getProduct(@PathVariable Long id) {
    Product product = productService.findById(id);
    return ResponseEntity.ok()
        .eTag("\"" + product.getVersion() + "\"")
        .body(ProductResponse.from(product));
}

@PutMapping("/products/{id}")
public ResponseEntity<ProductResponse> updateProduct(
        @PathVariable Long id,
        @RequestHeader("If-Match") String ifMatch,
        @Valid @RequestBody UpdateProductRequest request) {

    Product product = productService.findById(id);
    if (!("\"" + product.getVersion() + "\"").equals(ifMatch)) {
        return ResponseEntity.status(HttpStatus.PRECONDITION_FAILED).build();
    }
    return ResponseEntity.ok(ProductResponse.from(productService.update(id, request)));
}
```

**Why it matters:**
- Lost updates are silent without concurrency control — ETag makes version conflicts explicit
- 412 gives clients a clear signal: reload, resolve conflict, retry
- "Optimistic" means no locks held — works well for low-collision workloads
- GitHub, Google Drive, and most collaborative APIs use ETags — clients already know how to handle 412

---

**Read more:**
- [[PATCH with JsonMergePatch updates only the fields present in the request leaving others unchanged]]
- [[API Design - MOC]]
