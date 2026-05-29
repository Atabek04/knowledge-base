---
created: 2026-04-30
aliases: [asynccontextmanager, lifespan, async context manager]
tags:
  - python/async
  - python/fastapi
---

> `@asynccontextmanager` turns a generator function into an async `with`-block. Code before `yield` = setup. Code after `yield` = teardown.

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP — runs once before first request
    app.state.db = await create_clickhouse_client(...)
    app.state.redis = await create_redis_client(...)

    yield   # app runs here, handling requests

    # SHUTDOWN — runs once after last request
    await app.state.db.close()
    await app.state.redis.aclose()

app = FastAPI(lifespan=lifespan)
```

FastAPI calls `lifespan` automatically — you never invoke it directly.

### Java analogy

| Java/Spring | Python |
|---|---|
| `@PostConstruct` | code before `yield` |
| `@PreDestroy` | code after `yield` |
| `@Bean(initMethod=..., destroyMethod=...)` | same pattern, one function |

---

Related:
- [[pydantic-settings reads env files and type-coerces automatically]]
- [[Python MOC]]
