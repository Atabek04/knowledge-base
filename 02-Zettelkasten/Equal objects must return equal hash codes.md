---
created: 2026-06-03
tags: [java, oop, collections]
aliases: [hashCode contract, equals and hashCode together]
---

`hashCode()` has its own contract, and it is the bridge that links `hashCode()` to `equals()`. This is why the two methods must always be overridden together.

The binding rule: <mark style="background: #FFF3A3A6;">if two objects are equal, their hash codes must be equal.</mark>

---

### The hashCode contract

1. **Consistent** — called repeatedly on the same object, it returns the same int (as long as fields used in `equals()` don't change).
2. **Equal → equal** — `a.equals(b)` is `true` ⟹ `a.hashCode() == b.hashCode()`.
3. **Unequal → may collide** — unequal objects are <mark style="background: #ADCCFFA6;">not required</mark> to have different hash codes, but distinct codes improve hash-table performance.

Note the asymmetry: equal objects *must* share a hash; unequal objects *may* share one. <mark style="background: #FF5582A6;">Same hash code does NOT mean equal</mark> — it just means same bucket.

---

### Why override both — HashMap breaks otherwise

A `HashMap` finds a key in two steps: <mark style="background: #BBFABBA6;">hashCode picks the bucket, equals confirms the key</mark> inside it.

Override `equals()` but leave the identity `hashCode()` and you get this:

```java
var map = new HashMap<Point, String>();
map.put(new Point(1, 2), "origin-ish");

map.get(new Point(1, 2)); // null ❌
```

The lookup key is `equals()` to the stored key, but its identity hash points to a <mark style="background: #FF5582A6;">different bucket</mark>, so the map never even reaches the `equals()` check. The entry is effectively lost.

---

### Correct implementation

Use `Objects.hash()` for the common case — feed it the <mark style="background: #BBFABBA6;">same fields</mark> `equals()` compares:

```java
@Override public int hashCode() {
    return Objects.hash(x, y);
}
```

<mark style="background: #FF5582A6;">The fields in equals() and hashCode() must match.</mark> Compare on `x, y` but hash only `x` → still correct (equal objects share a hash), but more collisions. Hash a field `equals()` ignores → contract broken.

For a hot path, cache the result or hand-roll the `31 * result + field` form to avoid autoboxing in `Objects.hash`.

---

### Read more

- [[Object's default equals and hashCode are identity-based]]
- [[The equals contract requires reflexive, symmetric, transitive, and consistent]]
- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Java MOC]]
