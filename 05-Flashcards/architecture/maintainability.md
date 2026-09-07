TARGET DECK: Tech-KB::Architecture::Maintainability
Tags: architecture maintainability operability simplicity evolvability
**Chapter:** Maintainability — operability, simplicity, evolvability
**Related:** [[Architecture - MOC]]

START
Coding Questions
Where does the majority of software cost fall, and what does that imply about who you are designing for?
Back:
**Not in initial development — in ongoing maintenance:** fixing bugs, keeping systems operational, investigating failures, adapting to new platforms, modifying for new use cases, repaying technical debt, adding features.
The code is written once and paid for continuously, so optimizing the writing at the expense of the reading optimizes the small number.
The implication: **the future maintainer — possibly you in eighteen months — is the real user of the design.**
Tags: architecture maintainability
<!--ID: 1788436392529-->
END

START
Coding Questions
What are the three design principles DDIA names for maintainability?
Back:
- **Operability** → make it easy for operations teams to keep the system running smoothly
- **Simplicity** → make it easy for new engineers to understand the system, by removing complexity (note: *not* simplicity of the user interface)
- **Evolvability** → make it easy to change the system later for unanticipated use cases
None of the three has an easy solution. They are lenses you hold while designing, not features you add.
Tags: architecture maintainability
<!--ID: 1788436392533-->
END

START
Coding Questions
Between good software and good operations, which one can rescue the other? Why does the asymmetry matter?
Back:
**Good operations can often work around the limitations of bad or incomplete software. Good software cannot run reliably with bad operations.**
Operations is the load-bearing side — which is why operability is a *design* concern, not something you delegate after launch.
Automation doesn't escape this: humans still have to build the automation and verify it works, so "we'll automate it" relocates the human judgment rather than removing it.
Tags: architecture maintainability operability
<!--ID: 1788436392535-->
END

START
Coding Questions
Good monitoring, standard-tool integration, sane defaults with overrides, self-healing with manual control, no dependency on individual machines — what single property are all of these buying?
Back:
**Predictability** — minimizing surprises.
An operator's real job at 3am is reasoning about what the system will do next. A system that surprises them cannot be operated, no matter how good its uptime looks on an ordinary day.
The related goal is an understandable **operational model**: *"if I do X, Y will happen."*
Tags: architecture maintainability operability
<!--ID: 1788436392538-->
END

START
Coding Questions
How does building a system to tolerate the loss of any single machine buy you operability for free?
Back:
Because it removes **planned** downtime, not just unplanned.
- A single-server system must be taken offline to reboot for an operating system security patch
- A system that tolerates machine failure can be patched **one node at a time**, with no downtime for the system as a whole (a *rolling upgrade*)
So a reliability property pays out a second time as an operations property.
Tags: architecture maintainability operability
<!--ID: 1788436392540-->
END

START
Coding Questions
Does making a system simpler mean giving up functionality? Explain using the accidental/inherent distinction.
Back:
**No.** Simplifying means removing **accidental** complexity, which the problem never asked for.
- **Inherent complexity** → part of the problem the software solves, *as seen by the users*. You must carry it.
- **Accidental complexity** → arises only from the implementation. It got there by accident of how you built it — nobody chose it, and it's yours to delete.
The name is the mnemonic: *accidental* complexity was not intended by anyone.
Tags: architecture maintainability simplicity
<!--ID: 1788436392543-->
END

START
Coding Questions
What test tells you whether a piece of complexity is accidental or inherent?
Back:
**Would a user recognize this difficulty as part of their problem?**
- Yes → inherent. It belongs to the problem; carry it.
- No → accidental. It exists only because of your implementation; remove it.
The phrase that carries the test is *"as seen by the users"* — the users of the software, not the engineers.
Tags: architecture maintainability simplicity
<!--ID: 1788436392545-->
END

START
Coding Questions
Beyond slowing everyone down, what is the second and more dangerous cost of complexity?
Back:
**A greater risk of introducing bugs when making a change.**
When a system is hard to reason about, hidden assumptions, unintended consequences and unexpected interactions get overlooked.
So complexity compounds: it slows the work **and** raises the defect rate of the work, and those defects generate more work. (A project mired in this is a **big ball of mud** — tangled dependencies, tight coupling, inconsistent naming, special-casing to work around problems elsewhere.)
Tags: architecture maintainability simplicity
<!--ID: 1788436392549-->
END

START
Coding Questions
Why is reuse of a good abstraction worth more than the typing it saves?
Back:
Because **quality improvements inside the abstracted component benefit every application that uses it.**
Effort spent there compounds rather than being spent once — one fix improves every consumer simultaneously, which also raises overall software quality rather than just reducing duplication.
Tags: architecture maintainability abstraction
<!--ID: 1788436392551-->
END

START
Coding Questions
What three hard problems does SQL (Structured Query Language) abstract away, and what does that illustrate?
Back:
- on-disk and in-memory data structures
- concurrent requests from other clients
- inconsistencies after crashes
It illustrates the scale of hiding a good abstraction achieves: three genuinely hard problems behind one declarative sentence.
The parallel example: **high-level programming languages** abstract machine code, CPU registers and syscalls. You're still using machine code — you're just not thinking about it.
Tags: architecture maintainability abstraction
<!--ID: 1788436392553-->
END

START
Coding Questions
Why is a bad abstraction worse than no abstraction at all?
Back:
Because **it adds a layer to learn without removing the layer beneath**, so you now reason about both.
A leaky abstraction still charges the full price of the thing it was supposed to hide, plus its own.
This is why DDIA is explicit that **finding good abstractions is very hard** — in distributed systems there are many good algorithms but far less clarity on how to package them into abstractions that keep complexity manageable.
Tags: architecture maintainability abstraction
<!--ID: 1788436392555-->
END

START
Coding Questions
Agile already has TDD and refactoring for handling change. Why does DDIA introduce a separate word, "evolvability"?
Back:
Because of **scale**. Those techniques are discussed at a small, local level — a few source files inside one application.
**Evolvability is the same idea raised to the level of a data system**: several applications or services with different characteristics.
The worked question: how would you *refactor* Twitter's home-timeline architecture from fan-out on read to fan-out on write? That's unmistakably a refactor, and nothing in the test-driven-development (TDD) toolkit addresses it.
Tags: architecture maintainability evolvability
<!--ID: 1788436392557-->
END

START
Coding Questions
Why can't you pursue evolvability directly, and why does "let's make it flexible for the future" often backfire?
Back:
Because evolvability is **closely linked to simplicity and to the quality of your abstractions** — simple, easy-to-understand systems are easier to modify. There is no evolvability feature to add; it's what you find you have after removing accidental complexity and finding clean seams.
The backfire: **speculative extension points are added complexity**, and complexity is precisely what makes a system hard to change. Building for imagined futures buys the opposite of what it promises.
Tags: architecture maintainability evolvability
<!--ID: 1788436392560-->
END
