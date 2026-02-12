---
created: 2026-02-12
aliases: [Python Module, Python Package]
tags:
  - python/core
---

> A **module** is a single `.py` file.
> A **package** is a folder containing modules (with an `__init__.py` file).

The term **library** is informal — it usually means a package you install via `pip`.

```
matplotlib/          ← package (folder)
    __init__.py
    pyplot.py        ← module (file)
    animation.py     ← module (file)
```

When you write `import matplotlib.pyplot`, you're saying: from the `matplotlib` folder, import the `pyplot` file.

---

### Creating your own module

Any `.py` file is already a module. Save functions in `helpers.py`, then:

```python
import helpers
helpers.my_function()
```

To make a package, create a folder with `__init__.py` inside it.

---

Read more:
- [[Python functions are standalone while methods are attached to objects]]
- [[Python MOC]]
