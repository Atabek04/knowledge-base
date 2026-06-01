---
created: 2026-06-01
tags: [python, memory, cpython]
aliases: [Python name binding, Python variable reference semantics]
---

In Python, a variable is not a box that holds a value — it is a **name tag attached to a heap object**.

Assignment (`=`) binds a name to an object, not copies a value into a slot.

```python
x = [1, 2, 3]   # name 'x' bound to the list object
y = x            # name 'y' bound to the SAME list object
y.append(4)
print(x)         # [1, 2, 3, 4] — same object, both names see the change
```

### Rebinding vs mutating

Rebinding a name detaches it from the current object and attaches it to a new one.
The original object is untouched.

```python
x = 5      # 'x' → object 5
x = 10     # 'x' → object 10 (object 5 still exists until refcount hits 0)
```

Mutating an object changes the object itself — all names bound to it see the change.

### Contrast with Java

Java variables are also references to heap objects (for non-primitives) — same mental model.
The difference: Java's reference has a declared *type* that the compiler enforces.
Python's name binding is typeless — any name can be rebound to any object at runtime.

```python
x = 5        # x bound to int
x = "hello"  # x rebound to str — perfectly valid in Python
```

---

### Read more

- [[Python has no primitives because every value is a heap-allocated object]]
- [[CPython manages memory through reference counting with immediate deallocation]]
- [[Java objects always live on heap; reference location depends on declaration site]]
