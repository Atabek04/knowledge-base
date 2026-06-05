---
created: 2026-04-30
aliases: [list comprehension, Python list comprehension]
tags:
  - python/core
---

> List comprehension builds a new list inline — filter + map in one expression.

```python
[expression for item in iterable if condition]
#  ^ map        ^ loop                ^ filter (optional)
```

### Example

```python
[o.strip() for o in origins.split(",") if o.strip()]
# 1. split "http://a.com, ,http://b.com" → ["http://a.com", " ", "http://b.com"]
# 2. filter: skip empty/whitespace-only strings
# 3. map: strip whitespace from each kept item
```

### Explicit loop first, then collapse it

A comprehension is just a `for` loop that builds a list, <mark style="background: #FFF3A3A6;">rewritten as one expression</mark>. Write the explicit version when learning, then collapse it.

```python
# explicit — the mental model
result = []
for item in sorted_pairs[:k]:
    result.append(item[0])

# one-liner — same thing
result = [item[0] for item in sorted_pairs[:k]]
```

Read the one-liner by <mark style="background: #ABF7F7A6;">moving the trailing `for` to the front</mark>: "for each `item`, take `item[0]`". The output expression sits first; the loop and optional filter follow.

### Java Stream equivalent

```java
Arrays.stream(origins.split(","))
      .map(String::trim)
      .filter(s -> !s.isEmpty())
      .toList();
```

Same pipeline — Python puts the **map expression first**, filter last.

---

Related:
- [[Python functions are standalone while methods are attached to objects]]
- [[dict comprehension builds a transformed dict from any iterable inline]]
- [[Python MOC]]
