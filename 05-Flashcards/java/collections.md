TARGET DECK: Tech-KB::Java::Collections
Tags: java collections
**Chapter:** Collections Framework
**Related:** [[Java MOC]]

---

START
Coding Questions
In Java, does the `List` type tell you whether a list is mutable?
Back: **No.** `List` is only an **interface** — it declares `add()`/`remove()`/`set()` regardless of whether they work. Mutability is decided by the **implementation**:
```java
List<String> a = new ArrayList<>(); // mutable
List<String> b = List.of("x");      // immutable
// both typed List<String> — indistinguishable
```
Tags: java collections
END

START
Coding Questions
Name the common mutable `List` implementations in Java.
Back:
- **`ArrayList`** — resizable array; fast random access (the default)
- **`LinkedList`** — doubly-linked nodes; fast insert/remove at ends
- **`Vector`** — legacy, synchronized `ArrayList`
Tags: java collections
END

START
Coding Questions
Why does calling `add()` on `List.of("a")` compile but then throw at runtime?
Back: The **interface** declares `add()`, so the call compiles. The immutable implementation **overrides** `add()` to throw:
```java
List<String> list = List.of("a");
list.add("b"); // ❌ UnsupportedOperationException — runtime, not compile
```
Java enforces read-only at **runtime**, not in the type.
Tags: java collections
END

START
Coding Questions
How is `Collections.unmodifiableList()` implemented, and how does it differ from `List.of()`?
Back:
- **`Collections.unmodifiableList(orig)`** — a read-only **view**: read methods delegate to `orig`, mutators throw. Changes to the **original still show through**.
- **`List.of(...)`** — a **standalone** immutable structure (Java 9+); no backing list, elements fixed at creation.
```java
var backing = new ArrayList<>(List.of("a"));
var view = Collections.unmodifiableList(backing);
backing.add("b");      // view becomes [a, b]
```
Tags: java collections
END

START
Coding Questions
How does Kotlin's read-only `List` differ from Java's unmodifiable list?
Back: It's **type vs runtime**:
- **Java** — the type still exposes `add()`; immutable impls throw at **runtime**
- **Kotlin** — read-only `List` omits `add`/`remove` from the type, so misuse is a **compile error**
> Java: "the type allows it, the object might refuse." Kotlin: "the type doesn't even offer it."
Tags: java collections
END

START
Coding Questions
`Collections.unmodifiableList(x)` is a view that still reflects changes to `x`. How do you get a list no later mutation can touch?
Back: **Copy, don't wrap.** A view shares the backing data; `List.copyOf()` builds a standalone immutable snapshot:
```java
List<String> snapshot = List.copyOf(backing);
backing.add("c");
System.out.println(snapshot); // unchanged
```
Same trap exists in Kotlin's read-only `List` — read-only hides mutators but doesn't detach the object.
Tags: java collections
END
