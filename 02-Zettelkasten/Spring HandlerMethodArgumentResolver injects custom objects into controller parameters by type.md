---
aliases: [HandlerMethodArgumentResolver, custom argument resolver, controller param injection]
created: 2026-05-05
tags: [spring, kotlin, web-mvc, security]
---

<mark style="background: yellow">**`HandlerMethodArgumentResolver`** tells Spring MVC: "when you find this parameter type in a controller method, here's how to build its value." Spring calls your resolver automatically — the controller method never has to ask.</mark>

### The problem it solves

Without it, every controller method would extract `UserContext` manually from `SecurityContextHolder`. The resolver centralizes that once.

---

### Lifecycle — when does it run?

```
HTTP request arrives
  → Spring finds the matching controller method
  → Spring loops over the method's parameters
      → for each parameter: asks all registered resolvers "can you handle this?"
          → supportsParameter() returns true → call resolveArgument() → inject result
  → controller method executes with all arguments already built
```

<mark style="background: cyan">The resolver runs **before** your method body. By the time `generate(userContext, request)` executes, `userContext` is already fully populated.</mark>

---

### Two methods you implement

**`supportsParameter`** — filter. Spring has ~30 built-in resolvers (`@RequestBody`, `@PathVariable`, etc.). For every parameter, Spring asks each resolver: "is this yours?" You say yes only for `UserContext`:

```kotlin
override fun supportsParameter(parameter: MethodParameter): Boolean =
    parameter.parameterType == UserContext::class.java
```

**`resolveArgument`** — action. Runs only when `supportsParameter` returned `true`. Builds and returns the value Spring will inject:

```kotlin
override fun resolveArgument(
    parameter: MethodParameter,       // the parameter metadata
    mavContainer: ModelAndViewContainer?,  // model/view state — unused here
    webRequest: NativeWebRequest,     // raw HTTP request — unused here
    binderFactory: WebDataBinderFactory?, // data binding — unused here
): UserContext {
    val claims = SecurityContextHolder.getContext().authentication?.principal as Claims
    return UserContext(userId = ..., roles = ..., unitCode = ...)
}
```

The 4 params are the interface contract — other resolvers need them (e.g. one that reads from request headers). Here all data comes from `SecurityContext`, so they're unused.

---

### param vs arg

- **Parameter** — declared slot in the function definition: `fun generate(userContext: UserContext)`
- **Argument** — the actual value passed at the call site: `generate(resolvedContext, body)`

`HandlerMethodArgumentResolver` resolves the **argument** (value) for a handler **parameter** (slot).

---

### How `UserContextResolver` reads JWT claims

`JwtAuthenticationFilter` parses the Bearer token → stores `Authentication(principal = Claims)` in `SecurityContextHolder`. `Claims` is a `Map<String, Any>` (JJWT library), so bracket access works:

```kotlin
claims["iin"]       // → Any?  (map lookup)
claims["iin"] as? String  // → String? (safe cast — null if not a String)
```

`as Claims` on `authentication.principal` — <mark style="background: yellow">**`as`** is a **type cast**</mark>. `principal` is typed `Any?` in Spring Security. You know it's `Claims` because the filter put it there. `as` tells the compiler to treat it as `Claims`; throws `ClassCastException` at runtime if wrong.

---

### `requireValidClaim<T>` — generic null guard

```kotlin
private fun <T> requireValidClaim(value: T?, claimName: String): T =
    value ?: throw ReportException(...)
```

- `<T>` — works for any type (`Long`, `String`, etc.)
- `value: T?` — nullable in (claim might be absent)
- returns `T` (non-null) — `?:` either returns the value or throws

Purpose: same `?: throw` would repeat for every claim. One function, one error format, called 3 times.

---

### Registration (required)

```kotlin
@Configuration
class WebMvcConfig(private val userContextResolver: UserContextResolver) : WebMvcConfigurer {
    override fun addArgumentResolvers(resolvers: MutableList<HandlerMethodArgumentResolver>) {
        resolvers.add(userContextResolver)
    }
}
```

<mark style="background: pink">`@Component` alone is not enough — Spring doesn't auto-discover argument resolvers. Must be explicitly registered via `WebMvcConfigurer`.</mark>

---

### End result in controller

```kotlin
@PostMapping("/generate")
fun generate(userContext: UserContext, @RequestBody request: ReportRequest): ReportJobResponse =
    reportService.generate(userContext, request)
```

No annotation on `userContext`. Spring matches by type → resolver runs → value injected. Controller stays a one-liner.

---

### Read more

- [[Kotlin as keyword performs explicit type cast at runtime]]
- [[Spring Ecosystem - MOC]]
