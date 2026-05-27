---
aliases: [play with the variables, discover by manipulation]
created: 2026-05-23
tags: [learning, thinking, problem-solving, dsa]
---

### The idea

Before reaching for a solution, manipulate the objects in the problem.
Play with the variables, the inputs, the structures.

Manipulating them teaches you their <mark style="background: yellow">properties</mark> — and the properties point to the solution.

This is first principles thinking in action: you *discover* the method instead of memorizing it.

---
### Example: discovering binary search

Don't start by being told the algorithm.
Start with a sorted array and a target value.

Pick the middle element. Notice: if it's larger than the target, the target must be on the left; if smaller, on the right.
Half the array just became irrelevant.

Repeat that observation and you've reconstructed binary search — from the array's own property, *sortedness*, not from a memorized template.

<mark style="background: green">The sorted structure *was* the clue. Playing with it surfaced the algorithm.</mark>

---
### The same property, hidden in plain sight

Once you own the *property* instead of the code, you spot it everywhere.

Finding the moment a person appears in seven days of security footage is the same problem.
Before that moment every frame is a `0`; after it, every frame is a `1` — a sorted array in disguise.

So you binary-search the footage: jump to the middle, check which half the event is in, halve again.

<mark style="background: cyan">First principles let you recognize a solved problem wearing a different costume.</mark>

---
### Why this beats jumping to the answer

A memorized solution is brittle — change the problem slightly and it breaks.
A discovered solution comes with an understanding of *why* it works, so you can adapt it.

This is the same reason [[DSA mastery comes from recognizing patterns not memorizing individual solutions|pattern recognition]] beats grinding individual problems.

---
Read more:
- [[First Principles Thinking rebuilds understanding from fundamental truths instead of reasoning by analogy]]
- [[3-Pass Rule builds deep understanding of coding problems through attempt, study, and recall phases]]
- [[DSA mastery comes from recognizing patterns not memorizing individual solutions]]
