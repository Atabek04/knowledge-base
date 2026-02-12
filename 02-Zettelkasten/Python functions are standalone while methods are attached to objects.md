---
created: 2026-02-12
aliases: [Function vs Method]
tags:
  - python/core
---

> A **function** is standalone — called by name.
> A **method** is attached to an object — called via dot notation.

```python
# Function — standalone
len([1, 2, 3])
print("hello")

# Method — belongs to an object
my_list.append(4)
"hello".upper()
```

A method is just a function that lives inside a class and operates on that class's data.

---

### In practice

`plt.plot()` — this is a **function** inside the `pyplot` module (not a method on an object).

`fig.savefig()` — this is a **method** on a Figure object.

Python uses both terms. The distinction matters when reading docs.

---

Read more:
- [[A Python module is a single file and a package is a folder of modules]]
- [[Python MOC]]
