
SDLC (Software Development Life Cycle) is a structured process for building software. Each phase has specific goals, deliverables, and owners.

**Example case:** Building an e-commerce platform for a retail company.

---

## Phase 1: Planning & Requirements

**Goal:** Understand what to build and why.

**Involved:** Stakeholders (business), Product Manager, System Analyst, Business Analyst, Project Manager.

**Responsible:** **Product Manager** — defines vision, scope, business case.

**Output:** Requirements document, project charter, stakeholder list.

**Example:** Product Manager decides: "We need an e-commerce platform to reach online customers. Budget: $500k. Timeline: 6 months."

---

## Phase 2: Analysis

**Goal:** Deep dive into business processes and technical constraints.

**Involved:** Business Analyst, System Analyst, IT Operations, stakeholders.

**Responsible:** **Business Analyst** — documents current processes and gaps.

**Output:** Detailed requirements, process flows, use cases.

**Example:** BA interviews store managers, discovers: "Inventory updates are manual. Customers abandon carts if checkout takes >5 steps."

---

## Phase 3: Design

**Goal:** Plan the technical architecture and user experience.

**Involved:** System Analyst, Architects, UX Designers, DBAs, developers (review).

**Responsible:** **System Analyst/Architect** — designs system structure, database, APIs, security.

**Output:** System design document, database schema, UI mockups, API specifications.

**Example:** Design: PostgreSQL database, microservices architecture, React frontend, payment gateway integration, CDN for images.

---

## Phase 4: Development

**Goal:** Write and build the software.

**Involved:** Developers, Team Leads, QA (review code), System Analyst (clarifications).

**Responsible:** **Team Lead/Senior Developer** — owns code quality and architecture adherence.

**Output:** Working code, code documentation, unit tests.

**Example:** Frontend team builds login → Product catalog → Shopping cart. Backend team builds inventory API → Order API → Payment API.

---

## Phase 5: Testing

**Goal:** Verify the system works as designed and finds defects.

**Involved:** QA Engineers, Developers (fix bugs), Business Analyst (UAT).

**Responsible:** **QA Lead** — owns test strategy and defect management.

**Output:** Test cases, defect reports, test coverage metrics.

**Example:** QA tests: Can users add items to cart? Does checkout work? What if payment fails? Security tests for SQL injection.

---

## Phase 6: Deployment

**Goal:** Move the software to production safely.

**Involved:** DevOps Engineers, System Analyst, Project Manager, Business users (go-live).

**Responsible:** **DevOps/Release Manager** — owns deployment process and rollback plan.

**Output:** Deployment plan, user documentation, training materials.

**Example:** Deploy to production Friday night (low traffic). Have rollback ready. Train store staff on new inventory system.

---

## Phase 7: Maintenance & Support

**Goal:** Keep the system running, fix issues, add improvements.

**Involved:** Support team, Developers, System Analyst, users.

**Responsible:** **Support Lead** — owns incident response and issue tracking.

**Output:** Bugfixes, performance reports, enhancement requests for next cycle.

**Example:** "Checkout is slow during peak hours. Payment gateway sometimes times out. Add dark mode feature request from users."

---

## Key Insight

Each phase has a **primary owner** (who's accountable) and **supporting roles** (who contribute). Clarity on who decides what prevents chaos.

**Handoff:** Phase output becomes next phase's input. Requirements → Design → Code → Tests → Deploy.
