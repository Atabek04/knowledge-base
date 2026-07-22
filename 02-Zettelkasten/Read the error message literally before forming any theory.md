---
created: 2026-06-24
tags: [debugging/mindset]
aliases: [read the error literally]
---

When something breaks, the instinct is to immediately guess at the cause — "oh, it's probably the cache again." But the error message and stack trace have usually already told you the file, the line, and the exact failure. Theorizing before reading them means chasing a story instead of the evidence sitting in front of you.

The discipline is simple: <mark style="background: #FFF3A3A6; font-weight: bold;">read the error message literally, top to bottom, before forming any theory.</mark>

---

### The message already names the fault

A good error tells you most of what you need:

- the **exception type** (`NullPointerException`, `ConnectionTimeoutException`) — the *category* of failure
- the **message text** — often the specific value or condition that broke
- the **`file:line`** — exactly where it threw
- the **stack trace** — the call path that led there

Most "mysterious" bugs stop being mysterious the moment you actually read all four instead of skimming the first word.

---

#### Read the whole cause chain, not just the top line

Java and Spring wrap exceptions as they bubble up. The top of the trace is frequently a generic wrapper (`ServletException`, `BeanCreationException`); the real fault is at the bottom, after the last <mark style="background: #FF5582A6; font-weight: bold;">`Caused by:`</mark>. Reading only the first line points you at the symptom, not the cause.

```
org.springframework.web.util.NestedServletException: Request failed
  ...
  Caused by: java.lang.IllegalArgumentException: amount must be >= 0   ← the actual bug
```

---

### Why we skip this step

- **Familiarity bias** — "I've seen this before" → assume it's the same cause and skip reading.
- **Noise aversion** — a 60-line stack trace looks like noise, so the eye slides past it.

Both feel faster and are almost always slower.

The litmus test: <mark style="background: #ADCCFFA6;">can you quote the exact exception type and line number before you propose a fix?</mark> If not, you're guessing, not debugging.

---

### Read more
- [[Debug by the scientific method observe hypothesize test repeat]]
- [[Differential debugging asks what changed since the system last worked]]
- [[Debugging & Troubleshooting - MOC]]
