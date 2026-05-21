---
aliases: [AsyncClient, httpx AsyncClient, async http session]
tags:
  - python/http
---

> `httpx.AsyncClient` is an async HTTP session. Used as an `async with` context manager — it opens a connection pool on enter and closes it on exit.

## Basic Usage

```python
# auth_client.py:22
async with httpx.AsyncClient(timeout=self._timeout) as client:
    response = await client.get(
        f"{self._base_url}/api/profile",
        headers={"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    return response.json()
```

`async with` guarantees the connection pool is closed even if an exception is raised — same guarantee as `try/finally`.

## Key Constructor Parameters

```python
httpx.AsyncClient(
    timeout=10,           # seconds — applies to connect + read
    base_url="http://...", # prepended to all requests
    headers={},           # default headers for every request
)
```

## Per-Request vs Shared Client

`auth_client.py` creates a **new client per call** — fine for low-frequency calls (profile fetch, onboarding). The connection pool is short-lived.

For high-frequency calls (e.g. every chat message), create the client once and reuse:

```python
# Better for hot paths — reuses TCP connections
class SomeClient:
    def __init__(self):
        self._client = httpx.AsyncClient(base_url=base_url, timeout=10)

    async def close(self):
        await self._client.aclose()
```

Reusing a client = connection pooling = fewer TCP handshakes = faster.

## Exception Hierarchy

```python
httpx.TimeoutException      # connect or read timed out
httpx.ConnectError          # could not reach the server
httpx.HTTPStatusError        # raise_for_status() on 4xx/5xx
httpx.RequestError           # base for all request-level errors
```

`auth_client.py` catches `TimeoutException` separately to return a specific `502` error to the caller.

## `raise_for_status()`

```python
response.raise_for_status()
# raises httpx.HTTPStatusError if status >= 400
# silent if 2xx
```

Equivalent to Spring's `WebClient` `.retrieve().onStatus(...)` — fail fast on bad responses.

## Related

- [[httpx is a modern HTTP client for Python with async support]] — why httpx over requests
- [[httpx request-response-error pattern is the standard cycle for async HTTP calls]] — full request/response/error cycle
- [[with-as is Python's try-with-resources that guarantees cleanup on exit]] — `async with` follows the same protocol
- [[await suspends a coroutine and returns control to the event loop until IO completes]] — `await client.get()` is an I/O suspend point
