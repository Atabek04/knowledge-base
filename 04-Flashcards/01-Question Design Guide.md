---
created: 2025-01-04
tags: [reference, flashcards]
---

# Question Design Guide for Effective Active Recall

## Why This Matters

Your flashcard's **question determines learning outcomes**, not the answer or spacing algorithm.

A poor question wastes spaced repetition intervals. A good question produces **lasting understanding through effortful retrieval**.

This guide extracts actionable rules from learning science research (Roediger, Matuschak, Brown) to help you convert atomic notes into high-quality flashcards.

---

## Core Principle: Effortful Retrieval

**The Testing Effect**: Answering a question strengthens memory **2x more** than passive review.

But only if your question **forces genuine cognitive effort**.

**Three Requirements for Quality Questions:**

1. **Specificity** - One retrievable idea, clearly defined
2. **No Pattern-Matching** - Answer isn't contained in the question
3. **Connection** - Linked to your broader knowledge network

---

## Question Type Effectiveness

### 1. Open-Ended Q&A (Recommended for Conceptual Understanding)

```
How does WebSocket differ from HTTP's request-response model?
```

**Why it works:**
- Forces **free recall** (hardest, strongest memory effect)
- Requires integration, not pattern-matching
- Produces deeper understanding

**When to use:**
- Explaining mechanisms ("How does...")
- Identifying relationships ("Why...")
- Defining with context ("What is the difference...")
- Applying knowledge ("When would you choose...")

**Effectiveness:** ⭐⭐⭐⭐⭐ for understanding

---

### 2. Cloze Deletion (Best for Vocabulary & Drilling)

```
TCP provides ==reliable== delivery by numbering packets and requesting retransmission of lost ones.
```

**Why it works:**
- Quick to create and review
- Context aids memory (works well for vocabulary)
- Rapid drilling builds automaticity

**When to use:**
- Vocabulary/terminology
- Definitions embedded in sentences
- Rapid drilling when understanding already exists
- Technical terms that need quick recall

**Efficiency note:** Cloze works as a *second stage*. First create understanding via Q&A, then use cloze for maintenance drilling.

**Effectiveness:** ⭐⭐⭐⭐ for retention of known concepts

---

### 3. Definition Cards (Recognize When to Avoid)

```
What is TCP?
```

**Why to minimize:**
- Tests recognition, not deep retrieval
- Creates surface-level memorization
- Feels like "trivia" not understanding

**When it's acceptable:**
- New domain where definitions are prerequisites
- Rare terms with no conceptual depth
- Combined with follow-up "Why" or "How" cards

**Effectiveness:** ⭐⭐ for lasting understanding

---

## Practical Extraction Rules

### Extract From Your Atomic Notes

**For a note titled:** *"TCP provides reliable ordered error-checked data delivery over networks"*

```
Your atomic note contains rich material. Don't create one card.
Extract 2-3 focused questions:

1. What mechanisms allow TCP to detect lost packets?
   (Testing mechanism understanding)

2. How does TCP's ordering guarantee differ from UDP?
   (Testing comparative understanding)

3. Why would you choose TCP over UDP for email delivery?
   (Testing application/judgment)
```

**Extraction Process:**

1. **Identify the core concept** in your note title
2. **Ask "What would I need to retrieve to explain this?"**
3. **Break into mechanism, relationship, and application questions**
4. **Never test multiple concepts in one card**

---

## Common Pitfalls: Detection & Fixes

### ❌ Pitfall 1: Ambiguous Questions

**Problem:** Multiple valid answers waste your review time.

```
❌ "What is important about TCP?"
   (Could answer: reliability, ordering, congestion control, connection-oriented...)
```

**Fix:** Specify the retrieval target.

```
✓ "What guarantees does TCP provide that UDP doesn't?"
  (Clear: reliability, ordering, flow control)
```

---

### ❌ Pitfall 2: Hidden Hints (Recognition Instead of Retrieval)

**Problem:** Question context reveals the answer. You recognize instead of retrieve.

```
❌ "Which protocol ensures all data is received in correct order
    with error checking, detecting corrupted packets?"
   (The description IS the answer. You're recognizing, not retrieving.)
```

**Fix:** Remove descriptive context. Make it pure cue.

```
✓ "What is TCP's primary trade-off compared to UDP?"
  (Forces you to retrieve the concept independently)
```

**Hint Detection Checklist:**
- [ ] Does the question describe properties of the answer?
- [ ] Does the question provide example answers?
- [ ] Is the answer pattern-matchable from the question alone?
- [ ] Would an unfamiliar person guess the answer from your question?

If yes to any, **rewrite without hints**.

---

### ❌ Pitfall 3: Over-Complicated Multi-Concept Questions

**Problem:** Testing multiple concepts simultaneously. You can't tell what you actually learned.

```
❌ "Explain TCP's three-way handshake, what each flag means,
    why it's more reliable than UDP, and how it prevents
    data loss."
   (5 different concepts in one card. Working memory overload.)
```

**Fix:** Atomic cards = atomic questions. One concept per card.

```
✓ Card 1: "What are the three flags exchanged in TCP's handshake?"
✓ Card 2: "Why does TCP require a handshake before data transfer?"
✓ Card 3: "What happens if a SYN-ACK is never received during handshake?"
```

---

### ❌ Pitfall 4: Orphan Cards (Disconnected from Knowledge Network)

**Problem:** Questions about isolated facts feel burdensome. They're forgotten easily.

```
❌ Card created alone: "What year was the three-way handshake standardized?"
   (No connection to your TCP understanding. Feels like random trivia.)
```

**Fix:** Connect to your knowledge network.

```
✓ "How does TCP's three-way handshake enable reliable connection setup?"
  (Connects to your understanding of reliability and network protocols)
```

**Connection Test:**
- Can you trace this card to a MOC (Map of Contents)?
- Does it relate to other cards you're reviewing?
- Would this answer help you solve a practical problem?

If no to all three, reconnect or delete.

---

### ❌ Pitfall 5: Poor Question-Answer Mismatch

**Problem:** Question and answer don't align in depth or scope.

```
❌ Question: "Explain how WebSocket establishes connections."
   Answer: "Via HTTP upgrade handshake."
   (Question expects explanation; answer is a fragment.)
```

**Fix:** Align cognitive demand.

```
✓ Question: "What HTTP feature does WebSocket use to establish a connection?"
  Answer: "HTTP upgrade request with Connection: Upgrade and Upgrade: WebSocket headers"
  (Both expect specific, detailed retrieval.)
```

---

## Granularity Levels

Choose deliberately based on your learning goal:

| Level | Specificity | Example | Use When |
|---|---|---|---|
| **Definition** | Broad | "What is TCP?" | New domain, prerequisite terminology |
| **Mechanism** | Medium | "How does TCP detect packet loss?" | Understanding *how* something works |
| **Relationship** | Medium | "Why does TCP use sequence numbers?" | Understanding *why* design choices exist |
| **Application** | Specific | "When would you choose TCP over UDP?" | Judgment, transfer of learning |

**Avoid mixing levels in one card.** Each level requires different retrieval pathways.

---

## Quality Checklist Before Adding a Card

Before converting an atomic note into a flashcard, verify:

- [ ] **Single Concept:** Does this card test exactly one retrievable idea?
  - If testing multiple concepts, split into multiple cards

- [ ] **No Hints:** Does my question contain contextual clues that reveal the answer?
  - Remove all descriptions; make it a pure retrieval cue

- [ ] **Connected:** How does this relate to my broader knowledge?
  - Avoid orphans; link to MOCs or related concepts
  - Not every detail needs connection, but important concepts should

- [ ] **Unambiguous:** Is the answer clear and specific?
  - Could two reasonable people answer this differently?
  - Refine until one answer is correct

- [ ] **Requires Effort:** Does answering require meaningful cognitive work?
  - Too easy: wastes spaced repetition intervals
  - Too hard: causes frustration; rewrite for clarity

- [ ] **Right Granularity:** Am I asking at the appropriate specificity level?
  - Definition = low integration
  - "How" = mechanism
  - "Why" = reasoning
  - "When" = application

- [ ] **Properly Phrased:** Is my question phrased as a question?
  - Not: "Discuss TCP's reliability mechanisms"
  - Yes: "What mechanisms does TCP use to ensure reliability?"

---

## Question Templates for Atomic Notes

When extracting questions from atomic notes, use these templates:

### Definition/Terminology
```
What is [concept]?
Define [term] in the context of [domain].
```

### Mechanism (How)
```
How does [mechanism] work?
What steps are involved in [process]?
What is the sequence of [mechanism]?
```

### Causality (Why)
```
Why does [system] use [mechanism]?
What problem does [mechanism] solve?
What would happen without [mechanism]?
```

### Relationship (Comparison)
```
How does [concept A] differ from [concept B]?
What is the trade-off between [A] and [B]?
When would you choose [A] over [B]?
```

### Application
```
When would you use [concept] in practice?
How would you apply [principle] to [scenario]?
What are real-world implications of [mechanism]?
```

---

## Your Workflow: Fleeting → Atomic → Flashcards

### Step 1: Fleeting Notes
Capture raw insights without structure.

### Step 2: Atomic Notes
Refine into single, complete-statement titles.

**Title Example:** *"TCP maintains sequence numbers to detect missing packets"*

### Step 3: Extract Questions

**Ask yourself:** "What would I need to *retrieve* to explain this note to someone?"

For the TCP note above:
- "How do sequence numbers help TCP detect missing packets?"
- "Why is packet ordering important for reliable delivery?"
- "What information does a sequence number contain?"

### Step 4: Create Cards
Convert questions using your SR plugin syntax.

**Using Q&A format (recommended for understanding):**
```
How do sequence numbers help TCP detect missing packets?
?
By comparing the sequence number of received packets to the expected next sequence,
TCP can identify gaps and request retransmission of missing packets.
```

**Using Cloze format (for vocabulary reinforcement):**
```
TCP detects missing packets by comparing the ==sequence number== of received packets
to the expected next sequence, identifying gaps that require retransmission.
```

---

## Red Flags: Signs Your Questions Need Redesign

During review, pay attention to these feelings:

| Red Flag | What It Means | How to Fix |
|----------|---|---|
| "I can never remember this" | Question is too hard OR poorly defined | Simplify question or rewrite for clarity |
| "I knew the answer but don't understand what it means" | Surface-level pattern-matching | Remove hints; make question require deeper retrieval |
| "This feels like trivia" | Card is orphaned, disconnected from broader knowledge | Link to MOC; create related cards showing relationships |
| "I got it right but guessed" | Question is ambiguous | Tighten phrasing until only one answer fits |
| "This is too easy" | Question isn't challenging retrieval | Combine with related concept; ask at deeper level |

---

## Research Foundation

This guide synthesizes research from:

- **Roediger & Karpicke:** Spacing and testing effects double retention vs. passive review
- **Make It Stick:** Effortful retrieval creates durable, transferable learning
- **Andy Matuschak:** Prompts must avoid shallow pattern-matching and orphan knowledge
- **Leitner System & SM2:** Spacing algorithms assume well-designed questions
- **Learning Science:** Active recall is 2x more effective than passive review

The spacing algorithm is only as good as your question quality.

---

## Quick Reference

| Aspect | Best Practice |
|--------|---|
| **One concept per card** | Atomic cards → atomic questions |
| **Question type** | Q&A for understanding; Cloze for drilling |
| **Eliminate hints** | Remove contextual clues that enable pattern-matching |
| **Ensure connection** | Link to MOC; avoid orphan cards |
| **Calibrate difficulty** | Effortful but learnable |
| **Phrasing** | Use "How," "Why," "When," "What if" for depth |
| **Testing** | If you can't articulate the answer clearly, redesign |

---

## Next Steps

1. Review your existing flashcards with this checklist
2. Extract questions from new atomic notes using the templates
3. Listen to your review experience—red flags signal redesign opportunities
4. Connect related cards through MOC structure

Quality questions compound. Each well-designed card produces understanding that lasts and transfers to new domains.
