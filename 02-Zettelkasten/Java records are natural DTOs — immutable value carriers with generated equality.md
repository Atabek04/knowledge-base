---
created: 2026-06-08
tags: [java, records, dto]
aliases: [record DTO, records as DTOs]
---

A DTO (Data Transfer Object) is a plain container that moves data between layers — no business logic, just fields and equality. Records match that contract exactly, and provide everything a DTO needs with no boilerplate.

---

### Why records fit DTOs

| DTO requirement | What record provides |
|---|---|
| Hold data | Component fields, `private final` |
| Value equality | Auto-generated `equals()` / `hashCode()` |
| Readable output | Auto-generated `toString()` |
| No accidental mutation | No setters, immutable references |

The same DTO used to require Lombok or a full class:

```java
// Before — Lombok @Value
@Value
public class UserDto {
    String name;
    String email;
}

// After — Java record (Java 16+)
record UserDto(String name, String email) {}
```

Both produce identical behavior. The record needs no annotation processor.

---

### Jackson deserialization

Jackson supports records natively from version <mark style="background: #FFF3A3A6;">2.12</mark> (Spring Boot 2.5+). No extra configuration needed — Jackson reads the canonical constructor parameter names via reflection.

For older Jackson versions, annotate the canonical constructor:

```java
record UserDto(String name, String email) {
    @JsonCreator
    UserDto {}
}
```

---

### Records are not fit for JPA entities

<mark style="background: #FF5582A6;">Never use a record as a JPA `@Entity`.</mark> JPA instantiates entities via a no-arg constructor using reflection — records have no no-arg constructor, so the framework cannot create them.

Records belong at the layer boundary (controller ↔ service, service ↔ client), not in the persistence layer.

---

### Read more

- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Java records are shallowly immutable — final fields prevent reassignment but not mutation of mutable objects]]
- [[Java record is a dependency-free alternative to Lombok @Value for immutable value types]]
