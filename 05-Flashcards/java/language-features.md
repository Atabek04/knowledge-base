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
END
