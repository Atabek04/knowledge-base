---
created: 2026-04-30
aliases: [with statement, context manager, with as]
tags:
  - python/core
---

> `with` opens a context and guarantees its cleanup runs on exit — even if an exception is raised inside the block. `as` binds the resource to a name.

```python
with HINTS_PATH.open(encoding="utf-8") as f:
    data = json.load(f)
# file closed here automatically — even if json.load() raises
```

- `with` — opens the context, calls `__enter__()` on the object
- `as f` — binds the return value of `__enter__()` to `f`
- block exits — `__exit__()` is called regardless (success or exception)

### Without `with` — resource leak risk

```python
f = HINTS_PATH.open(encoding="utf-8")
data = json.load(f)   # raises → f.close() never called, file leaked
f.close()
```

### Java analogy

```java
try (var f = new BufferedReader(new FileReader(path))) {
    // f.close() called automatically on exit
}
```

`with` = `try-with-resources`. Identical guarantee, different syntax.

### Common uses

| Resource | Python |
|---|---|
| File | `with open(path) as f` |
| DB connection | `with get_db() as db` |
| Lock | `with asyncio.Lock() as lock` |
| HTTP client | `with httpx.Client() as client` |

---

Related:
- [[asynccontextmanager splits startup and shutdown logic at the yield]]
- [[Nested try-except creates a waterfall of fallbacks for independent failure points]]
- [[Python MOC]]
