---
created: 2026-04-30
aliases: [nested try except, nested exception, fallback chain]
tags:
  - python/core
---

> Nest `try/except` when you have two independent failure points, each needing its own fallback. Each `except` only catches errors from its own `try` block.

```python
try:
    return primary_source()       # attempt 1
except SomeError:
    try:
        return secondary_source() # attempt 2
    except (OSError, KeyError):
        return default_value      # final fallback
```

### When to use

Use when attempts are **sequential and dependent** — attempt 2 only makes sense if attempt 1 failed.

### Java analogy

```java
try {
    return primarySource();
} catch (SomeException e) {
    try {
        return secondarySource();
    } catch (IOException | IllegalArgumentException e2) {
        return defaultValue;
    }
}
```

Identical pattern — Python just drops the exception type declarations.

---

Related:
- [[Python MOC]]
