---
created: 2026-05-30
aliases: [C++ private header problem, C++ compile time headers, C++ header bloat]
tags:
  - software-design/principles
  - language-design
  - cpp
---

> To support `private` fields and inline methods, C++ required full class definitions in header files. This created a dependency problem that plagues large C++ codebases to this day.

### The mechanism

In C++, if you write:

```cpp
// person.h
class Person {
private:
    std::string name;  // private — but it's in the header
    int age;
public:
    const std::string& getName() const;
};
```

Every file that `#include`s `person.h` must see the full definition — including the private fields. The compiler needs to know the object's memory layout to allocate it on the stack.

### The consequence

- Changing a `private` field forces recompilation of every file that included the header
- Headers begin `#include`-ing other headers to satisfy private field types
- This cascades: one change → thousands of files recompile
- C++ build times in large codebases can exceed 30 minutes for this reason

### The irony

Private was introduced to *hide* implementation details from users. But the header system forces those details to be visible at compile time, even if they're inaccessible at runtime.

You pay the coupling cost (recompilation) without getting the safety (true hiding).

### The C contrast

[[C achieves data hiding by omitting struct definitions from headers|C's opaque pointer pattern]] avoids this entirely — users never see the struct layout, so changing internals requires zero user recompilation.

---

Read more:
- [[C achieves data hiding by omitting struct definitions from headers]]
- [[Private fields are a type-level fix for a module-level problem]]
- [[Software Engineering Principles - MOC]]
