TARGET DECK: Tech-KB::Python::Generators
Tags: python generator yield
**Related:** [[Python generator produces values one at a time on demand]] · [[yield in Python is one keyword with three different jobs]]

---

## yield — 3 jobs

START
Coding Questions
`yield` in Python has 3 jobs. What are they?
Back:
1. **Generator** — produce values one at a time, lazily
2. **Resource lifecycle** — split setup and teardown in a context manager
3. **Async streaming** — push chunks (SSE tokens) to a client as they arrive

Same keyword, three completely different use cases.
Tags: python yield
<!--ID: 1780311502646-->
END

START
Coding Questions
Job 1 — `yield` as a generator. What does it do and why use it?
Back:
Produces values **one at a time on demand** instead of building the full list in RAM.

```python
def count_up(n):
    for i in range(n):
        yield i   # hands i to caller, then pauses
```

- Calling `count_up(1_000_000_000)` runs **no code** — returns a generator object instantly
- Each `next()` runs until the next `yield`, returns the value, then freezes
- Memory: constant — only one value alive at a time

Use when reading once, top to bottom, on large data.
Tags: python yield generator
<!--ID: 1780311502667-->
END

START
Coding Questions
Job 2 — `yield` as resource lifecycle. What does it do?
Back:
Splits a context manager into **setup** (before `yield`) and **teardown** (after `yield`).

```python
@asynccontextmanager
async def lifespan(app):
    app.state.db = await connect()   # setup
    yield                            # caller runs here
    await app.state.db.close()       # teardown
```

- Everything before `yield` runs on enter
- `yield` hands control back to the caller (e.g. the app runs)
- Everything after `yield` runs on exit, even if an exception occurred

Used in `@asynccontextmanager` and FastAPI's `Depends()`.
Tags: python yield context-manager
<!--ID: 1780311502688-->
END

START
Coding Questions
Job 3 — `yield` as async streaming (SSE). What does it do?
Back:
In an `async def` function, each `yield` **pushes one chunk to the client immediately** without waiting for the full response.

```python
async def stream_response():
    async for token in llm.stream():
        yield f"data: {token}\n\n"  # sent to browser immediately
```

- `StreamingResponse` wraps this generator and calls `flush()` after each `yield`
- One token from LLM → `yield` → browser renders it live
- Users see the typewriter effect instead of waiting seconds for the full answer
Tags: python yield sse streaming
<!--ID: 1780311502709-->
END

---

## Generator mechanics

START
Coding Questions
What happens when you call a generator function?
Back:
**No code runs.** You get back a **generator object** immediately — the function body is frozen, waiting.

```python
def count_up(n):
    for i in range(n):
        yield i

gen = count_up(5)   # nothing executed yet
next(gen)           # NOW it runs — until first yield → returns 0
```

The generator object holds: local variables + position (which `yield` it's paused at).
Tags: python generator
<!--ID: 1780311502730-->
END

START
Coding Questions
How does `next()` drive a generator step by step?
Back:
```python
gen = count_up(3)

next(gen)   # runs → hits yield → returns 0, freezes
next(gen)   # resumes → returns 1, freezes
next(gen)   # resumes → returns 2, freezes
next(gen)   # nothing left → raises StopIteration
```

`for` loops call `next()` automatically and stop cleanly on `StopIteration`.

Each `next()` thaws the frozen frame, runs until the next `yield`, hands the value out, then freezes again.
Tags: python generator
<!--ID: 1780311502750-->
END

START
Coding Questions
What is a generator object internally?
Back:
A reference to a **frozen stack frame** on the heap.

Normally when a function returns, its frame is destroyed — locals gone, position gone. A generator **freezes** the frame instead of destroying it.

- Locals like `i` survive between iterations — sitting in the suspended frame
- `next()` thaws it, runs to the next `yield`, freezes again
- Frame is only freed when the generator is exhausted or garbage-collected
Tags: python generator internals
<!--ID: 1780311502771-->
END

START
Coding Questions
Why does a generator use constant memory regardless of how many values it produces?
Back:
Because it only ever holds **one value** alive at a time.

With a list of 1B integers:
- All 1B objects sit in RAM simultaneously (list holds a reference to each)

With a generator:
- After each `print(num)`, `num` rebinds → old integer's refcount → 0 → freed immediately
- Only one integer object alive at any moment

CPython's reference counting frees each object the instant nothing points to it.
Tags: python generator memory
<!--ID: 1780311502791-->
END

START
Coding Questions
When should you use a list instead of a generator?
Back:
| Need | List | Generator |
|---|---|---|
| Random access `nums[500]` | ✓ | ✗ forward-only |
| `len(nums)` | ✓ | ✗ unknown until exhausted |
| Iterate **twice** | ✓ | ✗ exhausted after first pass |
| Sort / reverse | ✓ | ✗ needs all values first |

**Rule:** generator when reading once, top to bottom, on large data. List when you need flexibility or the data is small.
Tags: python generator list
<!--ID: 1780311502812-->
END

START
Coding Questions
What iterator protocol methods does a generator object implement?
Back:
```python
gen.__next__()   # same as next(gen) — advance one step
gen.__iter__()   # returns itself — works in for loops directly
gen.close()      # force-stop; triggers GeneratorExit inside
```

Because it implements both `__iter__` and `__next__`, a generator **is** an iterator — it works anywhere an iterable is expected.
Tags: python generator iterator-protocol
<!--ID: 1780311502833-->
END

---

## Generator in SSE

START
Coding Questions
How does a Python generator map to SSE token streaming?
Back:
The generator **is** the SSE stream. Each `yield` = one event sent to the browser.

```python
async def agent_stream():
    async for token in llm.astream(prompt):
        yield f"data: {token}\n\n"   # SSE format

# FastAPI wraps it:
return StreamingResponse(agent_stream(), media_type="text/event-stream")
```

`StreamingResponse` drives the generator with `async for`, calling `flush()` after each `yield`. The generator pauses between tokens — no busy-waiting, no buffering.
Tags: python generator sse streaming fastapi
<!--ID: 1780311502854-->
END

START
Coding Questions
Why is a generator a natural fit for SSE — better than building a full list of tokens first?
Back:
**Memory:** tokens arrive one at a time from the LLM. A list would force you to wait for all tokens before sending anything — the generator lets you forward each one the moment it arrives.

**Latency:** with a list, the user waits for the entire response. With a generator, token 1 reaches the browser while token 2 is still being generated.

**Backpressure:** if the client is slow, the generator simply pauses at `yield` — it doesn't race ahead and pile up tokens.
Tags: python generator sse
<!--ID: 1780311502874-->
END

START
Coding Questions
What is an async generator, and how does it differ from a regular generator?
Back:
An **async generator** is a generator inside an `async def` function — it can both `yield` values and `await` async operations.

```python
async def stream():          # async def → async generator
    async for token in llm.astream():
        await asyncio.sleep(0)   # can await
        yield token              # can yield
```

- Regular generator: driven by `next()` / `for`
- Async generator: driven by `async for` / `__anext__()`
- FastAPI's `StreamingResponse` uses `async for` to drive it
Tags: python generator async sse
<!--ID: 1780311502895-->
END
