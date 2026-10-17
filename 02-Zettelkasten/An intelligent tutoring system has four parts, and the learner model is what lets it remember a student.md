---
created: 2026-10-13
tags: [education, ai-in-education, its]
aliases: [ITS architecture, four-component ITS, intelligent tutoring system]
---

An intelligent tutoring system tutors one learner at a time and adapts to that learner. The classic textbook design, used in most surveys of the field, splits it into four parts. Each part answers a different question.

### Glossary

- **Intelligent tutoring system (ITS)**: <mark style="background: #FFF3A3A6;">software that tutors a single learner and adapts its next move to what that learner knows</mark>.
- **Domain model**: <mark style="background: #FFF3A3A6;">the part that holds what is true in the subject: rules, facts, correct solutions and common errors</mark>.
- **Learner model**: <mark style="background: #FFF3A3A6;">the part that holds the system's current estimate of what this particular student knows</mark>.
- **Tutoring model**: <mark style="background: #FFF3A3A6;">the part that decides the next teaching move: which task, which hint, when to move on</mark>.
- **Interface**: the screen, text or voice the learner actually interacts with.

---

### The four parts and the question each answers

| Part | Question it answers | Example in an Arabic grammar tutor |
|---|---|---|
| Domain model | What is correct? | A noun after a preposition takes the genitive case |
| Learner model | What does this student know? | This student misses the genitive after prepositions 3 times in 5 |
| Tutoring model | What should happen next? | Give a hint, then two more preposition items before moving on |
| Interface | How does the student see it? | A sentence with the case ending to fill in |

The domain model is about the *domain*, the subject. The learner model is a *model* of the *learner*. The names say what each part stores.

---

### Why the learner model is what lets it remember

A system with only a domain model and an interface can still mark an answer right or wrong in the moment. The domain model knows the rule, so it can judge the answer.

<mark style="background: #ABF7F7A6;">Without a learner model, the system forgets the weakness as soon as the session ends, so tomorrow it cannot pick practice for that gap.</mark> The judgment is stored nowhere, and the tutoring model has nothing to adapt to.

#### A chat box is an interface without the other three

<mark style="background: #FF5582A6;">A plain chatbot tutor is mostly an interface over a language model: it has no explicit learner model, so it cannot report what a student has mastered.</mark> The language model holds a rough, unchecked domain model, and the conversation history stands in for a learner model only until the context is cleared.

---

### Source

- Woolf, B. P. (2009). *Building Intelligent Interactive Tutors*. Morgan Kaufmann. Architecture chapters.

### Read more

- [[AI in Education MOC]]
- [[One-to-one tutoring beats classroom teaching but Bloom's two sigma gain shrinks to under one sigma in later evidence]]
- [[Concept prerequisite mapping sequences instruction along the dependency graph]]
