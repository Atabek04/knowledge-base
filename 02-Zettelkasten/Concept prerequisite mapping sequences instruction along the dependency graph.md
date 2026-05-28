---
aliases: [Concept Prerequisite Mapping, Prerequisite Mapping, Learning Hierarchy, Gagné]
created: 2026-05-28
tags: [pedagogy, curriculum-design, instructional-design, learning]
---

### What it is

Every domain has a directed dependency graph of concepts: some concepts cannot be understood without prior mastery of others.

Teaching in the wrong order produces genuine learning failures — the learner has no schema to anchor the new concept, not just a gap in efficiency.

<mark style="background: yellow">Prerequisite mapping makes this dependency graph explicit and uses it to derive instruction order.</mark>

---

### The prerequisite relation

A prerequisite relation A → B means: *understanding B requires prior understanding of A.*

This relation is directed and transitive:

- `Number recognition → Place value → Arithmetic → Word problems`
- `Variables → Loops → Functions → Recursion`
- `HTTP basics → REST semantics → API auth → OAuth flows`

A **concept dependency graph** makes all such relations visible.

Topological sort of this graph gives a valid instruction sequence.

---

### Gagné's learning hierarchy

Gagné's method formalizes prerequisite mapping:

1. Identify the highest-complexity target learning outcome
2. Ask: "What must the learner already know/do to learn this?"
3. Recurse on each prerequisite until reaching known entry skills
4. The resulting tree *is* the instructional sequence — taught bottom to top

This surfaces <mark style="background: pink">hidden prerequisites</mark> that instructors assume but learners lack — the most common cause of unexplained learning failures.

---

### Concept maps (Novak)

Concept maps (Novak, building on Ausubel) visualize prerequisite relations as labeled nodes and directed edges.

Used to:
- Identify hidden prerequisites
- Detect circular or unbounded prerequisite chains (curriculum design errors)
- Communicate to learners *why* topics appear in a given order

---

### Spiral vs. linear prerequisite tension

<mark style="background: cyan">Prerequisite mapping and spiral curriculum are complementary.</mark>

- Prerequisites define the *minimum sequencing constraints* (what must come before what)
- Within those constraints, spiral design decides how often to revisit and at what depth
- Concepts with many dependents and high conceptual richness → spiral treatment
- Pure prerequisite leaves with no further conceptual growth → teach once, master linearly

---

### Application to curriculum design

1. List all concepts in the domain
2. For each concept, identify all direct prerequisites
3. Draw the directed graph; check for cycles (a cycle = curriculum design error)
4. Topological sort gives a valid teaching sequence
5. Mark which concepts benefit from spiral revisiting
6. Open each new branch in the graph with an [[Advance organizers give learners a cognitive hook before new content arrives|advance organizer]]

---

Read more:
- [[Spiral curriculum revisits concepts at increasing depth across multiple encounters]]
- [[Advance organizers give learners a cognitive hook before new content arrives]]
- [[Zone of Proximal Development defines the teachable gap between independent and guided performance]]
- [[Cognitive load theory explains why working memory bottlenecks determine learning speed]]
