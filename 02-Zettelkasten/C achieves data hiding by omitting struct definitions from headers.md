---
created: 2026-05-30
aliases: [C opaque pointer, C data hiding, opaque struct]
tags:
  - software-design/principles
  - language-design
  - c
---

> C has no `private` keyword, yet it achieves strong data hiding through a simple linker-level trick: forward-declare a struct in the header, define it only in the `.c` file. Users get a pointer they can't dereference.

### How it works

```c
// mylib.h — public header
typedef struct Context Context;  // forward declaration — size and fields hidden

Context* context_create(void);
void     context_destroy(Context* ctx);
int      context_run(Context* ctx);
```

```c
// mylib.c — private implementation
struct Context {
    int    state;
    char*  buffer;
    size_t size;
};
```

The caller can hold and pass a `Context*`, but can never access `.state` or `.buffer` — the compiler won't let them because the struct size and layout are unknown in the header.

### Why this is strong encapsulation

- Enforcement is at the **module boundary** (the linker), not the type system
- No special keywords needed
- Changing the struct internals never requires recompiling users — they never saw the definition

### Contrast with C++

C++ moved struct definitions *into* headers to support `private` keywords and inline methods. This broke the clean separation C had — users now must recompile when private fields change, even though they can't access them.

---

Read more:
- [[Private keyword in C++ created header dependencies and long compile times]]
- [[Private fields are a type-level fix for a module-level problem]]
- [[Software Engineering Principles - MOC]]
