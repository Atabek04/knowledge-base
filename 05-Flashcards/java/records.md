TARGET DECK: Tech-KB::Java::Records
Tags: java records
**Chapter:** Records
**Related:** [[Java MOC]]

---

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

START
Coding Questions
What is a Java record's **compact constructor** and why does it have no parameter list?
Back: It hooks into the auto-generated canonical constructor to **validate or normalize** components before they're assigned.
```java
record Account(List<String> transactions) {
    Account {                       // no ()
        transactions = List.copyOf(transactions);
    }
}
```
- **No `()`** — the record header already declares the parameters; the compact form receives them implicitly
- **No `this.x = x`** — at the end of the block the compiler auto-assigns each (possibly reassigned) parameter to its field
Tags: java records
<!--ID: 1782128729987-->
END

START
Coding Questions
How do you add a convenience constructor to a Java record, and what rule must it follow?
Back: Declare an additional constructor that calls `this(...)` as its **first statement** — delegating to the canonical constructor.

```java
record Account(String owner, int balance) {
    Account(String owner) {
        this(owner, 0); // must delegate to canonical
    }
}
```

**Why mandatory:** the canonical constructor is the only place field assignment happens. Skipping it leaves fields uninitialized. As a bonus, any compact constructor validation automatically applies to all paths.
Tags: java records constructors
<!--ID: 1782128729989-->
END

START
Coding Questions
Can a Java record extend a class or implement an interface?
Back:
- **Extend a class:** ❌ — records implicitly extend `java.lang.Record` and are `final`; no second superclass is allowed
- **Implement interfaces:** ✅ — any number of interfaces

```java
record Point(int x, int y) implements Describable {
    @Override
    public String describe() { return x + ", " + y; }
}
```

**Why final:** records are value types — subclassing would let a child add state and break `equals()` / `hashCode()`.
Tags: java records inheritance interfaces
<!--ID: 1782128729991-->
END

START
Coding Questions
Why are Java records a natural fit for DTOs?
Back: A DTO needs to hold data, compare by value, and stay immutable. Records provide all three out of the box:

| Need | What record provides |
|---|---|
| Hold data | `private final` component fields |
| Value equality | Auto-generated `equals()` / `hashCode()` |
| Immutability | No setters |
| Readability | Auto-generated `toString()` |

```java
record UserDto(String name, String email) {}  // replaces ~35 lines of boilerplate
```

**Caveat:** never use a record as a JPA `@Entity` — JPA requires a no-arg constructor.
Tags: java records dto
<!--ID: 1782128729994-->
END

START
Coding Questions
When should you pick `record` over Lombok `@Value`, and when does `@Value` still win?
Back:
**Prefer `record` when:**
- Java 16+ project
- No Lombok / reducing Lombok usage
- No need to extend a base class

**Prefer `@Value` when:**
- Need to extend a class (e.g. `BaseDto` with audit fields) — records cannot
- Pre-Java-16 codebase
- Framework requires `getName()`-style JavaBeans accessors

**Key difference:** `record` needs no external dependency; `@Value` requires Lombok but supports class inheritance.
Tags: java records lombok
<!--ID: 1782128729996-->
END

START
Coding Questions
What problem does Java record pattern matching solve over plain `instanceof` pattern matching?
Back: Plain `instanceof` binds the whole object — you still call accessors manually:

```java
if (obj instanceof Point p) {
    System.out.println(p.x() + p.y()); // accessor calls needed
}
```

Record patterns destructure components directly in the check:

```java
if (obj instanceof Point(int x, int y)) {
    System.out.println(x + y); // components bound inline
}
```

A record pattern matches if the object is the right type **and** its components can be extracted.
Tags: java records pattern-matching
<!--ID: 1782128729998-->
END

START
Coding Questions
How do you use nested record patterns in Java?
Back: A component can itself be a record pattern — lets you reach deep structure in one expression:

```java
record Address(String city, String country) {}
record Person(String name, Address address) {}

if (obj instanceof Person(String name, Address(String city, String country))) {
    System.out.println(name + " in " + city);
}
```

Without nesting: two `instanceof` checks + four accessor calls.
Tags: java records pattern-matching
<!--ID: 1782128730000-->
END

START
Coding Questions
How do record patterns work inside `switch` expressions?
Back: Each `case` combines a type check and destructuring in one line:

```java
String describe(Object obj) {
    return switch (obj) {
        case Point(int x, int y) -> "point at " + x + ", " + y;
        case String s            -> "string: " + s;
        default                  -> "unknown";
    };
}
```

Add `when` for guard conditions:
```java
case Point(int x, int y) when x == 0 && y == 0 -> "origin";
```
Tags: java records pattern-matching switch
<!--ID: 1782128730003-->
END
