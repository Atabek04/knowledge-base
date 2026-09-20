TARGET DECK: Tech-KB::AI Engineering::Harness Engineering
Tags: ai-engineering harness-engineering
**Chapter:** Harness Engineering
**Related:** [[AI Engineering MOC]]

---

START
Coding Questions
What is a harness, in one line?
Back:
Everything around the model that turns it into an agent: the loop, tools, persisted state, verification checks and stopping rules. **Agent = model + harness.**
Tags: ai-engineering harness-engineering
<!--ID: 1789921329535-->
END

START
Coding Questions
Why was context engineering not enough for long tasks, and what did harness engineering change?
Back:
Long tasks overflowed the window; **compaction** summarised history and lost the details later steps needed, giving incomplete or broken code. Harness engineering replaced one elastic window with a **loop**: each iteration starts a fresh window loaded with the same instructions plus state read from disk.
Tags: ai-engineering harness-engineering
<!--ID: 1789921329543-->
END

START
Coding Questions
Prompt → context → harness engineering: what does each layer control?
Back:
- **Prompt**: the wording of one message
- **Context**: what is in the window on one call
- **Harness**: the system of calls: loop, tools, state on disk, checks, stop rules
Harness does not replace the first two; it assembles them per iteration.
Tags: ai-engineering harness-engineering
<!--ID: 1789921329545-->
END

START
Coding Questions
What are the six components of an agent harness?
Back:
Loop and orchestration · state on disk · tools and skills · verification in the loop (tests, typecheck, hooks) · guardrails and permissions · observability
Tags: ai-engineering harness-engineering
<!--ID: 1789921329546-->
END

START
Coding Questions
How does the Ralph loop work?
Back:
`while` not done: spawn a **fresh** agent instance; it reads `prd.json` (stories with `passes` flags), `progress.txt` (learnings log) and git; implements one story; runs checks; commits; marks it passed; appends learnings; exits. Stops when all stories pass and the agent prints `<promise>COMPLETE</promise>`.
Tags: ai-engineering harness-engineering
<!--ID: 1789921329547-->
END

START
Coding Questions
In Ralph, what is the only memory between iterations, and why is that a feature?
Back:
Disk only: the PRD pass flags, `progress.txt`, and commits. Nothing from a context window survives. So no window ever degrades and no lossy summary accumulates; each story gets a model at full quality for the price of re-reading small files.
Tags: ai-engineering harness-engineering
<!--ID: 1789921329549-->
END

START
Coding Questions
Where does Ralph fail?
Back:
Only as good as its PRD and checks. A vague story or a missing test lets the loop mark broken work as passed and move on. Effort shifts to small verifiable stories and a strict done signal.
Tags: ai-engineering harness-engineering
<!--ID: 1789921329550-->
END
