---
created: 2026-06-08
tags: [java, pattern-matching, oop]
aliases: [instanceof pattern matching, pattern matching instanceof]
---

Before Java 16, checking an object's type and then using it required two steps: an `instanceof` check and a separate explicit cast. Pattern matching for `instanceof` collapses both into one.

```java
// Before Java 16 — check then cast
if (obj instanceof String) {
    String s = (String) obj; // redundant: compiler already knows it's a String
    System.out.println(s.length());
}

// Java 16+ — check and bind in one step
if (obj instanceof String s) {
    System.out.println(s.length()); // s is already bound, no cast needed
}
```

<mark style="background: #FFF3A3A6;">The binding variable `s` is introduced at the point of the type check — it only exists where the check is guaranteed true.</mark>

---

### Scope rules

The binding variable is in scope only where the check is provably true. The compiler enforces this statically.

#### Works with `&&` — right side is guarded

```java
if (obj instanceof String s && s.length() > 5) {
    // s is in scope — if we reach &&, the instanceof already passed
}
```

#### Does not work with `||` — right side is unguarded

```java
if (obj instanceof String s || s.length() > 5) { // ❌ compile error
    // s might not be bound if instanceof was false
}
```

---

### Negation and early return (flow typing)

<mark style="background: #BBFABBA6;">Inverting the check with `!` flips the scope</mark> — the binding is available *after* the block, not inside it. This enables clean early-exit patterns:

```java
if (!(obj instanceof String s)) {
    return; // or throw
}
// s is in scope here — compiler knows we only reach this line if instanceof passed
System.out.println(s.length());
```

This is called **flow typing**: the type narrows based on what the control flow proves must be true at that point.

---

### Foundation for record patterns

Plain `instanceof` pattern matching binds the whole object to a variable. [[Java record patterns destructure record components directly inside pattern matching|Record patterns]] go one step further — they destructure a record's components directly in the check, eliminating accessor calls as well.

---

### Read more

- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Java record patterns destructure record components directly inside pattern matching]]
