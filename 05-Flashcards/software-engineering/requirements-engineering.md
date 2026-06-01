TARGET DECK: Tech-KB::Software Engineering::Requirements Engineering
Tags: software-engineering requirements
**Chapter:** Requirements Engineering Phases & Artifacts
**Related:** [[Requirements Engineering MOC]]

---

START
Coding Questions
What is progressive elaboration in requirements engineering?
Back: **Progressively elaborating** requirements from broad business goals to granular implementation details.
- **BRD** → WHY (business goals)
- **SRS** → HOW (system capabilities)
- **FRS** → WHAT exactly (field-level behavior)
Each level adds precision while staying traceable to the level above.
Tags: software-engineering requirements
<!--ID: 1780311502244-->
END

START
Coding Questions
What is the traceability backbone in requirements engineering?
Back: A chain linking every level of requirements:
**Business goals → BRD scope → PRD features → FRD behaviors → system requirements → test cases**
- Every low-level requirement traces **back** to a business goal
- Every requirement traces **forward** to a test case that validates it
Tags: software-engineering requirements
<!--ID: 1780311502265-->
END

START
Coding Questions
What does a BRD (Business Requirements Document) contain?
Back: The **business case** — no technical detail:
- **Business objectives** — what the organization wants to achieve
- **Project scope** — boundaries of what's in and out
- **Stakeholders** — who is involved and their roles
- **Constraints** — budget, timeline, regulatory limits
- **Success criteria** — measurable outcomes
The BRD answers **"WHY are we building this?"**
Tags: software-engineering requirements
<!--ID: 1780311502285-->
END

START
Coding Questions
Why is the BRD always the first formal document in requirements engineering?
Back: Because you must establish **business justification** before any technical work begins.
- No UML, no database schemas, no API specs at this stage
- The BRD gets **signed off by the client** — it's the contractual agreement on project scope
- Without a BRD, technical work has no grounding in business value
Tags: software-engineering requirements
<!--ID: 1780311502306-->
END

START
Coding Questions
Why does BPMN come before UML in requirements engineering?
Back: Because you must understand the **business process** before designing the **system** that supports it.
- **BPMN** is business-facing and process-oriented — shows how work flows
- **UML** is system-facing and object-oriented — shows how software components interact
- Jumping to UML before BPMN means designing a system for a process you don't fully understand
Tags: software-engineering requirements
<!--ID: 1780311502327-->
END

START
Coding Questions
How do BPMN and UML differ in their role during requirements engineering?
Back:
- **BPMN** = **elicitation and analysis tool** — helps discover and validate requirements with stakeholders. Intuitive, no technical knowledge needed.
- **UML** (detailed) = **specification tool** — formalizes requirements that are already understood and documented.
- Exception: UML **Use Case Diagrams** appear early alongside TO-BE BPMN (high-level enough to be an elicitation tool).
Tags: software-engineering requirements
<!--ID: 1780311502348-->
END

START
Coding Questions
What is the purpose of AS-IS process modeling?
Back: **Mapping current-state workflows** with BPMN to identify bottlenecks and inefficiencies before designing any solution.
- Without it, you risk automating a broken process
- You might miss edge cases users handle manually
- Happens in **Phase 2** — right after BRD signoff
Tags: software-engineering requirements
<!--ID: 1780311502369-->
END

START
Coding Questions
What two deliverables does TO-BE process modeling produce?
Back:
1. **TO-BE BPMN diagrams** — the redesigned future-state process (bottlenecks removed)
2. **UML Use Case Diagram** — the first UML artifact, showing actors, system boundaries, and major interactions
- Together they answer: "How should work flow?" (BPMN) and "What does the system do within that flow?" (Use Cases)
Tags: software-engineering requirements
<!--ID: 1780311502390-->
END

START
Coding Questions
What are the three components of a UML Use Case Diagram?
Back:
- **Actors** — external entities (users or organizations) that interact with the system
- **Use cases** — functions users can access within the system
- **System boundary** — what's inside vs outside the system scope
Tags: software-engineering requirements
<!--ID: 1780311502410-->
END

START
Coding Questions
What is the user story format and what does each part clarify?
Back: **As a [role], I want [action], so that [benefit]** + acceptance criteria.
- **Role** → WHO needs this (stakeholder identification)
- **Action** → WHAT they need (the feature)
- **Benefit** → WHY they need it (business motivation)
- **Acceptance criteria** → DONE WHEN conditions (testable outcomes)
Tags: software-engineering requirements
<!--ID: 1780311502431-->
END

START
Coding Questions
How do user stories differ from SRS requirements?
Back:
- **User stories** — high-level, user-facing, behavior-oriented ("As a user, I want...")
- **SRS requirements** — more detailed and lower-level, technically oriented ("System shall validate...")
- User stories are **not a replacement** for the BRD or SRS — they live at a different abstraction level
- Depending on the project, you may need both together
Tags: software-engineering requirements
<!--ID: 1780311502457-->
END

START
Coding Questions
What does the SRS (Software Requirements Specification) contain?
Back: The **bridge** between business and development:
- **Functional requirements** — what the system must do
- **Non-functional requirements** — performance, security, scalability
- **Use case descriptions** — detailed narratives
- **System constraints** — technical limitations
- **High-level architecture** — overall system structure
The SRS answers **"HOW"** — it describes the structure and stages of implementation.
Tags: software-engineering requirements
<!--ID: 1780311502480-->
END

START
Coding Questions
How does the SRS relate to the BRD and FRS?
Back:
| Document | Question | Level | Audience |
|----------|----------|-------|----------|
| **BRD** | WHY? | Business goals | Client, sponsors |
| **SRS** | HOW? | System capabilities | Dev team, architects |
| **FRS** | WHAT exactly? | Field-level behavior | Developers |
The SRS sits in the middle — technical enough for developers, readable enough for stakeholders.
Tags: software-engineering requirements
<!--ID: 1780311502501-->
END

START
Coding Questions
Why should detailed UML diagrams only be created after the SRS is complete?
Back: Because UML **specification diagrams** formalize requirements that must already be understood.
- Sequence diagrams need **finalized use cases** — otherwise rework is inevitable
- Each UML model elaborates a specific written requirement from the SRS
- You don't model in a vacuum — every model must be grounded in a requirement
Tags: software-engineering requirements
<!--ID: 1780311502522-->
END

START
Coding Questions
What four types of detailed UML diagrams are produced in the specification phase?
Back:
- **Activity Diagrams** — detailed workflow logic per use case
- **Sequence Diagrams** — object-to-object interactions, API calls, method names
- **Class Diagrams / ERDs** — data model, entity relationships
- **State Machine Diagrams** — lifecycle of key objects (e.g., Order: created → paid → shipped)
Tags: software-engineering requirements
<!--ID: 1780311502542-->
END

START
Coding Questions
What does the FRS (Functional Requirements Specification) contain?
Back: The most **granular** document — developer's working specification:
- **Field-level specs** — every input field, type, length, default
- **Exact validation rules** — "email: required, max 255 chars, regex..."
- **Button behaviors** — what each UI action triggers
- **Error messages** — exact wording for every error state
- **References to UML** — links directly to sequence/activity diagrams
Tags: software-engineering requirements
<!--ID: 1780311502563-->
END

START
Coding Questions
What is a Requirements Traceability Matrix (RTM) and what does it prevent?
Back: An **RTM** links every requirement backward to its business goal and forward to its test cases.
Prevents two problems:
- **Gold plating** — features built that trace to no business goal (wasted effort)
- **Coverage gaps** — requirements with no test case (untested behavior)
Tags: software-engineering requirements
<!--ID: 1780311502584-->
END

START
Coding Questions
What is the complete artifact spine in requirements engineering?
Back: **BRD → BPMN (AS-IS) → BPMN (TO-BE) + Use Cases → User Stories → SRS → Detailed UML → FRS → Prototypes → Signoff**
- Documents and models are **interleaved**, not sequential
- Each phase produces an artifact that feeds the next
- BABOK treats knowledge areas as concurrent — analysis happens during elicitation
Tags: software-engineering requirements
<!--ID: 1780311502604-->
END

START
Coding Questions
Why are requirements documents and models interleaved rather than sequential?
Back: Because documents and models **co-evolve** — each validates the other:
- Models (BPMN, UML) help **discover** what to write in documents
- Documents (BRD, SRS) provide the **grounding** for what to model
- The BABOK treats requirements activities as concurrent, not waterfall
- Practitioner consensus: keep docs lean, use models for clarity, iterate frequently
Tags: software-engineering requirements
<!--ID: 1780311502625-->
END
