---
created: 2026-04-30
aliases: ["@field_validator", pydantic validator, mode before]
tags:
  - python/pydantic
---

> `@field_validator` registers a method as a hook Pydantic calls automatically when constructing a model. You never call it directly.

```python
from pydantic import field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    cors_allowed_origins: str = "http://localhost:3000"

    @field_validator("cors_allowed_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, v: object) -> object:
        if isinstance(v, str):
            return v.strip()
        if isinstance(v, list):
            return ",".join(v)
        return v
```

### Parameters explained

| Parameter | Meaning |
|---|---|
| `"cors_allowed_origins"` | Which field this validator targets. Can be multiple: `"field_a", "field_b"` |
| `mode="before"` | Runs **before** Pydantic type-coerces the value. Receives raw input (str, list, None…) |
| `mode="after"` | Runs **after** type coercion. Receives the already-converted typed value |

### Why `@classmethod` is required

The validator must be a `@classmethod` because it runs **before any instance exists** — there is no `self` yet. Pydantic calls it on the class directly. Without `@classmethod`, Pydantic raises an error.

### Method signature — `cls` and `v`

```python
def parse_cors_origins(cls, v: object) -> object:
#                      ^^^  ^
#                      |    the raw field value coming in
#                      the class (Settings) — needed for @classmethod protocol
```

- `cls` — the `Settings` class itself (standard `@classmethod` convention).
- `v` — the raw value Pydantic intercepted before assigning. Can be `str`, `list`, or anything the env provided.
- Return value becomes the new field value.

### `mode="before"` vs `mode="after"` — when to use which

- **`before`**: normalize messy input (strip whitespace, convert list → str, handle `None`). Use when the raw env value might not match the declared type yet.
- **`after`**: validate the already-typed value (check range, format, business rule). Use when you trust the type but need to verify the content.

---

Related:
- [[pydantic-settings reads env files and type-coerces automatically]]
- [[classmethod uses cls instead of self because it operates on the class not an instance]]
- [[Python MOC]]
