---
created: 2026-06-03
aliases: [sorted, sorted function, list.sort]
tags:
  - python/core
---

Python gives you two ways to sort, and the difference is *who gets changed*.

`sorted()` is a built-in function that takes any iterable and <mark style="background: #FFF3A3A6;">returns a brand-new sorted list</mark>, leaving the original untouched. `list.sort()` is a method on lists that <mark style="background: #FFF3A3A6;">sorts the list in place</mark> and returns `None`.

### sorted() — returns a new list

```python
nums = [3, 1, 2]
result = sorted(nums)   # [1, 2, 3]
print(nums)             # [3, 1, 2]  ← original unchanged
```

Because it returns a value, you can chain or assign it directly. It also accepts *any* iterable — a tuple, a set, dict keys, a generator — and always hands back a `list`.

```python
sorted("dcba")          # ['a', 'b', 'c', 'd']  — string → list of chars
sorted((3, 1, 2))       # [1, 2, 3]             — tuple → list
```

### list.sort() — mutates, returns None

```python
nums = [3, 1, 2]
nums.sort()             # returns None
print(nums)             # [1, 2, 3]  ← original changed
```

<mark style="background: #FF5582A6;">Common mistake:</mark> `x = nums.sort()` sets `x` to `None`, because `sort()` returns nothing. Use `sorted()` when you want a value back.

### The two arguments

Both share the same two keyword-only arguments:

- `reverse` — `True` sorts descending instead of ascending.
- `key` — a function that maps each element to the value used for comparison (its own note below).

```python
sorted([3, 1, 2], reverse=True)   # [3, 2, 1]
```

### Which to use

<mark style="background: #ABF7F7A6;">Use `sorted()` by default</mark> — it is safe, works on any iterable, and composes in expressions like list comprehensions. Reach for `list.sort()` only when the list is large and you genuinely want to avoid the extra copy.

---

### Read more

- [[Python sorted() key argument maps each element to the value used for comparison]]
- [[List comprehension is Python's inline filter-map equivalent to Stream API]]
- [[Python MOC]]
