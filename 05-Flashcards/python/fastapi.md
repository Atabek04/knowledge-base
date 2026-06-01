TARGET DECK: Tech-KB::Python::FastAPI
Tags: python fastapi
**Chapter:** FastAPI
**Related:** [[Python MOC]]

---

START
Coding Questions
What is the difference between I/O-bound and CPU-bound work in Python async context?
Back:
- **I/O-bound** — thread is idle waiting for an external response (DB, Redis, HTTP). `async/await` exploits this: suspend and let others run.
- **CPU-bound** — thread is actively computing (PyTorch, compression, loops). No idle time. A coroutine with CPU work and no `await` **freezes the event loop**.

Fix for CPU-bound: `run_in_executor` — offload to a thread pool, event loop stays free.
Tags: python async concurrency
<!--ID: 1780311502915-->
END

START
Coding Questions
Why does calling a blocking function directly inside `async def` cause a problem?
Back: The event loop runs on **one thread**. A blocking call occupies that thread — no other coroutine can run until it returns.
```python
# WRONG — freezes all other requests for ~800ms
async def _flush(text):
    audio = tts_service.synthesize(text)  # blocking, no await
```
Fix: `await loop.run_in_executor(executor, tts_service.synthesize, text)`
Tags: python async concurrency event-loop
<!--ID: 1780311502936-->
END

START
Coding Questions
What does `loop.run_in_executor(executor, fn, *args)` do?
Back: **Submits `fn(*args)` to a thread pool** and returns an awaitable. The event loop suspends the coroutine and stays free while the thread runs `fn`.
- `executor=None` → asyncio default pool (`min(32, cpu_count + 4)` workers)
- `executor=ThreadPoolExecutor(max_workers=2)` → custom pool with cap
- `fn` must be a **sync callable**, not a coroutine
Tags: python async concurrency run-in-executor
<!--ID: 1780311502957-->
END

START
Coding Questions
Why use a custom `ThreadPoolExecutor(max_workers=2)` instead of the default pool for TTS?
Back:
- Each TTS thread holds **PyTorch model state in memory** — uncapped threads → memory explosion
- `max_workers=2` limits concurrent syntheses to 2 → controlled memory usage
- `thread_name_prefix="tts"` → threads appear as `tts_0`, `tts_1` in stack traces and profilers

Default pool (`None`) has up to 32 workers — too many for memory-heavy work.
Tags: python async concurrency thread-pool
<!--ID: 1780311502977-->
END

START
Coding Questions
Does Python's GIL prevent `ThreadPoolExecutor` from giving real concurrency for PyTorch/NumPy?
Back: No — C extensions like PyTorch and NumPy **release the GIL** during computation. Multiple threads run their C code simultaneously.
GIL only blocks pure Python bytecode. So `ThreadPoolExecutor` gives real parallelism for PyTorch TTS synthesis.
For pure Python CPU loops → use `ProcessPoolExecutor` (bypasses GIL via separate processes).
Tags: python concurrency gil thread-pool
<!--ID: 1780311502997-->
END

---

START
Coding Questions
What does `Depends(factory_fn)` do in a FastAPI endpoint signature?
Back: **Wires dependency injection** — FastAPI calls `factory_fn` before the endpoint runs and injects its return value.
- `Annotated[AgentService, Depends(get_agent_service)]` = type hint + wiring in one name
- Nested deps resolved automatically (graph walk per request)
Tags: python fastapi dependency-injection
<!--ID: 1780311503018-->
END

START
Coding Questions
Why put dependency factory functions in a separate `dependencies.py` instead of inside the router?
Back:
- **Eliminates duplication** — construction logic written once, reused across all endpoints
- **Keeps router thin** — endpoint body is one-liner delegation, not object-graph assembly
- **Easy test overrides** — `app.dependency_overrides[get_fn] = lambda: MockService()`
Tags: python fastapi dependency-injection
<!--ID: 1780311503038-->
END

START
Coding Questions
What is the Spring/Java equivalent of FastAPI's `Depends`?
Back: `@Bean` methods in a `@Configuration` class — Spring calls the factory and injects the result wherever `@Autowired` appears.
Difference: FastAPI resolves at **request scope** by default; Spring beans are typically **application scope**.
Tags: python fastapi dependency-injection java
<!--ID: 1780311503058-->
END

START
Coding Questions
How do you override a FastAPI dependency in tests?
Back: `app.dependency_overrides[original_dep_fn] = lambda: MockService()`
- Key = the original factory function
- Value = replacement callable returning the mock
- Reset after test: `app.dependency_overrides = {}`
Tags: python fastapi testing dependency-injection
<!--ID: 1780311503079-->
END

START
Coding Questions
In what order does FastAPI resolve nested dependencies?
Back: **Leaves first** — deepest dependency resolved before its dependents.
```
endpoint needs AgentService
  AgentService needs redis (RedisClientDep)
  → redis resolved first
  → then get_agent_service(request, redis) called
  → AgentService injected into endpoint
```
Tags: python fastapi dependency-injection
<!--ID: 1780311503104-->
END

START
Coding Questions
What problem does a type alias solve in FastAPI dependency signatures?
Back: **Eliminates repetition** — `Annotated[AgentService, Depends(get_agent_service)]` written inline in every endpoint becomes stale when the factory changes.
- Extract once: `AgentServiceDep = Annotated[AgentService, Depends(get_agent_service)]`
- Use everywhere: `agent_svc: AgentServiceDep`
- One edit site → all endpoints updated automatically
Tags: python fastapi type-alias dependency-injection
<!--ID: 1780311503128-->
END

START
Coding Questions
What is a Python type alias and what is its runtime cost?
Back: A **type alias** is a name assigned to a type expression at module level — zero runtime cost, it's just a name binding.
```python
AgentServiceDep = Annotated[AgentService, Depends(get_agent_service)]
# Python 3.12+ formal syntax:
type AgentServiceDep = Annotated[AgentService, Depends(get_agent_service)]
```
- No wrapper class, no overhead
- Java has no equivalent (closest: dedicated wrapper class or generic bounds)
Tags: python type-alias
<!--ID: 1780311503150-->
END