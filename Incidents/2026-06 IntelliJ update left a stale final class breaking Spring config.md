---
created: 2026-06-24
tags: [incident]
aliases: [stale IDE compile, allopen final class]
severity: low
status: resolved
---

> Two Spring startup errors appeared right after an IntelliJ update — both traced to stale compiled output, not the source or `pom.xml`.

---

### Symptom

App failed to start with `@Configuration class DictionaryClientConfig may not be final`. The `pom.xml` already had the Kotlin `allopen` plugin configured for `spring`, so the error and the config directly contradicted each other.

### Impact

Local dev only — app would not boot on one machine. No deployed environment affected.

### Investigation

The error blamed the code, but `allopen` was provably configured — so the evidence contradicted itself. When config says X and behavior says not-X, the fault is in the *state*, not the *source*.

Second clue: two separate errors appeared right after **one event** — the IDE update. Rather than two unrelated bugs, the question became "what single change produces both?" → corrupted build state.

Hypothesis with a prediction: "if this is stale output, a clean rebuild outside the IDE will succeed." Tested the cheapest option first — `mvn clean package` from the terminal, removing IntelliJ from the equation.

### Root cause

The IntelliJ update reset the Kotlin facet to **JVM 1.8**. While misconfigured, the IDE compiled `DictionaryClientConfig` *without* the `allopen` plugin, leaving a `final` `.class` in `target/`. Fixing the JVM target let the app start, but the bad `.class` from the earlier broken compile was still sitting there.

### Fix

`mvn clean` wiped `target/` and forced a fresh compile with the correct plugins. The final-modifier error vanished. `pom.xml` and the source were correct the entire time.

### Prevention

After any IDE update, distrust the IDE's incremental output: run `mvn clean package` from the terminal and "Invalidate Caches / Restart" before debugging a contradiction between config and behavior.

---

### Lessons

- **Config says X but behavior says not-X → suspect stale state** (caches, compiled output, IDE indices). `clean`, invalidate caches, rebuild. → [[Read the error message literally before forming any theory|read the error, then distrust it when it contradicts the config]]
- **Multiple symptoms sharing a timestamp → look for one upstream cause**, not many independent bugs.
- **Error blames your code but the code is provably correct → distrust the environment before yourself.** Bypass the suspected layer: running `mvn` from the terminal removed the IDE and isolated build-vs-tool.
- **Test the cheapest hypothesis first** — `mvn clean package` costs 30s and rules out a whole category; pasting the class was the fallback. Order tests by cost, not suspicion. → [[Debug by the scientific method observe hypothesize test repeat|a testable prediction, cheapest test first]]
- **One variable per experiment** — changed only the global compiler setting, not the facet too, so the result stayed unambiguous. → [[Change one variable at a time when debugging to keep cause and effect clear]]

### Read more
- [[Debugging & Troubleshooting - MOC]]
