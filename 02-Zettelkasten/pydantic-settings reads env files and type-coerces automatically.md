---
created: 2026-04-30
aliases: [pydantic-settings, Settings class, BaseSettings]
tags:
  - python/pydantic
  - python/config
---

> `pydantic-settings` maps environment variables to a typed Python class. You declare the shape once; it reads, converts, and validates automatically.

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    clickhouse_host: str = "localhost"   # optional — has default
    openai_api_key: str                  # required — no default
    query_timeout: int = 30              # env var is a string; pydantic coerces to int
```

### What happens at startup

1. `BaseSettings` reads `.env` (or real env vars — same priority rules as the shell).
2. For each field: converts the raw string to the declared type (`"30"` → `int(30)`).
3. If a **required field** (no default) is missing → `ValidationError` at import time. Service never starts.

```
pydantic_core._pydantic_core.ValidationError: 1 validation error for Settings
openai_api_key
  Field required [type=missing, ...]
```

This is intentional — **fail fast** rather than crash later when the key is first used.

### Env var naming

By default, field name maps 1:1 to env var name (case-insensitive):
```
clickhouse_host  →  CLICKHOUSE_HOST  (or clickhouse_host)
openai_api_key   →  OPENAI_API_KEY
```

### Reading settings in FastAPI

```python
from functools import lru_cache

@lru_cache
def get_settings() -> Settings:
    return Settings()
```

`lru_cache` ensures the `.env` file is read once, not on every request.

---

### Java analogy

| Java/Spring                          | Python pydantic-settings            |
|--------------------------------------|-------------------------------------|
| `@Value("${key}")`                   | field with no default               |
| `@Value("${key:default}")`           | field with `= "default"`            |
| `application.properties` / `.yml`    | `.env` file                         |
| `@ConfigurationProperties`           | `BaseSettings` class                |
| Startup failure on missing property  | `ValidationError` — same behavior   |

---

Related:
- [[Python functions are standalone while methods are attached to objects]]
- [[field_validator runs before Pydantic assigns a field value]]
- [[Python MOC]]
