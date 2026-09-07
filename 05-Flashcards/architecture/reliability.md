TARGET DECK: Tech-KB::Architecture::Reliability
Tags: architecture reliability fault-tolerance
**Chapter:** Reliability — faults, failures, and tolerating them
**Related:** [[Architecture - MOC]]

START
Coding Questions
A disk in your cluster dies and a replica serves the traffic. Users notice nothing. In DDIA's terms, what happened and what did not?
Back:
A **fault** happened. A **failure** did not.
- **Fault** → one component deviating from its spec (the dead disk)
- **Failure** → the system as a whole stopping delivery of service to the user
Users only ever experience failures. Faults are internal and bounded.
Tags: architecture reliability
<!--ID: 1788436392562-->
END

START
Coding Questions
Why does fault tolerance aim at the transition from fault to failure, rather than at reducing faults?
Back:
Because **the probability of a fault can never be driven to zero** — hardware wears out, kernels have bugs, operators make mistakes.
So the only engineerable thing is the **arrow between them**: keeping a fault from propagating into a failure.
- Postgres primary dies → fault
- Replica promoted in time → no failure
- No promotion → failure
Same fault, two outcomes. Replication, failover, retries and circuit breakers all exist to interrupt that arrow.
Tags: architecture reliability
<!--ID: 1788436392564-->
END

START
Coding Questions
Why is "is this system fault-tolerant?" an unanswerable question, and what should you ask instead?
Back:
Because no system tolerates *every* fault — tolerating the datacenter being swallowed by a black hole would need hosting in space.
Tolerance is always **of specific fault types**, so the term is meaningless without a qualifier.
Ask instead: **"which faults does it tolerate?"** — in an interview, asking this back is the correct move.
Tags: architecture reliability
<!--ID: 1788436392566-->
END

START
Coding Questions
RAID arrays and dual power supplies both work well. What assumption do they share, and where does that assumption break?
Back:
Both assume **failures are independent** — one disk dying tells you nothing about whether the next will.
- True for hardware: correlations exist (a hot rack) but are weak
- Safety comes from multiplying two small probabilities together
**It breaks for systematic software faults**, which are perfectly correlated — so redundancy buys nothing against them.
Tags: architecture reliability redundancy
<!--ID: 1788436392568-->
END

START
Coding Questions
Why do three identical replicas give you no protection against a bug in your own code?
Back:
Because every node runs **the same build carrying the same wrong assumption**.
- The trigger doesn't hit one node — it hits all of them in the same second
- All three crash on the identical bad input
- Failover has nowhere healthy to fail over to
The uncomfortable part: **you built that correlation deliberately.** Running identical code everywhere is the point of a deployment pipeline, and it guarantees a bug arrives everywhere at once.
Tags: architecture reliability redundancy
<!--ID: 1788436392570-->
END

START
Coding Questions
Software faults are rarer than hardware faults, yet they cause many more system failures. Why?
Back:
Because they are **correlated across nodes** while hardware faults are roughly independent.
- Hardware: one disk dies today, another next month — redundancy absorbs it
- Software: one bad input takes down every node simultaneously — redundancy absorbs nothing
Rarity is offset by the fact that each occurrence takes out the whole system rather than one component.
Tags: architecture reliability
<!--ID: 1788436392572-->
END

START
Coding Questions
Why can't you plan against software faults the way you plan against disk failures?
Back:
Because **there is no mean time to failure for a wrong assumption.**
A systematic fault is code making an assumption about its environment that has been true so far:
- It is deterministic and has worked for years
- It fails identically every time once the invalidating circumstance arrives
- You cannot buy a second one, and testing only finds it if the test happens to contain the circumstance you didn't know to think of
Tags: architecture reliability
<!--ID: 1788436392574-->
END

START
Coding Questions
The leap second on June 30, 2012 hung applications worldwide via a Linux kernel bug. What does that illustrate about the nature of software faults?
Back:
That a software fault is a **dormant wrong assumption about the environment**.
- The assumption "a minute has 60 seconds" had never once been wrong
- So it was on nobody's risk register
- The bug lay latent for years until one unusual circumstance revealed what the software believed about the world
Tags: architecture reliability
<!--ID: 1788436392577-->
END

START
Coding Questions
A message queue should emit exactly as many messages as it receives. What reliability technique does that fact enable?
Back:
**Continuous self-checking at runtime** — the system constantly verifies its own guarantee while running and raises an alert on any discrepancy.
This is the strongest defence against systematic faults, because it turns a **silent wrong assumption** into a page.
Any system expected to provide a guarantee can check that guarantee against itself live, rather than waiting for a user to notice.
Tags: architecture reliability
<!--ID: 1788436392579-->
END

START
Coding Questions
Why does deliberately killing processes at random increase a system's reliability?
Back:
Because **error-handling code is the least-executed code in the system**, and many critical bugs live there.
- A `catch` block nobody has ever entered is a guess, not tested recovery logic
- The failover you've never triggered is a hypothesis
Injecting faults continuously keeps the fault-tolerance machinery exercised, so you learn it works **before** the fault arrives on its own schedule. Netflix's **Chaos Monkey** is the well-known implementation.
Tags: architecture reliability chaos-engineering
<!--ID: 1788436392582-->
END

START
Coding Questions
What question does fault injection answer that ordinary testing does not?
Back:
Ordinary testing asks **does the feature work.**
Fault injection asks **does the recovery work** — and that's the question your on-call rotation actually depends on.
It also converts an unknown into a scheduled cost: a replica failing at 2pm while you watch is far cheaper than the same fault at 3am during peak traffic.
Tags: architecture reliability chaos-engineering
<!--ID: 1788436392584-->
END

START
Coding Questions
The default stance is to tolerate faults rather than prevent them. When does that reverse?
Back:
When **no cure exists.**
- Crashed process → restart. Dead disk → rebuild. Bad deploy → roll back. All curable, so spend on recovery.
- **Security breach** → if an attacker has read sensitive data, that cannot be undone. There is no rollback for exfiltration.
For that class the whole budget goes to prevention, because the recovery side of the ledger is empty. Data deletion and irreversible financial actions sit on the same side of the line.
Tags: architecture reliability security
<!--ID: 1788436392586-->
END

START
Coding Questions
What single question tells you whether to invest in prevention or in recovery for a new failure mode?
Back:
**"What does recovery look like here?"**
- Can you describe the recovery → build it, and stop trying to make the fault impossible
- Can you describe no recovery at all → you've found something that must not be allowed to happen, and that changes the **design**, not just the runbook
Tags: architecture reliability
<!--ID: 1788436392588-->
END

START
Coding Questions
In one study of large internet services, what was the leading cause of outages — and how did hardware faults compare?
Back:
**Configuration errors made by operators** were the leading cause.
Hardware faults (servers or network) played a role in only **10–25%** of outages.
The implication: reliability work aimed only at hardware is aimed at the minority of the problem.
Tags: architecture reliability operations
<!--ID: 1788436392590-->
END

START
Coding Questions
Why can making an admin interface *more* restrictive leave the system less safe?
Back:
Because **a restriction removes a safe path but not the need** — so the work relocates to an unsafe path with no guardrails at all, and the dangerous action becomes **invisible** to you.
- Deploy tooling permits one pipeline → engineer hand-edits config over SSH at 3am; prod now differs from the repo and nothing recorded it
- Admin UI refuses bulk operations → ops scripts straight against the database, skipping every validation the UI enforced
You end up worse off than with a permissive interface, because you've lost the audit trail too.
Tags: architecture reliability operations
<!--ID: 1788436392592-->
END

START
Coding Questions
What is the difference between making the right thing easy and making the wrong thing hard, and why does it matter?
Back:
- **Making the wrong thing hard** only blocks a path. The need remains, so people route around it into unguarded territory — risk is *relocated*, not reduced.
- **Making the right thing easy** removes the motive for the workaround, so the safe path stays the convenient one.
Do only the first and you've hidden the risk from yourself. This is why the rest of the human-error toolkit (sandboxes, gradual rollout, fast rollback, telemetry) assumes the mistake happens anyway and works on **containing** it.
Tags: architecture reliability operations
<!--ID: 1788436392595-->
END
