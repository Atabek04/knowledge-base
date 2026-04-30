---
created: 2026-04-30
aliases: [underscore prefix, private python, _field, __field]
tags:
  - python/core
  - python/oop
---

> Python has no `private` keyword. Underscore prefix is a gentleman's agreement — "don't touch this from outside the class." Nothing stops you, but you're breaking the contract.

```python
class MyService:
    _client = None       # private by convention — internal use only
    __secret = "key"     # name-mangled — Python renames to _MyService__secret
    public_field = "ok"  # no prefix — fair game
```

### Two levels

| Prefix | Name | Enforcement |
|---|---|---|
| `_field` | private by convention | none — just a signal |
| `__field` | name-mangled | Python renames it → harder (not impossible) to access from outside |

```python
obj = MyService()
obj._client       # works — just rude
obj.__secret      # AttributeError
obj._MyService__secret  # works — but now you're really being rude
```

### Java analogy

`_field` ≈ `private` in Java — except Java enforces it at compile time. Python trusts you.

---

Related:
- [[classmethod uses cls instead of self because it operates on the class not an instance]]
- [[Python MOC]]
