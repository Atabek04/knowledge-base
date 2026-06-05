---
created: 2026-06-04
aliases: [dict pop, pop with default, remove dict key]
tags:
  - python/core
---

`dict.pop(key)` does two things in one call: <mark style="background: #FFF3A3A6;">removes the key from the dict *and* returns its value</mark>. It's the read-and-delete operation — `del d[key]` only deletes, giving nothing back.

```python
d = {"a": 1, "b": 2}

value = d.pop("a")    # 1 — and "a" is gone
d                     # {"b": 2}

d.pop("z")            # KeyError — same loud failure as d["z"]
```

---

### The default argument

Like [[Python dict bracket access raises KeyError while get returns a default|get]], `pop` accepts a second argument that <mark style="background: #BBFABBA6;">replaces the `KeyError` with a fallback value</mark>:

```python
d.pop("z", 0)      # 0 — no exception, dict unchanged
d.pop("z", None)   # common "remove if present" idiom
```

This makes `pop(key, None)` the standard one-liner for *"delete the key if it exists, don't care if it doesn't"* — no `if key in d:` guard needed.

For a Java developer: `map.remove(key)` returns the value too, but has no default — Java gives `null` for absent keys, Python lets you choose.

---

### Sliding-window use

In a [[Counter counts hashable items and treats missing keys as zero|Counter]]-based sliding window, `pop` is how the window forgets a character whose count hit zero — decrementing alone leaves the key behind, and `len()` would still count it.

---

### Read more

- [[Python dict bracket access raises KeyError while get returns a default]]
- [[Counter counts hashable items and treats missing keys as zero]]
- [[Python MOC]]
