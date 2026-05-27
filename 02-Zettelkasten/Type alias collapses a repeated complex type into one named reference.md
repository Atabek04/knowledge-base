## The Problem

Complex types written inline get repeated across many function signatures. Every repetition is a risk: one site gets updated, others don't.

```python
# WITHOUT alias — same complex type copy-pasted in 3 endpoints
async def get_status(token: RawTokenDep, agent_svc: Annotated[AgentService, Depends(get_agent_service)]):
async def agent_chat(req, current_user, token: RawTokenDep, agent_svc: Annotated[AgentService, Depends(get_agent_service)]):
async def complete_onboarding(token: RawTokenDep, agent_svc: Annotated[AgentService, Depends(get_agent_service)]):
```

## The Fix: Type Alias

```python
# dependencies.py — defined once
AgentServiceDep = Annotated[AgentService, Depends(get_agent_service)]

# router.py — used everywhere, one token
async def get_status(token: RawTokenDep, agent_svc: AgentServiceDep): ...
async def agent_chat(req, current_user, token, agent_svc: AgentServiceDep): ...
async def complete_onboarding(token: RawTokenDep, agent_svc: AgentServiceDep): ...
```

## What It Solves

| Problem | Without alias | With alias |
|---------|--------------|------------|
| Repetition | Full type in every signature | One name |
| Change propagation | Edit every site | Edit one definition |
| Readability | Noise at call sites | Intent is visible |

## Formal Syntax (Python 3.12+)

```python
type AgentServiceDep = Annotated[AgentService, Depends(get_agent_service)]
```

Before 3.12, simple assignment works fine — Python treats any assignment at module level as an alias when it's just a type expression:

```python
AgentServiceDep = Annotated[AgentService, Depends(get_agent_service)]  # works in 3.9+
```

## Java Equivalent

No direct equivalent — Java doesn't have type aliases. The closest is a dedicated wrapper class or `typedef`-like patterns via generics. Python's alias is zero runtime cost: it's just a name.

## Rule

If a type expression appears in more than one function signature → extract it to a named alias in `dependencies.py` or a dedicated `types.py`.

## Related

- [[FastAPI Depends wires service creation to endpoint function signatures]] — alias packages `Annotated[..., Depends(...)]` into one reusable name