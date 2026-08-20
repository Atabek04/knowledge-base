TARGET DECK: Tech-KB::Software Engineering::Debugging
Tags: debugging troubleshooting engineering
**Related:** [[Debugging & Troubleshooting - MOC]]

---

## Read the error literally

START
Coding Questions
Before forming any theory about a bug, what should you do first, and why?
Back:
**Read the error message literally, top to bottom.** The message usually already names the fault: exception type, message text, `file:line`, and the stack trace. Theorizing first means chasing a story instead of the evidence in front of you.

Litmus test: can you quote the exact exception type and line before proposing a fix? If not, you're guessing.
Tags: debugging mindset
<!--ID: 1787201882950-->
END

START
Coding Questions
In a Java/Spring stack trace, where is the real fault usually found, and why not the top line?
Back:
At the **bottom**, after the last `Caused by:`. Java and Spring wrap exceptions as they bubble up, so the top is often a generic wrapper (`ServletException`, `BeanCreationException`). The top line points at the symptom; the final `Caused by:` is the actual bug.
Tags: debugging mindset
<!--ID: 1787201882952-->
END

## Scientific method debugging

START
Coding Questions
What is the scientific method applied to debugging, and why does it beat random "try this, try that" changes?
Back:
The loop: **observe → hypothesize → predict → test → repeat.**

Each test rules a cause in or out, so the search space only shrinks. Random edits don't partition the possibilities — a fix that "works" leaves you unsure what worked or whether you just hid the bug.
Tags: debugging method
<!--ID: 1787201882955-->
END

START
Coding Questions
What makes a debugging hypothesis useful?
Back:
It must be **falsifiable** — a single test can disprove it.

✓ "The NPE happens because `user` is null on a cache miss" → predicts a concrete observation a log or breakpoint can confirm or kill.
✗ "Something's wrong with the cache" → nothing can refute it, so it can't guide a test.
Tags: debugging method
<!--ID: 1787201882957-->
END

## Change one variable at a time

START
Coding Questions
Why change only one variable at a time when debugging?
Back:
So cause and effect stay clear. If you change A and B together and the bug disappears, you can't tell whether:
- A fixed it and B did nothing,
- B fixed it and A did nothing, or
- one introduced a new bug that just *masks* the symptom.

The changes are **confounded** — their effects can't be told apart.
Tags: debugging mindset
<!--ID: 1787201882959-->
END

## Bisection

START
Coding Questions
What is bisection in debugging, and what is its time complexity advantage?
Back:
**Bi-section** = cut the suspect range in two. Find a known-good and known-bad point, test the midpoint, discard the half that's clean, repeat.

Each test halves the remaining suspects, turning an O(n) linear scan into **O(log n)** — e.g. 1000 candidates resolve in ~10 tests.
Tags: debugging method
<!--ID: 1787201882961-->
END

START
Coding Questions
Name three places the bisection technique applies.
Back:
- **Commits** — find a good and bad commit, test the middle (`git bisect` automates this).
- **A data pipeline** — at which stage does the value first go wrong?
- **Code** — comment out half the function; if the bug survives, that half is innocent.
- Also: config / dependency version bumps.
Tags: debugging method
<!--ID: 1787201882962-->
END

## Five Whys

START
Coding Questions
What is the Five Whys technique, who created it, and what is its goal?
Back:
A root-cause method created by **Sakichi Toyoda at Toyota** (core to the Toyota Production System / Kaizen).

Ask "why?" about the symptom, then "why?" about that answer, repeatedly, until you reach something **systemic you can fix** — not just the immediate technical glitch. "Five" is a guide, not a rule.
Tags: debugging root-cause
<!--ID: 1787201882965-->
END

START
Coding Questions
What is the main limitation of the Five Whys?
Back:
It follows a **single linear chain**, so it can miss a problem with multiple independent causes, and a careless analyst can steer the chain toward a predetermined conclusion.

Pair it with differential debugging (find *what* changed), then use Five Whys to ask *why* that change broke things.
Tags: debugging root-cause
<!--ID: 1787201882967-->
END

## Differential debugging

START
Coding Questions
When a system "worked yesterday but not today," what is the core question of differential debugging?
Back:
**What is different between the last-known-good state and now?**

The change is the prime suspect. Diff: deploys, config/env vars, dependency versions, data, infrastructure (expired cert, full disk), and traffic. Check the *boring, recent* change first.
Tags: debugging method
<!--ID: 1787201882969-->
END

## Rubber duck debugging

START
Coding Questions
Why does rubber duck debugging — explaining code aloud to an inanimate object — actually work?
Back:
Reading code, the mind silently glides over assumptions. Explaining **out loud** forces every silent assumption into an explicit sentence, and the step you can't say cleanly is where the bug hides.

The listener never answers — the value is entirely in the act of explaining. (Name from *The Pragmatic Programmer*.)
Tags: debugging method
<!--ID: 1787201882971-->
END
