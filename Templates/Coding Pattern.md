---
aliases: []
---

<!-- TITLE = a complete statement naming the mechanic + payoff. e.g. "Sliding Window scans contiguous subarrays in O(n) by reusing overlap instead of recomputing" -->
<!-- This is the PATTERN concept note. Individual solved problems live as separate solve-logs in LeetCode-Log/ and are linked from the MOC, not here. -->

{{Intro: 1-2 lines. Use the pattern NAME to explain the mechanic, so the name itself is the recall hook.}}

### Trigger — when to reach for it

<mark style="background: #FFF3A3A6;">Recognition signals</mark> in the problem statement:

- {{data shape — e.g. array/string, contiguous}}
- {{keywords — e.g. "longest", "size K", "at most K distinct"}}
- {{brute-force cost it collapses — e.g. O(n²) all-subarrays → O(n)}}

### How it works

{{The core mechanic in 2-4 lines. Why reuse / which invariant is maintained.}}

### Variants

- <mark style="background: #ABF7F7A6;">**Variant**</mark> — when to use it

### Template

```
// language-neutral skeleton — the reusable shape, not a specific problem
```

### Complexity

- Time: {{ }}
- Space: {{ }}

### Pitfalls

- <mark style="background: #FF9D9DA6;">Common mistake:</mark> {{the usual bug — off-by-one, when to shrink, etc.}}

### Practice problems

<!--
  HOW TO POPULATE THIS SECTION:
  Run in terminal (from vault root):
    grep -rl 'topic:.*<pattern-tag>' "06-Planning/Trackers/LeetCode-Log/" --include="*.md" -l
  where <pattern-tag> is the topic tag used in LeetCode problem frontmatter (e.g. sliding-window, two-pointers).

  For each result, list: [[Problem Name]] — Easy/Medium/Hard
  Sort: Easy → Medium → Hard.
-->

- [[...]] — Easy

### Read more
- [[Coding Interview Patterns - MOC]]
- Related patterns:
    - [[...]]
