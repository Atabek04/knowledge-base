---
created: 2026-04-30
aliases: [BaseModel, model_validate, model_dump, Pydantic serialization]
tags:
  - python/pydantic
---

> `BaseModel` is Pydantic's base class for typed data models. Inherit from it to get validation, serialization, and deserialization for free.

```python
from pydantic import BaseModel

class HintsResponse(BaseModel):
    hints: list[str]
```

### Two directions

```python
# Deserialization — dict → typed object
response = HintsResponse.model_validate({"hints": ["how many overdue?"]})

# Serialization — typed object → dict
response.model_dump()  # → {"hints": ["how many overdue?"]}
```

- **`model_validate(dict)`** — validates input against field definitions, raises `ValidationError` if invalid, returns a typed instance.
- **`model_dump()`** — converts the instance back to a plain Python dict.

Both are classmethods/instance methods inherited from `BaseModel` — you don't define them.

### Java analogy

| Pydantic | Java (Jackson) |
|---|---|
| `BaseModel` | `@JsonSerializable` POJO |
| `model_validate(dict)` | `objectMapper.readValue(json, MyClass.class)` |
| `model_dump()` | `objectMapper.writeValueAsString(obj)` |

---

Related:
- [[pydantic-settings reads env files and type-coerces automatically]]
- [[field_validator runs before Pydantic assigns a field value]]
- [[Python MOC]]
