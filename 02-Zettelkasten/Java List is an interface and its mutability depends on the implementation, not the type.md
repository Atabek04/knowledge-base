---
created: 2026-06-03
tags: [java, collections, immutability]
aliases: [List implementations, unmodifiable list, List.of]
---

In Java, `List` is only an **interface**. It declares every operation — including `add()`, `remove()`, `set()` — but says nothing about whether they actually work. That is decided by the concrete **implementation** you hand it.

This is why a variable typed `List` gives no guarantee about mutability: the type carries the mutators regardless of what the object behind it allows.

```java
List<String> a = new ArrayList<>(); // mutable
List<String> b = List.of("x");      // immutable
// both are "List<String>" — the type can't tell them apart
```

---

### Mutable implementations

These store elements in a structure you can grow and shrink. `add()` / `remove()` work.

- **`ArrayList`** — backed by a resizable array; fast random access
- **`LinkedList`** — doubly-linked nodes; fast insert/remove at ends
- **`Vector`** — legacy, synchronized `ArrayList`

`new ArrayList<>()` is the default workhorse.

---

### Unmodifiable implementations — how they fail

The interface still has `add()`, so calling it **compiles**. The immutable implementation overrides that method to throw at runtime:

```java
List<String> list = List.of("a", "b");
list.add("c"); // ❌ UnsupportedOperationException — at runtime, not compile time
```

Two common ways to get one:

#### `List.of(...)` — standalone immutable (Java 9+)

Builds its own compact, truly immutable structure. No backing list exists — the elements are fixed at creation.

#### `Collections.unmodifiableList(original)` — a read-only *view*

Wraps an existing list. Read methods delegate to the original; every mutator is overridden to throw `UnsupportedOperationException`.

Because it's a **view**, changes to the *original* still show through:

```java
List<String> backing = new ArrayList<>(List.of("a"));
List<String> view = Collections.unmodifiableList(backing);

backing.add("b");  // ✅ mutating the original
System.out.println(view); // [a, b] — the view reflects it
```

`Arrays.asList(...)` is a third case — fixed-size: `set()` works but `add()`/`remove()` throw.

---

### A read-only view is not immutable — copy to detach

`Collections.unmodifiableList()` and `Arrays.asList()` hand back a **view**, not a snapshot: they share the original's backing data, so a mutation through any other reference still shows through (the `backing.add("b")` example above).

The view stops *you* from mutating; it does not detach the object from whoever else holds it.

To get a list no later mutation can touch, **copy** instead of wrapping — `List.copyOf(original)` builds a standalone immutable structure:

```java
List<String> snapshot = List.copyOf(backing);
backing.add("c");
System.out.println(snapshot); // unchanged — independent copy
```

Kotlin's read-only `List` has the [[Kotlin read-only List type omits mutators so the reference cannot modify the collection#Caveat — read-only is not immutable|exact same trap]] — read-only hides the mutators but does not detach the object.

---

### How Kotlin differs — type vs runtime

Java enforces read-only at **runtime** — the type still exposes `add()`, and you only discover the list is immutable when it throws.

Kotlin moves the guarantee to the **type system**. Its read-only `List` interface omits `add`/`remove` entirely, so misuse is a **compile error**, not a runtime exception.

<mark style="background: #ADCCFFA6;">Java: "the type allows it, the object might refuse." Kotlin: "the type doesn't even offer it."</mark>

(On the JVM, `listOf()` still returns a `java.util.List` under the hood — Kotlin's protection is the narrower *type*, not a different runtime object.)

---

### Read more

- [[Kotlin read-only List type omits mutators so the reference cannot modify the collection]]
- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Defensive copying prevents external mutation of internal state]]
- [[Java MOC]]
