---
created: 2026-06-04
aliases: [dict access, dict get, KeyError, dict brackets]
tags:
  - python/core
---

A Python `dict` offers two ways to read a value, and they differ exactly in <mark style="background: #FFF3A3A6;">what happens when the key is missing</mark>: brackets raise, `get` returns a fallback.

```python
d = {"a": 1}

d["a"]          # 1
d["z"]          # KeyError!

d.get("z")      # None — no exception
d.get("z", 0)   # 0 — your own default
```

For a Java developer: `d["z"]` is the opposite of `map.get(key)` — Java returns `null` silently, Python fails loudly. Python's `d.get(key, default)` is `map.getOrDefault(key, default)`.

---

### Which to use

- <mark style="background: #BBFABBA6;">`d[key]` when the key *must* exist</mark> — a missing key is a bug, and the loud `KeyError` points straight at it
- `d.get(key, default)` when absence is a normal case you handle inline

Suppressing the error with `get` when the key should always be there hides bugs — you read `None` and crash three lines later with a worse message.

---

### When every missing key gets the same default

`get(key, 0)` on every access is a sign you want [[defaultdict creates and inserts a default value on first access to a missing key|defaultdict]] — it bakes the default into the dict itself. For counting specifically, [[Counter counts hashable items and treats missing keys as zero|Counter]] already treats missing keys as 0.

---

### Read more

- [[dict.pop removes a key and returns its value or a default]]
- [[defaultdict creates and inserts a default value on first access to a missing key]]
- [[Counter counts hashable items and treats missing keys as zero]]
- [[Python MOC]]
