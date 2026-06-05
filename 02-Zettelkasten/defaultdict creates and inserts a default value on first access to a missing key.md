---
created: 2026-06-04
aliases: [defaultdict, default dict, collections defaultdict]
tags:
  - python/core
---

A plain `dict` raises `KeyError` on a missing key, forcing guard code (`if key not in d:` or `d.get(key, ...)`) before every accumulating update. `collections.defaultdict` removes the guard: <mark style="background: #FFF3A3A6;">on a missing key it calls a factory you provide, inserts the result, and returns it</mark>.

```python
from collections import defaultdict

counts = defaultdict(int)        # int() → 0
for char in "aab":
    counts[char] += 1            # no KeyError, starts from 0

groups = defaultdict(list)       # list() → []
for word in ["apple", "ant", "bee"]:
    groups[word[0]].append(word) # {'a': ['apple', 'ant'], 'b': ['bee']}
```

The name says it: a *dict* with a *default* for absent keys.

For a Java developer: this is `map.computeIfAbsent(key, k -> new ArrayList<>())` baked into the map itself.

---

### The factory is any zero-arg callable

You pass <mark style="background: #BBFABBA6;">the callable itself, not a value</mark> — `int`, `list`, `set`, or a `lambda: "N/A"` for custom defaults. defaultdict calls it once per missing key.

```python
d = defaultdict(lambda: "N/A")
d["missing"]    # "N/A"
```

---

### Access inserts — even reads

<mark style="background: #FF5582A6;">Merely reading a missing key inserts the default</mark> — `if d[key]:` silently grows the dict. Use `key in d` for pure membership checks.

This is the behavioral split from [[Counter counts hashable items and treats missing keys as zero|Counter]]: Counter returns 0 for a missing key *without* inserting it; defaultdict always inserts. For pure counting, prefer Counter — it's the specialized tool.

---

### Read more

- [[Counter counts hashable items and treats missing keys as zero]]
- [[Python dict bracket access raises KeyError while get returns a default]]
- [[Python MOC]]
