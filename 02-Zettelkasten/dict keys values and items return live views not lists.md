---
created: 2026-06-04
aliases: [dict views, dict items, dict keys, dict values]
tags:
  - python/core
---

A `dict` exposes its contents through three methods — `keys()`, `values()`, `items()` — and none of them returns a list. Each returns a <mark style="background: #FFF3A3A6;">**view object**: a live window into the dict that reflects later changes</mark>, costing no copy.

```python
d = {"a": 1, "b": 2}

d.keys()     # dict_keys(['a', 'b'])
d.values()   # dict_values([1, 2])
d.items()    # dict_items([('a', 1), ('b', 2)])

view = d.items()
d["c"] = 3
view         # dict_items([('a', 1), ('b', 2), ('c', 3)]) — view sees the new key
```

For a Java developer: same design as `map.keySet()` / `map.values()` / `map.entrySet()` — backed collections, not snapshots. `items()` is `entrySet()`, and each element plays the role of `Map.Entry`.

---

### items() yields tuples

Each element of `items()` is a <mark style="background: #BBFABBA6;">`(key, value)` [[A tuple is an immutable sequence whose fixedness makes it hashable|tuple]]</mark> — which is why the idiomatic loop uses [[Python for loop unpacks tuples into multiple loop variables|tuple unpacking]]:

```python
for key, value in d.items():
    print(key, value)
```

Looping the dict directly (`for k in d:`) yields keys only — `items()` is how you get both without a `d[k]` lookup per iteration.

---

### Snapshot with list()

Views are iterable but not indexable and not independent. <mark style="background: #8ED1FCA6;">Wrap in `list()` to get a real, detached list</mark>:

```python
list(d.keys())     # ['a', 'b', 'c'] — supports indexing, sorting, slicing
list(d.items())    # [('a', 1), ('b', 2), ('c', 3)] — list of tuples
```

Needed when you want `[0]` access, or to mutate the dict while iterating:

```python
for key in list(d.keys()):   # snapshot — safe
    if d[key] == 0:
        d.pop(key)           # RuntimeError if iterating the live view
```

<mark style="background: #FF5582A6;">Adding or removing keys while iterating a live view raises `RuntimeError: dictionary changed size during iteration`</mark> — the snapshot is the fix.

---

### Read more

- [[A tuple is an immutable sequence whose fixedness makes it hashable]]
- [[Python for loop unpacks tuples into multiple loop variables]]
- [[Python dict bracket access raises KeyError while get returns a default]]
- [[dict comprehension builds a transformed dict from any iterable inline]]
- [[Python MOC]]
