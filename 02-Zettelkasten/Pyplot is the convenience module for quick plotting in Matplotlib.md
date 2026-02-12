---
created: 2026-02-12
aliases: [pyplot, plt]
tags:
  - python/libraries
---

> `pyplot` is a [[A Python module is a single file and a package is a folder of modules|module]] inside [[Matplotlib is a Python library for creating static and interactive visualizations|Matplotlib]] that provides a simple interface for creating plots.

```python
import matplotlib.pyplot as plt
```

`pyplot` is what you'll use 90% of the time. It lets you create charts in a few lines without manually managing figure and axis objects.

---

### Why not just `import matplotlib`?

`matplotlib` alone doesn't expose plotting [[Python functions are standalone while methods are attached to objects|functions]] directly. The plotting API lives inside `pyplot`.

Importing everything with `from matplotlib import *` would dump hundreds of names into your namespace — risking name collisions and making code harder to read.

<mark style="background: yellow">Import only what you need, give it a short alias.</mark>

---

### Other modules in Matplotlib

| Module | Purpose |
|---|---|
| `pyplot` | Quick plotting interface |
| `animation` | Animated charts |
| `image` | Image loading/processing |
| `colors` | Color maps and conversions |

---

Read more:
- [[Matplotlib is a Python library for creating static and interactive visualizations]]
- [[A Python module is a single file and a package is a folder of modules]]
- [[Python MOC]]
