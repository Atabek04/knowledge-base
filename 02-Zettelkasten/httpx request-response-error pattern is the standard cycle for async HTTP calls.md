---
aliases: [httpx request, httpx error handling, httpx response]
tags:
  - python/http
---

> One async HTTP call follows three steps: send the request, read the response, handle failures. Each step has a correct form.

## Sending a Request

```python
async with httpx.AsyncClient(timeout=10) as client:
    response = await client.get(
        "https://service/api/profile",
        headers={"Authorization": f"Bearer {token}"},
        params={"page": 1},          # query string: ?page=1
    )

    response = await client.post(
        "https://service/api/data",
        json={"key": "value"},       # serialized to JSON body, sets Content-Type
        headers={"Authorization": f"Bearer {token}"},
    )
```

## Reading the Response

```python
response.status_code      # int: 200, 401, 502, ...
response.json()           # dict — parses JSON body
response.text             # str — raw body
response.headers          # dict-like

response.raise_for_status()  # raises HTTPStatusError if status >= 400
                              # silent on 2xx — call before reading body
```

Always call `raise_for_status()` before `response.json()` — avoids parsing error bodies as data.

## Error Handling — Senior Pattern

Catch from **specific → broad**. Each layer handles what it understands:

```python
# auth_client.py — production pattern
async def get_profile(self, token: str) -> dict:
    try:
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            response = await client.get(
                f"{self._base_url}/api/profile",
                headers={"Authorization": f"Bearer {token}"},
            )
            if response.status_code == 401:          # (1) known business case
                raise AuthenticationError("Token rejected by auth service.")
            response.raise_for_status()              # (2) any other 4xx/5xx
            return response.json()
    except (AuthenticationError, AppException):      # (3) re-raise own exceptions
        raise
    except httpx.TimeoutException:                   # (4) specific network failure
        logger.error("Auth service timed out on GET /api/profile")
        raise AuthServiceUnavailableError("Auth service timed out.")
    except Exception as exc:                         # (5) catch-all — never swallow
        logger.error("Auth service unreachable: %s", exc)
        raise AuthServiceUnavailableError()
```

### Why This Order

| Layer | What it catches | Why |
|-------|----------------|-----|
| `if status == 401` | Known business status | Needs a specific domain exception, not a generic HTTP error |
| `raise_for_status()` | All other 4xx/5xx | Fail fast — don't parse error bodies as success |
| `except (AuthenticationError, AppException)` | Your own exceptions | Re-raise immediately — don't wrap in a generic error |
| `except httpx.TimeoutException` | Timeout specifically | Deserves its own log message and error code |
| `except Exception` | Everything else | Always log before re-raising — never silently swallow |

### Rules

- **Never** `except Exception: pass` — always log + re-raise
- **Always** check known status codes (401, 403, 404) **before** `raise_for_status()` — gives precise domain errors
- **Always** log at the catch site with enough context (which endpoint, which user) — not inside the exception class
- **Always** raise a domain exception (`AuthServiceUnavailableError`) — never let raw `httpx` exceptions leak to the caller

## Related

- [[httpx.AsyncClient manages connection lifecycle as an async context manager]] — the `async with` wrapper
- [[httpx is a modern HTTP client for Python with async support]] — why httpx
