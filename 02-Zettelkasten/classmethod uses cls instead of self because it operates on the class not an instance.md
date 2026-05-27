---
created: 2026-04-30
aliases: [@classmethod, cls vs self, class method]
tags:
  - python/oop
---

> A regular method receives the **instance** as its first argument (`self`).
> A `@classmethod` receives the **class itself** as its first argument (`cls`).

```python
class Dog:
    species = "Canis lupus"

    def bark(self):           # self = this specific dog object
        return f"{self} says woof"

    @classmethod
    def get_species(cls):     # cls = the Dog class itself
        return cls.species    # same as Dog.species
```

### Why use `@classmethod`

- You need to access or modify **class-level state**, not instance state.
- You want an **alternative constructor** — a factory that builds an instance differently.
- A **validator hook** registered by a framework (like Pydantic) must run without an instance existing yet.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @classmethod
    def from_string(cls, s: str) -> "Point":   # alternative constructor
        x, y = s.split(",")
        return cls(int(x), int(y))

p = Point.from_string("3,4")   # cls = Point; returns Point(3, 4)
```

### `cls` vs `self` — precise difference

| | `self` | `cls` |
|---|---|---|
| Refers to | the instance (`dog1`) | the class (`Dog`) |
| When available | after `__init__` runs | always — class exists before any instance |
| Decorator needed | none (default) | `@classmethod` |

---

### Java analogy

`@classmethod` ≈ `static` method in Java, **except** `cls` still lets you reference the class dynamically. A Java `static` method has no implicit class reference — you hardcode the class name.

```java
// Java static — hardcoded class
static Point fromString(String s) { return new Point(...); }

# Python classmethod — cls is dynamic, works with subclasses too
@classmethod
def from_string(cls, s): return cls(...)   # if subclassed, returns the subclass
```

---

Related:
- [[field_validator runs before Pydantic assigns a field value]]
- [[pydantic-settings reads env files and type-coerces automatically]]
- [[Python MOC]]
