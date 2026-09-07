# Phase templates and calibration

Output skeletons plus good/bad pairs. The skeletons keep runs consistent; the pairs are the
calibration that actually matters — most failures are a question that's too soft or a card front
that tests recognition.

## Contents

- [Phase 1 skeleton](#phase-1-skeleton)
- [Phase 2 — question calibration](#phase-2--question-calibration)
- [Phase 2 — handling a vague answer](#phase-2--handling-a-vague-answer)
- [Phase 3 skeleton](#phase-3-skeleton)
- [Phase 4 — card calibration](#phase-4--card-calibration)
- [Phase 5 — note title calibration](#phase-5--note-title-calibration)

---

## Phase 1 skeleton

```markdown
## Ch5 — Replication · your questions

### Why is semi-synchronous replication the practical middle ground?

[Answer in your own words, 3–6 short paragraphs max, one idea per line.] (p. 154)

### Does a version vector tell you which write happened first?

**Correcting your recall:** you wrote that version vectors order writes. They don't — they detect
concurrency, which is the absence of an ordering. (p. 190)

[Answer.]

### How does Raft pick a leader?

`OUT OF SCOPE` — consensus is Ch9, not Ch5. Answering anyway: [answer] (p. 366)
```

Then stop:

> That's the question list. Interview next — book shut, notes repo unopened. Ready?

---

## Phase 2 — question calibration

The escalation is concrete → trade-off → transfer. Each rung tests something the previous can't.

**Concrete (opener, 1–2 questions).** Establishes they have the mechanism at all.

- ✓ "What problem does leader-based replication solve that a single node doesn't have?"
- ✗ "What is leader-based replication?" — invites a recited definition, tests nothing.

**Trade-off (the bulk, 5–7 questions).** Where real understanding lives.

- ✓ "You make the follower synchronous. What did you just buy, and what did you just pay?"
- ✓ "When would you NOT use multi-leader replication, given you've just told me it survives a
  datacenter outage?"
- ✗ "What are the advantages and disadvantages of multi-leader replication?" — a list prompt.
  They'll recite; you'll learn nothing about whether they can apply it.

**Transfer (close, 2–3 questions).** Does it survive contact with a system?

- ✓ "Your read replicas are 30 seconds behind and users say their own profile edits vanish. Which
  anomaly is that, and what's the cheapest fix that doesn't require synchronous replication?"
- ✓ "Traffic goes 10×. Which part of this design breaks first?"
- ✗ "Can you give a real-world example of replication lag?" — they'll name Twitter and stop.

---

## Phase 2 — handling a vague answer

The failure mode is completing their sentence for them. Narrow instead.

> **Them:** "Quorums make sure you read fresh data."
>
> ✗ **Don't:** "Right — because with w + r > n the read and write sets overlap, so…"
> ✓ **Do:** "Make that precise. n is 5. What are the smallest w and r that give you that?"
>
> **Them:** "Like, 3 and 3?"
>
> ✓ **Do:** "That works. Now tell me why 3 and 2 doesn't."

Three narrowing follow-ups is usually the ceiling. If they still can't produce it, say
*"okay — that's a missing, we'll card it"* and move on. Don't teach it here; that's Phase 4's job
or a `/teach` handoff if they ask.

When they're wrong, be plain and immediate: *"No — that's backwards."* Then one constraint that
forces the correction: *"If it worked the way you just said, what would happen when both leaders
accept a write to the same key?"*

---

## Phase 3 skeleton

```markdown
## Grade — Ch5

| Concept | Your answer | Verdict |
|---|---|---|
| Sync vs async followers | Clean on the durability/latency trade-off | solid |
| Failover hazards | Named split brain, missed lost writes on async promotion | shaky |
| Read-your-writes | Couldn't distinguish it from monotonic reads | shaky |
| Version vectors | Thought they ordered writes | missing |

### The one that costs most

**Treating version vectors as an ordering.** [Two or three sentences: the concrete failure — the
design you'd propose in an interview, or the data you'd silently lose in production — and why the
confusion is easy to hold.]
```

Cross-check the ps06756 repo at this point, and add a line if it surfaces a chapter concept neither
of you raised:

> Not covered either way, and worth knowing: chained replication topologies in multi-leader setups.

---

## Phase 4 — card calibration

Fronts that make them *derive* beat fronts that make them *recognize*.

| ✗ Recognition front | ✓ Retrieval front |
|---|---|
| What is a version vector? | You have two concurrent writes to one key. What does a version vector let you conclude, and what does it deliberately refuse to tell you? |
| What is read-your-writes consistency? | A user edits their profile and the edit vanishes on refresh. Which replication-lag anomaly is this, and what's the fix that doesn't need synchronous replication? |
| Define split brain. | Async failover promotes a follower while the old leader is still up. Name the two distinct data-loss modes this creates. |
| What does `w + r > n` guarantee? | n=5, w=3, r=3. A sloppy quorum accepts your write on two nodes outside the designated five. Is the guarantee still intact? Why not? |

Only draft from `shaky` and `missing`. If the grade has three shaky rows, you get roughly three to
six cards — not twelve. The cap is a ceiling, not a target.

---

## Phase 5 — the split test

Worked example of the failure, from Ch1. This draft looked reasonable and was wrong:

```
Fault tolerance targets the transition from fault to failure...
  ### A fault is local, a failure is what the user sees
  ### The design target is the arrow, not the endpoints
  ### Redundancy only defeats faults that fail independently
  ### Increasing the fault rate on purpose
  ### When prevention beats tolerance
```

Five headings, five claims that each carry their own complete-statement title — so five notes, not
one. The tell is that the headings read as a *tour of reliability* rather than as the defence of a
single claim. The same draft also silently swallowed the systematic-fault-dormancy concept inside
the redundancy heading, which is how concepts disappear from a vault.

The correct decomposition:

| Note | The one claim it defends |
|---|---|
| A fault is a component deviating from spec while a failure is the system no longer serving users | the distinction, and that you engineer the arrow between them |
| Redundancy only defeats faults that fail independently so it cannot save you from a shared bug | redundancy's hidden independence assumption |
| A systematic software fault is a dormant wrong assumption about the environment | why software faults have no failure rate |
| Deliberately triggering faults is the only way to exercise error-handling code that otherwise never runs | why chaos engineering works |
| Preventing a fault beats tolerating it only when no cure exists | the one exception to tolerate-don't-prevent |

Ch1's real yield was 14 atomic notes against a stated budget of 1–2. The budget was wrong and got
updated. **A budget is an estimate; atomicity is a law.**

Contrast with legitimate `####` sub-points, which do *not* mean a note should split: a caveat,
an edge case, or a named example that only makes sense as support for the note's single claim.
"Fault-tolerant is a misleading label" belongs inside the fault-vs-failure note — it's a qualifier
on that claim, not a separate one.

---

## Phase 5 — note title calibration

Per the MOC: **every title names a tension.**

| ✗ Names a thing | ✓ Names a tension |
|---|---|
| Version vectors | Version vectors detect concurrent writes but deliberately refuse to order them |
| Synchronous replication | Synchronous replication trades write availability for guaranteed follower durability |
| Sloppy quorums | A sloppy quorum keeps writes available by breaking the w + r > n overlap guarantee |
| Replication lag | Read-your-writes consistency is needed because a user's own write is the one they notice missing |

Before writing, search the vault for each concept. DDIA overlaps existing notes heavily — MVCC,
isolation levels, locking, Kafka delivery semantics all likely have owners already. Link into them;
don't create a second owner. If the search shows a prerequisite is missing entirely, write the
prerequisite first, per `CLAUDE.md`.

Budget check before you start writing, out loud:

> MOC says 8–10 notes for Ch5. Solid + recovered-shaky rows give me 7 candidates, two of which
> the vault already owns — so 5 new notes, routed to Distributed Systems and PostgreSQL.
