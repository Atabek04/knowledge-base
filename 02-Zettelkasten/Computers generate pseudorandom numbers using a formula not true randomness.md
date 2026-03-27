---
created: 2026-03-27
aliases: [PRNG, Pseudorandom]
tags:
  - ml/fundamentals
---

> Computers can't generate truly random numbers — they use a **formula** called a pseudorandom number generator (PRNG).

### How it works

A PRNG takes a starting number (the **seed**), runs it through a mathematical formula, and produces an output. That output becomes the input for the next number, and so on. It's a chain reaction — deterministic, like a recipe.

<mark style="background: yellow">Same seed → same math → same sequence every time.</mark>

### Without a seed

When you call `random()` without setting a seed, Python automatically picks one from the **system clock** (current time in nanoseconds). Since the time changes every millisecond, you get a different seed each call — which gives a different sequence. That's why it *feels* random, but it's not.

```python
import random

# No seed — Python uses system clock, different each run
print(random.random())  # 0.7291... (varies)
print(random.random())  # 0.1483... (varies)
```

### With a seed

Setting a seed is like rewinding a tape to the same position. The sequence restarts identically every time.

```python
import random

random.seed(42)
print(random.random())  # always 0.6394267984578837
print(random.random())  # always 0.02501082869692039

random.seed(42)         # rewind to same starting point
print(random.random())  # 0.6394267984578837 again
```

<mark style="background: cyan">This is why [[random_state is a seed that makes random operations reproducible|random_state]] works — same seed forces the same sequence, making results reproducible.</mark>

---

Read more:
- [[random_state is a seed that makes random operations reproducible]]
- [[42 is not a special seed it is just a convention from pop culture]]
- [[Machine Learning MOC]]
