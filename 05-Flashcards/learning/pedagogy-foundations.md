TARGET DECK: Tech-KB::Pedagogy::Foundations
Tags: pedagogy foundations
**Related:** [[Learning Strategies MOC]]

---

START
Coding Questions
Why does extraneous load hurt learning more than intrinsic load?
Back:
Working memory capacity is **fixed** — intrinsic + extraneous share the same pool.

- **Intrinsic** = unavoidable complexity of the content itself
- **Extraneous** = wasted capacity from poor presentation (layout, noise, redundancy)

Extraneous load directly steals capacity from actual learning without adding anything.
Tags: pedagogy clt cognitive-load
<!--ID: 1782128730280-->
END

START
Coding Questions
What changed in CLT's 2010 revision regarding germane load?
Back:
Germane load was **removed as a third additive type**.

Before 2010: total load = intrinsic + extraneous + germane
After 2010: total load = intrinsic + extraneous

Germane processing is now understood as working memory being *redirected* from extraneous to intrinsic work — a beneficial side-effect of reducing extraneous load, not a separate bucket to fill.
Tags: pedagogy clt cognitive-load
<!--ID: 1782128730283-->
END

START
Coding Questions
What is the split-attention effect and how do you fix it?
Back:
**Problem:** Diagram and its explanation are physically separated — learner must mentally integrate them, consuming working memory.

**Fix:** Integrate labels and captions directly onto the diagram.

Rule: anything that mutually refers must be spatially co-located.
Tags: pedagogy clt slide-design
<!--ID: 1782128730286-->
END

START
Coding Questions
Why do worked examples help beginners but hurt experts? (expertise reversal effect)
Back:
**Beginners:** No schema → worked example manages intrinsic load → enables learning

**Experts:** Rich schema already exists → worked example is redundant → forces them to reconcile their mental model with the example → wastes capacity

Fix: fade from worked examples to problem-solving as competence grows.
Tags: pedagogy clt
<!--ID: 1782128730288-->
END

START
Coding Questions
What is the Zone of Proximal Development?
Back:
The **distance between what a learner can do alone** and what they can do **with knowledgeable guidance**.

- Below ZPD → wastes time (too easy)
- Above ZPD → no learning (too hard, no schema to scaffold from)
- Inside ZPD → where learning happens

Instruction must operate precisely inside the ZPD, then fade support as competence grows.
Tags: pedagogy zpd vygotsky
<!--ID: 1782128730291-->
END

START
Coding Questions
Why is fading mandatory in scaffolding — what happens if you skip it?
Back:
Scaffolding without fading creates **dependency**, not competence.

The learner performs correctly only when the support is present.
Remove the support → performance collapses.

Fading = gradually removing supports as the learner internalizes the capability.
Tags: pedagogy zpd scaffolding
<!--ID: 1782128730293-->
END

START
Coding Questions
Why does a missing prerequisite prevent the ZPD from forming?
Back:
The ZPD requires a **lower wall** — what the learner can already do independently.

A prerequisite is that lower wall. Without it:
- There is no existing capability to scaffold from
- New content has no schema to attach to
- The ZPD literally has no lower boundary → instruction cannot operate inside it
Tags: pedagogy zpd prerequisites
<!--ID: 1782128730295-->
END

START
Coding Questions
What does Krashen's affective filter claim happens when the filter is high?
Back:
Comprehensible input arrives but is **blocked before reaching the acquisition system**.

The learner may intellectually understand the input but does **not acquire** it — it doesn't stick.

High filter causes:
- Guarded output
- Performance anxiety
- A feedback loop that raises the filter further
Tags: pedagogy affective-filter krashen
<!--ID: 1782128730298-->
END

START
Coding Questions
What raises vs. lowers the affective filter?
Back:
**Raises (blocks acquisition):**
- Anxiety, fear, embarrassment
- Low self-confidence
- Being put on the spot publicly
- Encountering unexplained jargon or missing prerequisites

**Lowers (enables acquisition):**
- Curiosity, positive motivation
- High self-confidence
- Low-stakes private practice
- Clear framing and pre-taught vocabulary
Tags: pedagogy affective-filter krashen
<!--ID: 1782128730301-->
END

START
Coding Questions
What is the main empirical weakness of Krashen's affective filter hypothesis?
Back:
The "filter" metaphor is **unfalsifiable** — there is no way to directly measure a neurological filter.

McLaughlin (1987), Lightbown & Spada (2006), Liu (2015) all note this.

**What survives:** the practical insight — anxiety suppresses learning, calm confidence supports it — is well-supported by test-anxiety literature and self-determination theory.

Use it as a **design heuristic**, not a neurological claim.
Tags: pedagogy affective-filter krashen
<!--ID: 1782128730304-->
END

START
Coding Questions
What is Ausubel's most famous axiom and what does it imply for instruction?
Back:
**"The most important single factor influencing learning is what the learner already knows."**

Implication: before presenting new content, you must either:
1. Activate existing relevant knowledge, OR
2. Build a temporary cognitive structure (advance organizer) for the new content to attach to

Without this, new material arrives with nothing to hook into → stored as isolated rote facts or lost.
Tags: pedagogy advance-organizers ausubel
<!--ID: 1782128730306-->
END

START
Coding Questions
When do you use an expository vs. comparative advance organizer?
Back:
**Expository** — when material is genuinely new to the learner
- Creates a conceptual framework from scratch
- Example: before TCP/IP, give a 2-min overview of "how two computers agree to talk"

**Comparative** — when material resembles something the learner already knows
- Explicitly maps similarities AND differences to prevent false transfer
- Example: before stacks — "like an array, but you can only access one end"
Tags: pedagogy advance-organizers ausubel
<!--ID: 1782128730308-->
END

START
Coding Questions
What are Bruner's three principles of spiral curriculum?
Back:
1. **Cyclical revisiting** — topics return at planned intervals (not randomly; must be designed)
2. **Increasing depth per iteration** — each revisit adds rigor or new connections; not re-teaching, deepening
3. **Explicit connection to prior encounters** — learners are told "you saw X before; now we formalize it"

Without #3, revisitation is just repetition. The connection is what produces deepening.
Tags: pedagogy spiral-curriculum bruner
<!--ID: 1782128730311-->
END

START
Coding Questions
When should a concept be taught linearly (Gagné) vs. spirally (Bruner)?
Back:
**Linear (Gagné):** procedural skills with clear dependencies where full mastery before advancing is required
- Example: arithmetic operations, syntax rules, specific API patterns

**Spiral (Bruner):** conceptual understanding that grows richer through multiple encounters
- Example: recursion, consistency models, design trade-offs

Rule of thumb: **pure prerequisite leaf with no further conceptual growth** → linear.
**Many dependents + high conceptual richness** → spiral.
Tags: pedagogy spiral-curriculum curriculum-design
<!--ID: 1782128730313-->
END

START
Coding Questions
What does a prerequisite relation A → B mean in instructional design?
Back:
**Understanding B requires prior understanding of A.**

The relation is directed and transitive:
- `Variables → Loops → Functions → Recursion`
- `HTTP basics → REST semantics → API auth → OAuth`

Teaching B without A does not produce slow learning — it produces **genuine learning failure** because no schema exists to anchor the new concept.
Tags: pedagogy prerequisite-mapping
<!--ID: 1782128730316-->
END

START
Coding Questions
How do prerequisite mapping and spiral curriculum complement each other?
Back:
They operate at **different levels**:

- **Prerequisite mapping** defines minimum sequencing constraints — what *must* come before what
- **Spiral curriculum** decides *how often to revisit* within those constraints and at what depth

Prerequisites prevent impossible ordering.
Spiral decides the re-encounter schedule within the valid orderings.

They are not competing — they are nested.
Tags: pedagogy prerequisite-mapping spiral-curriculum
<!--ID: 1782128730319-->
END
