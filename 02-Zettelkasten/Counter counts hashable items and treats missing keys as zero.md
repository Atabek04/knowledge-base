---
created: 2026-06-04
aliases: [Counter, collections Counter, frequency map]
tags:
  - python/core
---

Counting frequencies with a plain `dict` means guarding every increment against `KeyError`. `collections.Counter` is <mark style="background: #FFF3A3A6;">a `dict` subclass purpose-built for counting: missing keys read as `0`, so `counter[x] += 1` always just works</mark>.

```python
from collections import Counter

counts = Counter("aab")     # Counter({'a': 2, 'b': 1})
counts = Counter()          # empty, fill manually
counts["z"]                 # 0 — no KeyError
counts["z"] += 1            # increment from nothing
```

The name says it: a dict that *counts*.

For a Java developer: this replaces `map.merge(key, 1, Integer::sum)` over a `Map<K, Integer>`.

---

### It's still a dict

`Counter` inherits everything from `dict` — `len()`, `.items()`, `.pop()`, `in` all behave normally. <mark style="background: #8ED1FCA6;">`len(counter)` counts *distinct* keys, not total occurrences</mark> — which is exactly what a sliding window needs to know how many distinct characters it holds:

```python
window = Counter()
window[right_char] += 1
if len(window) > 2:              # more than 2 distinct chars
    window[left_char] -= 1
    if window[left_char] == 0:
        window.pop(left_char)    # shrink distinct count
```

<mark style="background: #FF5582A6;">Decrementing to 0 does NOT remove the key</mark> — `len()` still counts it. Pop zeros manually, as above.

---

### Reading a missing key does not insert it

`counts["z"]` returns 0 and <mark style="background: #BBFABBA6;">leaves the Counter unchanged</mark> — unlike [[defaultdict creates and inserts a default value on first access to a missing key|defaultdict]], which inserts the default on any access. Both live in `collections`; Counter is the specialized counting case, defaultdict the general "default for missing key" tool.

---

### Counting extras

- `counts.most_common(n)` — top-n `(item, count)` tuples, sorted by count
- `Counter(a) + Counter(b)` / `-` — merge or subtract counts
- `counts.total()` — sum of all counts (3.10+)

---

### Read more

- [[defaultdict creates and inserts a default value on first access to a missing key]]
- [[Python MOC]]
