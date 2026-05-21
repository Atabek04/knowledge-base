FastAPI resolves dependencies declared in endpoint signatures before calling the handler. `Depends(factory_fn)` tells FastAPI: "call this factory, inject its return value here."

## The Pattern

```python
# dependencies.py — factory builds the full object graph
def get_agent_service(request: Request, redis: RedisClientDep) -> AgentService:
    settings = request.app.state.settings
    auth_client = AuthClient(settings.auth_service_url, settings.agent_http_timeout)
    tool_executor = ToolExecutor(auth_client=auth_client, ...)
    return AgentService(auth_client=auth_client, tool_executor=tool_executor, redis=redis, ...)

# Type alias — combines the type hint and the wiring in one name
AgentServiceDep = Annotated[AgentService, Depends(get_agent_service)]
```

```python
# router.py — endpoint declares what it needs, not how to build it
async def agent_chat(req: AgentChatRequest, agent_svc: AgentServiceDep) -> StreamingResponse:
    return StreamingResponse(agent_svc.stream_chat(req, ...))
```

## Resolution Order (per request)

```
HTTP request arrives
  → FastAPI reads endpoint signature
  → resolves nested deps first (redis before agent_service)
  → calls get_agent_service(request, redis)
  → injects AgentService into endpoint
  → endpoint runs
```

## Why a Separate `dependencies.py`?

Without it, every endpoint repeats the same 8-line construction block — that's duplication, and duplication rots. The factory centralises object-graph assembly in one place.

**Java/Spring analogy:** `@Bean` methods in a `@Configuration` class. Spring calls the factory, wires the result wherever `@Autowired` appears. FastAPI does the same at request scope instead of application scope.

## Key Rules

- `Annotated[Type, Depends(fn)]` — type hint tells the editor the type; `Depends` tells FastAPI how to produce it
- Nested dependencies are resolved automatically (FastAPI walks the graph)
- Override in tests: `app.dependency_overrides[get_agent_service] = lambda: MockAgentService()`
- Use `yield` inside a factory for cleanup (connection pools, DB sessions)

## Related

- [[pydantic-settings reads env files and type-coerces automatically]] — settings pulled from `request.app.state.settings`, often injected the same way
- [[Type alias collapses a repeated complex type into one named reference]] — `AgentServiceDep = Annotated[..., Depends(...)]` is a type alias