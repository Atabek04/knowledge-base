---
created: 2026-02-19
aliases: [uv, uv package manager]
tags:
  - python/tooling
---

> **`uv` is a Python package and project manager written in Rust that replaces pip, virtualenv, pip-tools, and pyenv — all in one tool.**

Made by Astral, the same company behind the Ruff linter.

---

### Why use uv over pip?

- **10-100x faster** — parallel downloads + system-wide cache
- **All-in-one** — no need for separate virtualenv, pip-tools, pyenv
- **Cleaner uninstalls** — removes transitive dependencies that pip leaves behind
- **Better error messages** — easier to debug dependency issues
- **Fully compatible** — works with `requirements.txt` and the same package indexes as pip

---

### Quick comparison

| | pip | uv |
|---|---|---|
| Speed | Sequential installs | Parallel, cached |
| Scope | Install/uninstall only | Environments, locking, Python versions |
| Uninstall | Leaves orphan deps | Cleans up transitive deps |
| Ships with Python | Yes | No (separate install) |

---

Read more:
- [[Python virtual environments isolate project dependencies]]
- [[requirements.txt specifies Python package dependencies]]
