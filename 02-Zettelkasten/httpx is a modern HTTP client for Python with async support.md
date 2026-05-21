---
aliases: [httpx, python http client]
tags:
  - python/http
---

> `httpx` is a Python HTTP client that works both synchronously and asynchronously — drop-in replacement for `requests` with native `async/await` support.

## Why Not `requests`

`requests` is synchronous only — calling it inside `async def` blocks the event loop:

```python
# WRONG in async context
import requests
response = requests.get(url)   # blocks event loop thread
```

`httpx` provides the same API but with an async client:

```python
import httpx
response = await client.get(url)   # suspends coroutine, event loop stays free
```

## Sync vs Async Client

```python
# Sync — use in regular functions
with httpx.Client() as client:
    response = client.get(url)

# Async — use inside async def
async with httpx.AsyncClient() as client:
    response = await client.get(url)
```

## Java Analogy

| Java | Python |
|------|--------|
| `RestTemplate` | `httpx.Client` (sync) |
| `WebClient` (Spring WebFlux) | `httpx.AsyncClient` |

`httpx.AsyncClient` ≈ Spring's `WebClient` — non-blocking, returns a future/awaitable.

## Common Methods

```python
await client.get(url, headers={}, params={})
await client.post(url, json={}, headers={})
await client.put(url, json={})
await client.delete(url)

response.status_code     # int
response.json()          # dict
response.text            # str
response.raise_for_status()  # raises httpx.HTTPStatusError if 4xx/5xx
```

## Related

- [[httpx.AsyncClient manages connection lifecycle as an async context manager]]
