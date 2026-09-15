---
created: 2026-06-24
tags: [incident]
aliases: [stale IDE compile, allopen final class]
severity: low
status: resolved
---

> Two Spring startup errors appeared right after an IntelliJ update. Both came from stale compiled output, not from the source or the build file.

### Symptom

Startup failed with `@Configuration class ... may not be final`, while the build already applied the Kotlin `allopen` plugin for Spring. Config said X, behaviour said not-X.

### Root cause

The IDE update reset the Kotlin facet to JVM 1.8. While misconfigured, the IDE compiled the class without `allopen` and left a `final` `.class` in the output directory. Fixing the JVM target did not remove the stale class; `mvn clean package` from the terminal did.

### Where to look next time

- Config contradicts behaviour: suspect state (caches, compiled output, IDE indices) before source.
- Several symptoms sharing one timestamp: look for one upstream cause.
- Test the cheapest hypothesis first, and bypass the suspected tool (run the build from the terminal, not the IDE).

### Lessons

- [[Read the error message literally before forming any theory]]
- [[Debug by the scientific method observe hypothesize test repeat]]
- [[Change one variable at a time when debugging to keep cause and effect clear]]

### Read more
- [[Debugging & Troubleshooting - MOC]]
