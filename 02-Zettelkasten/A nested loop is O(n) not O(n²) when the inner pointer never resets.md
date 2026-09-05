---
aliases: [monotone pointer, amortized O(n), nested loop complexity]
---

The rule "nested loop = O(n²)" is a shortcut that only holds when the inner loop **resets** on every outer iteration. When the inner pointer is <mark style="background: #FFF3A3A6;">monotone</mark> — meaning it only moves in one direction across the entire function and never resets — the total inner work is bounded by `n`, not `n × n`.

### The amortized argument

Consider a [[Sliding Window scans contiguous subarrays in O(n) by reusing overlap instead of recomputing|sliding window]] with two pointers `l` and `r`:

```python
l = 0
for r in range(n):       # r moves forward: n steps total
    ...
    while condition:
        l += 1           # l moves forward: at most n steps TOTAL
```

`r` advances exactly `n` times.
`l` starts at 0 and can only move right — it travels at most `n` steps across the **entire function**, not per outer iteration.

```
Total work = n (outer) + n (inner, all iterations combined) = 2n = O(n)
```

The while loop looks expensive per outer step but it isn't — it's spending movement that was already "budgeted" by the array length.

### Credits analogy

Give every element 2 credits: one for when `r` enters it, one for when `l` exits it.
Each element spends both credits <mark style="background: #ABF7F7A6;">exactly once</mark> and is never touched again.
The while loop can only spend credits already deposited — it cannot charge the same element twice.
Total spend = 2n.

### Contrast with true O(n²)

```python
for i in range(n):
    for j in range(i, n):   # j resets to i on every outer iteration
        ...
```

Here `j` resets on every outer step, so the same elements are revisited repeatedly.
The inner pointer has no monotonicity guarantee — that's what makes it quadratic.

### The one rule

<mark style="background: #FFF3A3A6;">A nested loop is O(n) when the inner pointer is monotone across the entire function.</mark>
The bound comes from how far the pointer can travel end-to-end, not per outer step.

---

### Read more
- [[Sliding Window scans contiguous subarrays in O(n) by reusing overlap instead of recomputing]]
- [[Data Structures & Algorithms - MOC]]
