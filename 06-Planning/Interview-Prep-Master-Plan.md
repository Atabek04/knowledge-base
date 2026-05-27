# Interview-Prep Master Plan — Mid-Level Java Backend

> The **methodology** behind the prep: four tracks, end-states, the daily workflow, and per-track Do/Don'ts. For *scheduling* (month → week, real dates) see the Ribaat-vault plan: `06-Planning/Job-Search/Interview-Prep-Execution.md`, which is subordinate to the six-pillar `2026-2027-Master-Plan`.
>
> ⚠️ **Reconciled 2026-05-27 (v2).** This doc was first drafted standalone at 18h/week / Senior. Against the candidate's real life (full-time work + Quran + Arabic + Mutqin + thesis + teaching), the locked reality is:
> - **Level:** mid-level ($40–70K), not senior — ~1y XP.
> - **Budget:** **~10h/week** — weekday *free-work-time only* + reclaimed weekend ML block. Not 18h.
> - **Timeline:** start June 2026, ramp top-priority Sept, offer target Dec 2026.
> - The end-states, estimates, daily workflow, and Do/Don'ts below remain valid — only the hours/week and calendar change (see the execution plan for the real schedule).
>
> **Weak areas:** DSA, Design Patterns, Behavioral · **Courses:** all owned (Grokking Patterns, Grokking System Design, Decode Coding Interview Java)

---

### The four tracks at a glance

| Track | MOC | Tracker | Flashcards |
|---|---|---|---|
| DSA / LeetCode | [[LeetCode - MOC]] | [[Grokking-Coding-Interview-Patterns - Tracker]] · [[Decode-Coding-Interview-Java - Tracker]] | `05-Flashcards/dsa/` |
| System Design | [[System Design - MOC]] | [[Grokking-System-Design - Tracker]] | `05-Flashcards/system-design/` |
| Design Patterns | [[Design Patterns - MOC]] | [[Design-Patterns - Tracker]] | `05-Flashcards/design-patterns/` |
| Behavioral | [[Behavioral Interview - MOC]] | [[Behavioral-Interview - Tracker]] | `05-Flashcards/behavioral/` |

---

## End-states (binary, testable)

Each track is "done" only when its end-state is provably true — no fuzzy "studied enough".

- **DSA** → NeetCode 150 complete (~143 problems in the MOC), each reviewed ≥2× via spaced repetition, **and** you can solve a *fresh* medium in < 35 min and explain it out loud.
- **System Design** → can design **8 standard systems** (URL shortener, rate limiter, key-value store, Twitter feed, chat/WhatsApp, notification service, YouTube, web crawler) **end-to-end in 45 min**, out loud, with back-of-envelope estimation and explicit trade-offs. Grokking 40 modules covered + 2 full mocks.
- **Design Patterns** → **8 core patterns implemented in Java** + explained ("when/why", not naming), remaining 15 GoF understood, 5 enterprise patterns implemented, can answer 5 scenario prompts out loud.
- **Behavioral** → **7-story STAR-L bank** covering all 8 competencies, each rehearsed to a 2-3 min spoken delivery, + company-research routine + negotiation script ready.

---

## Estimates — pre-buffer and post-buffer

Per-unit numbers are from the research brief (NeetCode timing, SD prep timelines, ~1-2h/pattern, story-bank rehearsal). A **25% buffer** is added to every track for illness, work crunch, and hard topics (graphs/DP, distributed consensus).

| Track | Work | Pre-buffer | **Post-buffer (+25%)** | Implied rate |
|---|---|---|---|---|
| DSA | 143 problems (first pass ~95h) + spaced review (~25h) | 120h | **150h** | ~8 problems/week over ~18 wks (~1.5/day) |
| System Design | 40 modules (~30h) + 8-10 designs (~10h) + 2-3 timed + 2 mocks (~10h) | 50h | **63h** | ~4 modules/week + 1 practice design/week over ~10 wks |
| Design Patterns | 8 core implemented (~12h) + 15 GoF (~11h) + 5 enterprise (~6h) + scenarios (~5h) | 34h | **42h** | ~4 patterns/week over ~8 wks |
| Behavioral | 7 stories drafted (~7h) + structure/mapping (~4h) + rehearsal (~12h) + research/negotiation (~5h) | 28h | **35h** | draft early, rehearse heavy near interviews |
| **Total** | | **232h** | **~290h** | |

**State both sides back:**
- DSA's end-state (143 problems + review) ÷ ~18 weeks of active solving = **~8 problems/week**. At your budget that's the backbone track.
- SD's end-state (40 modules + 10 designs) ÷ ~10 weeks = **~4 modules + 1 full design per week**.
- Patterns' end-state (33 patterns) ÷ ~8 weeks = **~4 patterns/week**, front-loaded on the core 8.
- Behavioral's end-state (7 rehearsed stories) spread across ~12 weeks = **draft ~1 story/week early, then rehearse**.

---

## Feasibility verdict

**~290 buffered hours ÷ 18h/week = ~16 weeks if 100% of your time went to these four tracks.**

It won't — you also need Java/Spring refresh, a portfolio project, and the application process itself. Assume ~14h/week reaches the four tracks (the rest covers Java refresh + portfolio + applying):

**~290h ÷ ~14h/week ≈ ~21 weeks ≈ ~5 months of focused work.**

Starting ~June 2026 → **interview-ready by ~late October / early November 2026**, with November for mocks + applications, and **first offer realistically December 2026 – February 2027.**

**Verdict on the Dec 2026 target:**
- ✅ **Achievable** as a *quality-first* path: ready ~Oct/Nov, applying Nov, offers landing Dec–Feb. This matches your "flexible / quality-first" choice.
- ⚠️ **Tight as a firm hard deadline.** A *guaranteed* signed offer by 31 Dec 2026 would require either more hours (~22h/week) or cutting scope (see below). The original `LeetCode - MOC` timeline (150 problems by **April 2027**) is *slower* than this plan and contradicts a Dec offer — that conflict is now resolved by the compressed 18h/week schedule below.

**If the date must harden to Dec 2026, cut in this order:**
1. Design Patterns Tier 2 (the 15 non-core GoF) → understand-only, skip implementing. Saves ~8h.
2. NeetCode hard problems (the ~10%) → skip until after first offer. Saves ~15h.
3. System Design real-world modules 26-40 → cover only the 8 end-state systems deeply, skim the rest. Saves ~12h.
- Do **not** cut: Behavioral (it's the leveling round) or DSA mediums + spaced review (the core of coding rounds).

---

## Calendar — sequencing the four tracks

Principle: **don't run all four in parallel** — 18h/week can't cover four tracks well at once. Two primary + one low-intensity track per phase.

Why this order:
- **DSA runs continuously** — it's the long pole (150h) and benefits most from spaced repetition stretched over months.
- **Design Patterns front-loaded** — small, you're weak on it, and it sharpens both your Java code and your system-design vocabulary, so it pays off downstream.
- **System Design mid-to-late** — recency matters; you want it freshest near interviews.
- **Behavioral spread thin throughout** — draft stories early while memory is fresh, rehearse heavily near interviews.

| Phase | Weeks | Primary (hrs/wk) | Secondary (hrs/wk) | Low-intensity (hrs/wk) |
|---|---|---|---|---|
| **A — Foundations** | Jun–Jul (8 wks) | DSA ~10h (Grokking patterns 1-9 + NeetCode easy/med) | Design Patterns ~6h (core 8 + enterprise) | Behavioral ~2h (draft 3 stories) |
| **B — Ramp** | Aug–Sep (8 wks) | DSA ~8h (med/hard: trees, graphs, DP + spaced review of A) | System Design ~8h (Grokking building blocks 1-25 + practice designs) | Behavioral ~2h (finish 7 stories, start rehearsal) |
| **C — Depth + mocks** | Oct (4 wks) | System Design ~8h (modules 26-40, timed designs, 2 mocks) | DSA ~6h (review + timed mock coding, remaining hard) | Behavioral ~4h (rehearse all 7, company research, negotiation) |
| **D — Apply** | Nov (4 wks) | Mock interviews (all tracks, timed) + applications | Portfolio polish | Behavioral final rehearsal |
| **Interviews** | Dec 2026 → | Active interviewing · first offer | | |

Design Patterns finishes in Phase A–B and then only resurfaces as flashcard review — that's intentional; it's the smallest track and an early multiplier.

---

## The daily per-unit workflow (the engine)

This is what you run **every study session**, for any track. It is the loop that turns a course module into knowledge that survives the forgetting curve. Skipping the note + flashcard + review steps is the #1 documented failure mode across all four tracks.

```
LEARN → ATTEMPT → ATOMIC NOTE → FLASHCARDS → SPACED REVIEW
```

1. **LEARN** — read the specific course module/page you're on. (Claude reads it with you and answers questions — per-unit, not pre-digested.)
2. **ATTEMPT** — *before* reading the solution: DSA → solve blind, 20-30 min timer; SD → sketch the design on paper, 10 min; Patterns → code the "without it" painful version; Behavioral → draft the story from memory.
3. **ATOMIC NOTE** — write one note per concept in `02-Zettelkasten/`, **in your own words**, complete-statement title, linked to its MOC + related notes. Follow `CLAUDE.md` conventions exactly.
4. **FLASHCARDS** — immediately add cards to the matching `05-Flashcards/{track}/{topic}.md` deck. Card the *idea/pattern*, never the full solution code.
5. **SPACED REVIEW** — re-attempt failed DSA problems after **3 days, then 7 days**; review Anki daily. Memory loses ~50% in a day, ~90% in a month without this.

Per track, the "ATTEMPT" step is non-negotiable — it creates the cognitive struggle that makes the rest stick.

---

## Per-track Do / Don't (from research)

### DSA
- ✅ Learn by **pattern**, not problem. Time-box (20 easy / 25-30 med / 40 hard), then study the solution. Spaced re-attempts. Talk solutions out loud.
- ❌ Memorize solutions. Grind all 150 with no review system. Jump to Hard early. Never time yourself.

### System Design
- ✅ Sequence fundamentals → framework → worked examples → mocks. Always do back-of-envelope estimation. **Lead and decide** (senior expectation). Practice out loud. State trade-offs explicitly.
- ❌ Force memorized templates. Name-drop tech you can't defend. Skip estimation. Endlessly enumerate options without committing.

### Design Patterns
- ✅ Implement each, then code the painful "without it" version. Learn trade-offs + alternatives. Tie each to a real Spring/framework example. Practice scenario answers out loud.
- ❌ Memorize UML without "when to apply". Over-apply ("pattern-itis"). Grind all 23 equally instead of 8 deep.

### Behavioral
- ✅ Build a 5-7 story bank, mapped to competencies. STAR-L (add Learning). Quantify results. Say "I". Prepare a real failure story. Research company values.
- ❌ Recite STAR robotically / one canned answer per question. Generic "we did X" with vague results. Skip company research. Wing the salary talk.

---

### Read more

- [[Remote-Job-Prep]]
- [[LeetCode - MOC]]
- [[System Design - MOC]]
- [[Design Patterns - MOC]]
- [[Behavioral Interview - MOC]]
- [[Senior Java-Kotlin Developer Roadmap]]
