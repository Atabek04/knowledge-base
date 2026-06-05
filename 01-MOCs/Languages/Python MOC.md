## Environment Management

- [[Python virtual environments isolate project dependencies|Virtual environments isolate project deps]]
- [[requirements.txt specifies Python package dependencies|requirements.txt lists package deps]]
- [[uv is a fast all-in-one Python package manager written in Rust|uv: fast all-in-one package manager (Rust)]]

## Libraries & Frameworks

- [[Pandas MOC]]
- [[Matplotlib is a Python library for creating static and interactive visualizations|Matplotlib]]
- [[Pyplot is the convenience module for quick plotting in Matplotlib|pyplot]]
- [[plt.scatter draws individual data points as dots on a chart|plt.scatter: individual dots]]
- [[plt.plot draws a line by connecting points in order|plt.plot: line connecting points]]
- [[plt.title, xlabel, and ylabel add text labels to a chart|plt.title / xlabel / ylabel: text labels]]
- [[plt.show renders and displays the chart on screen|plt.show: render the chart]]
- [[Scikit-learn provides ready-to-use ML algorithms and preprocessing tools|Scikit-learn]]

## Memory Model

- [[Python has no primitives because every value is a heap-allocated object|No primitives: every value is a heap object]]
- [[Python variables are name bindings to heap objects not value containers|Variables are name bindings, not containers]]
- [[CPython manages memory through reference counting with immediate deallocation|CPython: reference counting, immediate dealloc]]

## Core Concepts

- [[A Python module is a single file and a package is a folder of modules|Module = file; package = folder of modules]]
- [[Python functions are standalone while methods are attached to objects|Functions are standalone; methods attach to objects]]
- [[Generics parameterize a type so the container and its element type are both known|Generics parameterize container + element type]]

## Data Structures

- [[list.append adds to the end in O(1) while insert shifts every element after the index|list append vs insert — end is O(1), index shift is O(n)]]
- [[Python dict bracket access raises KeyError while get returns a default|dict access — brackets raise, get falls back]]
- [[dict.pop removes a key and returns its value or a default|dict.pop — remove + return, optional default]]
- [[dict keys values and items return live views not lists|dict views — live windows, list() to snapshot]]
- [[A tuple is an immutable sequence whose fixedness makes it hashable|tuple — immutable, therefore a valid dict key]]
- [[Counter counts hashable items and treats missing keys as zero|Counter — dict for counting, missing key reads 0]]
- [[defaultdict creates and inserts a default value on first access to a missing key|defaultdict — factory fills missing keys on access]]

## Object-Oriented Programming

- [[classmethod uses cls instead of self because it operates on the class not an instance|classmethod uses cls: operates on the class]]
- [[Underscore prefix marks private members by convention not enforcement in Python|Underscore marks private by convention]]

## Async

- [[The event loop is a Python runtime scheduler that drives async concurrency on one thread|Event loop: one-thread async scheduler]]
- [[A coroutine executes line by line and only yields at an await point|Coroutine yields only at await points]]
- [[await suspends a coroutine and returns control to the event loop until IO completes|await suspends until IO completes]]
- [[asynccontextmanager splits startup and shutdown logic at the yield|asynccontextmanager splits setup/teardown at yield]]
- [[asyncio.create_task schedules a coroutine to run concurrently without blocking the caller|create_task schedules a coroutine concurrently]]

## Concurrency

- [[IO-bound and CPU-bound work require different concurrency strategies|IO-bound vs CPU-bound: different strategies (GIL)]]
- [[run_in_executor offloads a blocking function to a thread pool without blocking the event loop|run_in_executor offloads blocking calls to a thread pool]]

## Functional Programming

- [[List comprehension is Python's inline filter-map equivalent to Stream API|List comprehension: inline filter-map (like Stream API)]]
- [[dict comprehension builds a transformed dict from any iterable inline|dict comprehension — transform, filter, invert dicts inline]]
- [[yield in Python is one keyword with three different jobs|yield: one keyword, three jobs]]
- [[Python generator produces values one at a time on demand|Generator: values one at a time, on demand]]
- [[Call stack is a LIFO structure that tracks active method frames|Call stack: LIFO of active frames]]
- [[A generator object is a suspended stack frame that resumes at yield|Generator object: a suspended frame resuming at yield]]
- [[Python for loop works with any iterable not just lists|for loop works on any iterable]]
- [[Python for loop unpacks tuples into multiple loop variables|for loop unpacks tuples into multiple variables]]
- [[enumerate yields index-value pairs so you never manage a counter manually|enumerate — index-value pairs, no manual counter]]
- [[A list holds all values in RAM even when you only process one at a time|A list holds all values in RAM]]
- [[Python range computes values on demand without storing them|range computes on demand, stores nothing]]
- [[range takes start stop step with stop always exclusive|range(start, stop, step) — stop always exclusive]]
- [[reversed iterates a sequence backward without index arithmetic|reversed() — backward values, no index math]]

## Standard Library

- [[Python sorted() returns a new sorted list while list.sort() mutates in place|sorted() returns new; list.sort() mutates]]
- [[Python sorted() key argument maps each element to the value used for comparison|sorted(key=...) maps elements to compare values]]

## File I/O

## Testing

## Pydantic

- [[Pydantic BaseModel provides serialization and deserialization via model_validate and model_dump|BaseModel: model_validate / model_dump]]
- [[pydantic-settings reads env files and type-coerces automatically|pydantic-settings reads .env and type-coerces]]
- [[field_validator runs before Pydantic assigns a field value|field_validator runs before field assignment]]

## Configuration & Settings

- [[pydantic-settings reads env files and type-coerces automatically|pydantic-settings: BaseSettings, .env, fail-fast]]
- [[field_validator runs before Pydantic assigns a field value|field_validator: mode before/after, cls + v]]

## Resource Management

- [[with-as is Python's try-with-resources that guarantees cleanup on exit|with-as: try-with-resources, guaranteed cleanup]]

## Error Handling

- [[Nested try-except creates a waterfall of fallbacks for independent failure points|Nested try-except: waterfall of fallbacks]]

## HTTP Clients

- [[httpx is a modern HTTP client for Python with async support|httpx: modern async HTTP client (vs requests)]]
- [[httpx.AsyncClient manages connection lifecycle as an async context manager|httpx.AsyncClient: lifecycle as async context manager]]
- [[httpx request-response-error pattern is the standard cycle for async HTTP calls|httpx send → read → error: the async HTTP cycle]]

## FastAPI

- [[FastAPI Depends wires service creation to endpoint function signatures|FastAPI Depends wires services into endpoints]]
- [[Type alias collapses a repeated complex type into one named reference|Type alias names a repeated complex type]]

## Best Practices
