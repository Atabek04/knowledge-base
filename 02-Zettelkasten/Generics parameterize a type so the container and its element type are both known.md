---
aliases: [generics, generic types, type parameters, brackets in type hints]
tags:
  - python/types
---

> Generics let one class work with many types while still letting the type checker track *which* type it holds.

## The Problem Without Generics

```python
def get_items() -> list:   # a list of... what?
    return ["a", "b"]

items = get_items()
items[0].upper()           # type checker: no idea if this is valid
```

## With Generics

```python
def get_items() -> list[str]:
    return ["a", "b"]

items = get_items()
items[0].upper()           # ✓ type checker knows items[0] is str
```

The `[]` syntax **parameterizes** the generic — fills in the type variable.

## Java Analogy

```java
List<String> items = getItems();   // Java
```

```python
items: list[str] = get_items()     # Python — same idea, different syntax
```

| Java | Python |
|------|--------|
| `List<String>` | `list[str]` |
| `Map<String, Integer>` | `dict[str, int]` |
| `Optional<User>` | `User \| None` |
| `CompletableFuture<byte[]>` | `Awaitable[bytes]` |
| `Generator<String, Void, Void>` | `AsyncGenerator[str, None]` |

## Multiple Type Parameters

Some generics take more than one:

```python
dict[str, int]              # key type, value type
AsyncGenerator[str, None]   # yield type, send type
```

`AsyncGenerator[str, None]`:
- `str` — each `yield` produces a `str`
- `None` — nothing is `.send()`-ed into the generator (not used)

## What Happens If You Skip It

```python
def stream_chat(...) -> AsyncGenerator:       # vague
async for frame in stream_chat(...):
    frame.upper()  # type checker: unknown — no autocomplete, no error detection
```

Runtime is unaffected — Python ignores type hints at runtime. Only tooling (editors, `mypy`, `pyright`) uses them.

## Common Standard Library Generics

```python
list[str]
dict[str, int]
set[float]
tuple[str, int, bool]
Callable[[str, int], bool]   # args types, return type
AsyncGenerator[str, None]
Generator[str, None, None]   # yield, send, return
```

## Related

- [[Type alias collapses a repeated complex type into one named reference]] — aliases often wrap generics
- [[asyncio.create_task schedules a coroutine to run concurrently without blocking the caller]] — `AsyncGenerator` is the return type of async generators
