---
created: 2026-06-08
tags: [java, records]
aliases: [record custom constructor, record convenience constructor]
---

A Java record auto-generates one canonical constructor — the one that takes every component. You can add extra constructors for convenience, but <mark style="background: #FFF3A3A6;">every non-canonical constructor must call `this(...)` as its first statement.</mark>

```java
record Account(String owner, int balance) {
    Account(String owner) {
        this(owner, 0); // delegates to canonical
    }
}

var acc = new Account("Alice"); // balance defaults to 0
```

---

### Why delegation is mandatory

The canonical constructor is the only place field assignment happens. Skipping it would leave fields uninitialized — Java doesn't allow that.

There is a second benefit: any [[Java records auto-generate accessor, equals, hashCode, and toString from their components#Compact constructor — validate and normalize components|compact constructor]] validation runs inside the canonical constructor. All paths — including convenience constructors — automatically pass through it.

```java
record Account(String owner, int balance) {
    Account {
        if (balance < 0) throw new IllegalArgumentException("negative balance");
    }

    Account(String owner) {
        this(owner, 0); // validation above runs on this path too
    }
}

new Account("Alice", -10); // ❌ IllegalArgumentException
new Account("Alice");      // ❌ same — canonical constructor always runs
```

<mark style="background: #FF5582A6;">You cannot bypass validation logic by adding a convenience constructor.</mark>

---

### Explicit canonical constructor

You can also write the canonical constructor explicitly — useful when the compact form's implicit assignment is not enough:

```java
record Account(String owner, int balance) {
    Account(String owner, int balance) { // explicit canonical — all components, exact types
        this.owner = Objects.requireNonNull(owner);
        this.balance = balance;
    }
}
```

Unlike the compact form, you must write every `this.field = param` assignment yourself — the compiler does not inject them.

---

### Read more

- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Java records are shallowly immutable — final fields prevent reassignment but not mutation of mutable objects]]
