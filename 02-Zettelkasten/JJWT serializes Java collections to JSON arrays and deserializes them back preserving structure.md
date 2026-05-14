---
aliases: [JJWT serialization, JWT claims List, JWT JSON array, JJWT claims map]
created: 2026-05-05
tags: [jwt, jjwt, serialization, kotlin, spring]
---

<mark style="background: yellow">JJWT serializes JWT claims to JSON when building a token and deserializes them back to Java/Kotlin objects when parsing. Java `List<String>` becomes a JSON array; when parsed, it comes back as `List<*>`.</mark>

### How auth-service stores roles

```kotlin
.claim("roles", user.roles.map { it.name })   // List<String> → stored in token
```

JJWT calls Jackson under the hood. `List<String>` → JSON array `["ADMIN", "MANAGER"]` embedded in the JWT payload.

---

### What you get back when parsing

```kotlin
val claims: Claims = Jwts.parser()...parseSignedClaims(token).payload
// Claims implements Map<String, Any>

claims["roles"]              // → Any?  (could be anything at compile time)
claims["roles"] as? List<*>  // → List<*>? — safe: JVM can check "is it a List?"
```

JJWT deserializes the JSON array back to `List<String>` internally, but the static type is `Any?` because `Claims` is `Map<String, Any>`. Generic type info (`<String>`) is erased at runtime — see star projection note.

---

### `Claims` is a `Map`

```java
public interface Claims extends Map<String, Object>, ClaimsMutator<Claims>
```

That's why `claims["iin"]` works — bracket access = `Map.get(key)`. Returns `Object` (Java) = `Any?` (Kotlin). Every value needs a cast.

---

### Primitive types

| Java/Kotlin type stored | JSON | Parsed back as |
|---|---|---|
| `String` | `"value"` | `String` |
| `Long` / `Int` | `123` | `Integer` or `Long` (Jackson decides) |
| `List<String>` | `["a","b"]` | `List<String>` (but typed as `Any?`) |
| `Boolean` | `true` | `Boolean` |

<mark style="background: pink">`Long` stored as a claim may come back as `Integer` if the value fits — always use `toLongOrNull()` rather than direct cast when reading numeric claims.</mark>

---

### Read more

- [[Kotlin star projection List<*> means element type is unknown at compile time]]
- [[Kotlin safe cast as? returns null instead of throwing ClassCastException]]
- [[Databases - MOC]]
