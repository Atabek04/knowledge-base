---
created: 2026-06-24
tags: [debugging/method]
aliases: [rubber duck debugging, rubber ducking]
---

You stare at code you're *sure* is correct, the bug invisible. Then a colleague walks over, you start explaining it line by line — and halfway through a sentence you stop and say "oh." You found it yourself; they said nothing. Rubber duck debugging turns that into a deliberate technique: explain the code, out loud, to an inanimate listener.

The name comes from *The Pragmatic Programmer*, where a developer carried a <mark style="background: #FFF3A3A6;">rubber duck</mark> and forced himself to explain his code to it line by line. <mark style="background: #FFF3A3A6; font-weight: bold;">The duck never answers — the value is entirely in the act of explaining.</mark>

---

### Why talking works

Reading code, your mind silently glides over assumptions — "this returns the user, obviously." Explaining *out loud* forces every silent assumption into an explicit sentence, and the moment you have to say <mark style="background: #ADCCFFA6;">"this returns the user, *unless* the cache missed, in which case—"</mark> the gap you skipped becomes audible. The bug lives in the step you couldn't say cleanly.

Verbalizing also slows you down and switches you from fast pattern-matching to deliberate, line-by-line reasoning.

---

#### What to explain

Walk through it stating, for each piece: what this line *should* do, and what it *actually* does with the real inputs. The mismatch is where the bug hides. <mark style="background: #BBFABBA6;">The listener can be anything</mark> — a literal duck, a colleague who just listens, a written-out message you never send, or an AI you narrate the problem to.

---

### Read more
- [[Debug by the scientific method observe hypothesize test repeat]]
- [[Read the error message literally before forming any theory]]
- [[Debugging & Troubleshooting - MOC]]

### Sources
- [Rubber duck debugging — Wikipedia](https://en.wikipedia.org/wiki/Rubber_duck_debugging)
- [Talk to the Duck — Michigan Tech Computing Blog](https://blogs.mtu.edu/computing/2024/08/21/talk-to-the-duck-the-rubber-duck-debugging-method/)
