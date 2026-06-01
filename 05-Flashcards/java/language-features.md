TARGET DECK: Tech-KB::Java::Language Features
Tags: java features
**Chapter:** Language Features
**Related:** [[Java MOC]]

---

START
Coding Questions
What is `var` in Java and since which version?
Back: **`var`** — type inference for local variables, introduced in **Java 10**.

The compiler infers the type from the assigned value:

```java
var myVar = "A string!"; // compiler infers String
var count = 42;          // compiler infers int
```
Tags: java features type-inference
<!--ID: 1780311507433-->
END

START
Coding Questions
What is the limitation of `var` in Java?
Back: `var` can only be used for **local variables** — not for fields, method parameters, or return types.

```java
var name = "John"; // ✅ local variable
private var name;  // ❌ field — not allowed
```
Tags: java features type-inference
<!--ID: 1780311507453-->
END

START
Coding Questions
What does a Java record auto-generate for each component?
Back:
- **Accessor method** — `fieldName()` (no `get` prefix)
- **`equals()`** — compares all components by value
- **`hashCode()`** — derived from all components
- **`toString()`** — `RecordName[field1=..., field2=...]`
- **Canonical constructor** — takes all components as parameters

No setters generated — records are value carriers.
Tags: java records
<!--ID: 1780311507476-->
END

START
Coding Questions
How do Java record accessors differ from Lombok `@Getter`?
Back:
| | Naming | Example |
|---|---|---|
| **Record** | field name, no prefix | `acc.transactions()` |
| **Lombok** | `get` + capitalized field | `acc.getTransactions()` |

Both return the raw reference — no defensive copy by default.
Tags: java records lombok
<!--ID: 1780311507497-->
END

START
Coding Questions
Records have no setters — how do you "update" a record field?
Back: Create a new record instance:

```java
record Account(String owner, int balance) {}

var acc = new Account("Alice", 100);
var updated = new Account(acc.owner(), acc.balance() + 50);
```

No built-in `with` in the JDK yet — mutation = new instance.
Tags: java records
<!--ID: 1780311507518-->
END

START
Coding Questions
What does "shallowly immutable" mean for Java records?
Back: Record fields are `private final` — you **cannot reassign** them.
But `final` only locks the reference, not the object behind it.

If a field is a mutable type like `List`, the contents can still be modified:

```java
record Account(List<String> transactions) {}
acc.transactions().add("FAKE"); // ✅ compiles — record not truly immutable
```
Tags: java records immutability
<!--ID: 1780311507538-->
END

START
Coding Questions
What does `final` on a reference variable prevent — and what does it NOT prevent?
Back:
- **Prevents:** reassigning the variable to a different object
- **Does NOT prevent:** mutating the object the variable points to

```java
final List<String> list = new ArrayList<>();
list = new ArrayList<>(); // ❌ compile error
list.add("x");            // ✅ fine
```
Tags: java records immutability final
<!--ID: 1780311507559-->
END

START
Coding Questions
How do you make a Java record truly immutable when it has a List field?
Back: Use a **compact constructor** with `List.copyOf()`:

```java
record Account(List<String> transactions) {
    Account {
        transactions = List.copyOf(transactions); // defensive copy + unmodifiable
    }
}
```

`List.copyOf()` creates a new unmodifiable copy — mutation attempts throw `UnsupportedOperationException`.
Tags: java records immutability defensive-copy
<!--ID: 1780311507579-->
END
