---
created: 2026-06-03
tags: [java, oop]
aliases: [default equals, default hashCode, identity equality]
---

Every Java class inherits `equals()` and `hashCode()` from `java.lang.Object`. Knowing what they do *before* you touch them tells you whether you even need to override them.

By default, both methods are <mark style="background: #FFF3A3A6; font-weight: bold;">identity-based</mark> — they answer "is this the *same object in memory*?", not "do these two objects *mean* the same thing?".

---

### Default `equals()` — reference equality

`Object.equals()` is literally `==`:

```java
public boolean equals(Object obj) {
    return (this == obj);
}
```

It returns `true` only when both references point to the <mark style="background: #FFF3A3A6;">exact same instance</mark>.

```java
var a = new Point(1, 2);
var b = new Point(1, 2);

a.equals(b); // false — different objects, even with identical fields
a.equals(a); // true  — same reference
```

---

### Default `hashCode()` — identity hash

`Object.hashCode()` returns an int derived from the object's identity (typically related to its memory address). Two distinct instances almost always get <mark style="background: #FFF3A3A6;">different hash codes</mark>, even if every field matches.

```java
a.hashCode(); // e.g. 1829164700
b.hashCode(); // e.g. 2018699554  — different, despite equal fields
```

---

### When the default is fine

Keep the inherited behavior when each instance is genuinely <mark style="background: #ABF7F7A6;">unique by identity</mark>:

- **Entities with an identity that is the object itself** — a `Thread`, a DB connection, a running session
- **Mutable objects where two "equal" instances should still be distinguishable**

---

### When you must rewrite

Override both when the class is a <mark style="background: #BBFABBA6; font-weight: bold;">value object</mark> — equality should depend on *contents*, not identity:

- Used as a `HashMap` key or stored in a `HashSet`
- Money, `Point`, `Range`, DTOs, value types
- Anything you'd compare with "do these hold the same data?"

<mark style="background: #FF5582A6; font-weight: bold;">Never override one without the other.</mark> They are a pair — see [[Equal objects must return equal hash codes]].

Or skip the boilerplate entirely: [[Java records auto-generate accessor, equals, hashCode, and toString from their components]].

---

### Read more

- [[The equals contract requires reflexive, symmetric, transitive, and consistent]]
- [[Equal objects must return equal hash codes]]
- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Java MOC]]
