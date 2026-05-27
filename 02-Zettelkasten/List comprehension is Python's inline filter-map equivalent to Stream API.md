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
- [[Python MOC]]
