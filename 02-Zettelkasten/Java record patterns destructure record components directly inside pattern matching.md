---
created: 2026-06-08
tags: [java, records, pattern-matching]
aliases: [record patterns, record destructuring]
---

[[Java instanceof pattern matching binds the checked type to a variable, eliminating the cast|instanceof pattern matching]] (Java 16) binds the whole object to a variable — you still need to call accessors to reach the components. Record patterns (Java 21) go one step further: they destructure the record's components directly inside the check.

```java
record Point(int x, int y) {}

// Java 16 — bind the record, then call accessors
if (obj instanceof Point p) {
    System.out.println(p.x() + p.y()); // two accessor calls
}

// Java 21 — destructure components directly
if (obj instanceof Point(int x, int y)) {
    System.out.println(x + y); // components bound inline
}
```

<mark style="background: #FFF3A3A6;">A record pattern `Point(int x, int y)` matches if the object is a `Point` **and** its components can be extracted into `x` and `y`.</mark>

---

### Nested patterns

Record patterns compose — a component can itself be a record pattern, letting you reach deep into a structure in one expression.

```java
record Address(String city, String country) {}
record Person(String name, Address address) {}

if (obj instanceof Person(String name, Address(String city, String country))) {
    System.out.println(name + " lives in " + city + ", " + country);
}
```

Without nested patterns this would require two `instanceof` checks and four accessor calls.

---

### In switch expressions

Record patterns are most powerful inside `switch`, where each branch can match a different shape:

```java
String describe(Object obj) {
    return switch (obj) {
        case Point(int x, int y) -> "point at " + x + ", " + y;
        case String s            -> "string: " + s;
        default                  -> "unknown";
    };
}
```

<mark style="background: #BBFABBA6;">Each `case` is a type check + destructuring in one line.</mark> The compiler enforces exhaustiveness — with sealed types, `default` can often be dropped entirely.

---

### Guard conditions

Add `when` to filter on component values after destructuring:

```java
String classify(Object obj) {
    return switch (obj) {
        case Point(int x, int y) when x == 0 && y == 0 -> "origin";
        case Point(int x, int y)                        -> "other point";
        default                                          -> "not a point";
    };
}
```

---

### Only works with records

<mark style="background: #FF5582A6;">Record patterns only work on `record` types</mark> — not on plain classes, even if they have the same field structure. The deconstruction relies on the canonical constructor contract that records guarantee.

---

### Read more

- [[Java instanceof pattern matching binds the checked type to a variable, eliminating the cast]]
- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Java records can implement interfaces but cannot extend classes or other records]]
