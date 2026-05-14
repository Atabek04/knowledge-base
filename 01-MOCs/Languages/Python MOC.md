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

## Data Structures

## Object-Oriented Programming

- [[classmethod uses cls instead of self because it operates on the class not an instance]]
- [[Underscore prefix marks private members by convention not enforcement in Python]]

## Async

- [[asynccontextmanager splits startup and shutdown logic at the yield]]
- [[await suspends a coroutine and returns control to the event loop until IO completes]]
- [[The event loop is a Python runtime scheduler that drives async concurrency on one thread]]
- [[A coroutine executes line by line and only yields at an await point]]

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

## Best Practices
