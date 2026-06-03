---
aliases: [GoF, Gang of Four, GoF patterns]
---

A **design pattern** is a named, reusable solution to a problem that keeps recurring in object-oriented design. You don't copy code — you copy the *shape* of a proven solution.

The term went mainstream in 1994 with one book.

### The book

![[gof_design_patterns_book_cover.jpg]]

<mark style="background: yellow">**Design Patterns: Elements of Reusable Object-Oriented Software**</mark> (1994), written by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides.

Four authors → nicknamed the <mark style="background: yellow">**Gang of Four (GoF)**</mark>. The book itself is often just called "the GoF book."

### What's inside

It catalogs <mark style="background: cyan">23 patterns</mark> split into three families by *what they solve*:

- **Creational** → how objects get created (Singleton, Factory Method, Builder, …)
- **Structural** → how objects are composed into bigger structures (Adapter, Decorator, Facade, …)
- **Behavioral** → how objects communicate and divide responsibility (Strategy, Observer, Command, …)

### Why it matters

It gave engineers a <mark style="background: cyan">shared vocabulary</mark>. Saying "use a Strategy here" instantly communicates an entire design — no need to draw the whole class diagram.

<mark style="background: pink">Caveat:</mark> patterns are tools, not goals. Forcing a pattern where a plain function works is overengineering. A pattern earns its place only when the recurring problem actually shows up.

### Read more
- [[Design Patterns - MOC]]
