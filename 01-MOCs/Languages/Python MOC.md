## Environment Management

- [[Python virtual environments isolate project dependencies]]
- [[requirements.txt specifies Python package dependencies]]
- [[uv is a fast all-in-one Python package manager written in Rust|uv]] — fast all-in-one replacement for pip, virtualenv, and pyenv

## Libraries & Frameworks

- [[Pandas MOC]]
- [[Matplotlib is a Python library for creating static and interactive visualizations|Matplotlib]]
- [[Pyplot is the convenience module for quick plotting in Matplotlib|pyplot]]
  - [[plt.scatter draws individual data points as dots on a chart|plt.scatter]] — draws individual dots
  - [[plt.plot draws a line by connecting points in order|plt.plot]] — connects points with a line
  - [[plt.title, xlabel, and ylabel add text labels to a chart|plt.title / xlabel / ylabel]] — add text labels
  - [[plt.show renders and displays the chart on screen|plt.show]] — render the chart on screen
- [[Scikit-learn provides ready-to-use ML algorithms and preprocessing tools|Scikit-learn]]

## Core Concepts

- [[A Python module is a single file and a package is a folder of modules]]
- [[Python functions are standalone while methods are attached to objects]]
- [[Generics parameterize a type so the container and its element type are both known]] — `list[str]`, `AsyncGenerator[str, None]`, Java analogy

## Data Structures

## Object-Oriented Programming

- [[classmethod uses cls instead of self because it operates on the class not an instance]]
- [[Underscore prefix marks private members by convention not enforcement in Python]]

## Async

- [[The event loop is a Python runtime scheduler that drives async concurrency on one thread]]
- [[A coroutine executes line by line and only yields at an await point]]
- [[await suspends a coroutine and returns control to the event loop until IO completes]]
- [[asynccontextmanager splits startup and shutdown logic at the yield]]
- [[asyncio.create_task schedules a coroutine to run concurrently without blocking the caller]] — fire-and-await-later; vs direct `await`

## Concurrency

- [[IO-bound and CPU-bound work require different concurrency strategies]] — async vs threads vs processes; GIL factor
- [[run_in_executor offloads a blocking function to a thread pool without blocking the event loop]] — `ThreadPoolExecutor`, custom pool, `max_workers`, Java analogy

## Functional Programming

- [[List comprehension is Python's inline filter-map equivalent to Stream API]]
- [[yield in Python is one keyword with three different jobs]]

## Standard Library

## File I/O

## Testing

## Pydantic

- [[Pydantic BaseModel provides serialization and deserialization via model_validate and model_dump]]
- [[pydantic-settings reads env files and type-coerces automatically]]
- [[field_validator runs before Pydantic assigns a field value]]

## Configuration & Settings

- [[pydantic-settings reads env files and type-coerces automatically]] — BaseSettings, .env, fail-fast on missing fields
- [[field_validator runs before Pydantic assigns a field value]] — @field_validator, mode before/after, cls + v params

## Resource Management

- [[with-as is Python's try-with-resources that guarantees cleanup on exit]]

## Error Handling

- [[Nested try-except creates a waterfall of fallbacks for independent failure points]]

## HTTP Clients

- [[httpx is a modern HTTP client for Python with async support]] — vs `requests`, sync/async, Java analogy
- [[httpx.AsyncClient manages connection lifecycle as an async context manager]] — context manager, per-request vs shared, exception hierarchy
- [[httpx request-response-error pattern is the standard cycle for async HTTP calls]] — send, read, error handling order, senior pattern

## FastAPI

- [[FastAPI Depends wires service creation to endpoint function signatures]] — `Depends`, `Annotated`, factory pattern, test overrides
- [[Type alias collapses a repeated complex type into one named reference]] — why aliases exist, `Annotated[..., Depends(...)]` pattern, Java comparison

## Best Practices
