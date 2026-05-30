---
created: 2026-05-30
aliases: [getters setters antipattern, getter setter boilerplate]
tags:
  - software-design/principles
  - language-design
---

> Getters and setters are often cargo-culted from Java culture: "make everything private, expose via accessors" — taught as best practice without explaining why. In most cases, they add boilerplate with no real protection.

### The problem

```java
// What are you actually protecting here?
private String name;

public String getName() { return name; }
public void setName(String name) { this.name = name; }
```

The field is still fully readable and writable. You've added two methods and gained nothing.

### When getters/setters make sense

Only when the accessor does real work — validation, transformation, notification, lazy initialization. A passthrough getter is dead code.

```java
// This is justified — setter enforces an invariant
public void setAge(int age) {
    if (age < 0) throw new IllegalArgumentException();
    this.age = age;
}
```

### The deeper issue

The "make everything private" rule comes from a real concern: users of your code shouldn't depend on implementation details that might change.

But wrapping a field in a getter doesn't prevent that coupling — it just adds indirection. The field is still observable, just through a method call.

The real solution is controlling what gets *exposed at the module boundary* — not wrapping every field in a method.

---

Read more:
- [[Private fields are a type-level fix for a module-level problem]]
- [[Hyrum's Law states any observable behavior in a library will be depended on]]
- [[Software Engineering Principles - MOC]]
