---
created: 2026-06-01
tags: [python, memory, cpython]
aliases: [Python no primitives, Python everything is object]
---

In Python, **every value is a full object** — integers, booleans, strings, lists, class instances, functions.
There are no primitive types like Java's `int`, `boolean`, or `char`.

This means **every value lives on the heap** — always, with no exceptions.

```python
x = 5        # 5 is an object on the heap
y = True     # True is an object on the heap
z = "hello"  # "hello" is an object on the heap
```

### Contrast with Java

Java has a two-tier type system: primitives (stack-allocated) and objects (heap-allocated).

| Value | Java | Python |
|---|---|---|
| integer `5` | `int` primitive → stack | `int` object → heap |
| boolean | `boolean` primitive → stack | `bool` object → heap |
| text | `String` object → heap | `str` object → heap |

Python has no stack-allocated values at all.
Every `int`, every `str`, every `True` — all objects, all heap.

---

Because everything is a heap object, Python can treat all values uniformly.
You can call methods on integers (`(5).bit_length()`), pass any value as a function argument, and store any type in a collection — no boxing/unboxing required.

### Read more

- [[Python variables are name bindings to heap objects not value containers]]
- [[CPython manages memory through reference counting with immediate deallocation]]
- [[Java objects always live on heap; reference location depends on declaration site]]
