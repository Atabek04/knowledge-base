---
aliases: [parameter vs argument, param vs arg]
created: 2026-06-10
tags: [java, fundamentals]
---

Every method call involves two distinct roles that share the same value but live at different points in the code.

<mark style="background: #FFF3A3A6;">Parameter</mark> — the named variable declared in the method signature. It's the **slot** that receives a value.

<mark style="background: #FFF3A3A6;">Argument</mark> — the actual value (or expression) you pass when calling the method. It's what **fills** the slot.

```java
// "platform" is the PARAMETER — declared in the signature
void install(String platform) { ... }

// "windows" is the ARGUMENT — passed at the call site
install("windows");
```

The names are often used interchangeably in conversation, but they mean different things: the parameter belongs to the method definition; the argument belongs to the call site.

<mark style="background: #FF5582A6;">Common mistake:</mark> saying "pass a parameter" — you pass an *argument*, you declare a *parameter*.

### Read more

- [[Java has 4 types of variables each with distinct scope and memory location|Four variable types: scope & storage]]
- [[Java MOC]]
