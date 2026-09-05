---
created: 2026-06-03
tags: [java, oop]
aliases: [equals contract, equals rules]
---

When you override `equals()` to compare by value, you must obey the <mark style="background: #FFF3A3A6;">general contract</mark> defined in `Object.equals()`. Break a clause and collections, sets, and any code relying on equality behave unpredictably.

The contract has five clauses. Mnemonic: an equality relation must be an *equivalence relation* (reflexive, symmetric, transitive) plus *consistent* and *non-null*.

---

### The five clauses

For non-null references `x`, `y`, `z`:

| Clause | Rule | Meaning |
|---|---|---|
| **Reflexive** | `x.equals(x)` is `true` | every object equals itself |
| **Symmetric** | `x.equals(y)` ⟺ `y.equals(x)` | order doesn't change the answer |
| **Transitive** | `x.equals(y)` ∧ `y.equals(z)` → `x.equals(z)` | equality chains |
| **Consistent** | repeated calls return the same result | unless a compared field changes |
| **Non-null** | `x.equals(null)` is `false` | never throw, never `true` |

---

### Where it usually breaks: symmetry

Mixing types or comparing across a subclass commonly violates <mark style="background: #FF5582A6;">symmetry</mark>:

```java
class CaseInsensitiveString {
    private final String s;

    @Override public boolean equals(Object o) {
        if (o instanceof CaseInsensitiveString cis)
            return s.equalsIgnoreCase(cis.s);
        if (o instanceof String str)               // ⚠️ trying to equal a String too
            return s.equalsIgnoreCase(str);
        return false;
    }
}

var cis = new CaseInsensitiveString("Hello");
var str = "hello";

cis.equals(str); // true
str.equals(cis); // false — String has no idea what CaseInsensitiveString is
```

<mark style="background: #FF5582A6;">Asymmetric.</mark> Put both in a list and `contains()` gives different answers depending on order. Fix: only ever compare against your own type.

---

### Inheritance breaks transitivity

There is <mark style="background: #FF5582A6;">no way</mark> to extend an instantiable class with a new value-carrying field and preserve the `equals` contract. The standard escape is <mark style="background: #ADCCFFA6;">favor composition over inheritance</mark> — hold the parent as a field instead of extending it.

---

### Practical recipe

1. `==` self-check (performance shortcut for reflexivity)
2. `instanceof` type check (handles non-null + wrong-type → `false`)
3. cast, then compare each <mark style="background: #BBFABBA6;">significant field</mark>
4. compare primitives with `==`, objects with `Objects.equals()`, floats with `Float.compare()`

```java
@Override public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Point p)) return false;
    return x == p.x && y == p.y;
}
```

<mark style="background: #FF5582A6;">Override `hashCode()` too</mark> — see [[Equal objects must return equal hash codes]].

---

### Read more

- [[Object's default equals and hashCode are identity-based]]
- [[Equal objects must return equal hash codes]]
- [[Java MOC]]
