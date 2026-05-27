---
aliases: [kotlin open class, kotlin final default, allopen plugin, CGLIB proxy kotlin]
created: 2026-05-08
tags: [kotlin, spring, jvm, cglib, proxy]
---

Kotlin makes every class `final` by default — the opposite of Java, where classes are open unless marked `final`. To allow subclassing in Kotlin you must explicitly declare `open class`.

## Why Spring requires open classes

Spring uses **CGLIB** to proxy `@Configuration`, `@Service`, `@Component`, and similar annotated classes. CGLIB works by generating a *subclass* at runtime that intercepts method calls. If the class is `final`, CGLIB cannot subclass it → the proxy cannot be created → `@Bean` methods lose singleton enforcement (each call creates a new instance instead of returning the cached one).

```kotlin
// Without allopen: final by default → Spring fails at startup
@Configuration
class AppConfig {
    @Bean
    fun dataSource() = HikariDataSource() // called directly, no interception
}

// With open: CGLIB can proxy it
@Configuration
open class AppConfig {
    @Bean
    open fun dataSource() = HikariDataSource() // intercepted → singleton enforced
}
```

## Java vs Kotlin comparison

| | Java | Kotlin |
|---|---|---|
| Default | open (subclassable) | final (closed) |
| To prevent subclassing | `final class Foo` | nothing needed |
| To allow subclassing | nothing needed | `open class Foo` |

## The kotlin-allopen compiler plugin

Manually adding `open` to every Spring class is noisy and misleading. The `kotlin-maven-allopen` plugin (or Gradle equivalent) instructs the Kotlin compiler to automatically make `open` any class carrying a specified annotation. The Spring preset covers all Spring stereotype annotations.

```xml
<!-- pom.xml: activates allopen for all Spring annotations -->
<compilerPlugins>
    <plugin>spring</plugin>
</compilerPlugins>
<dependencies>
    <dependency>
        <groupId>org.jetbrains.kotlin</groupId>
        <artifactId>kotlin-maven-allopen</artifactId>
        <version>${kotlin.version}</version>
    </dependency>
</dependencies>
```

The transformation happens at **compile time** — the bytecode is correct (classes are open), but IntelliJ's static inspector reads source without running the compiler plugin and may still warn. Fix: reload Maven project in IntelliJ so it picks up the plugin config.

## Key rule

Never add `open` manually to Spring-annotated classes when allopen is configured — it is redundant and misleads readers into thinking the class is intentionally designed for inheritance.

---

Read more:
- [[Kotlin MOC]]
- [[01-MOCs/Frameworks/Spring Ecosystem - MOC.md]]