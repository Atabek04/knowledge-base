
**What is Waterfall?**

Waterfall is a **linear, phase-based approach** where software flows through stages sequentially — Requirements → Design → Implementation → Testing → Deployment → Maintenance.

Each phase must complete before the next begins. Changes to previous phases are costly and discouraged.

---

**Why it emerged (1970s):**

Early software projects were chaotic disasters. No planning, teams built randomly, budgets exploded, timelines missed.

Companies needed **predictability and control**. Manufacturing and construction used sequential phases successfully — why not software?

**Winston Royce (1970)** formalized the model in his paper: "Managing the Development of Large Software Systems." He proposed a rigid, phase-based approach.

**Context then:**
- Hardware was expensive and slow — changes were physically difficult
- Large government/defense contracts demanded documented, auditable processes
- Teams were geographically spread (no instant communication)
- Requirements were relatively stable (business didn't change daily)

Waterfall gave them: **structure, documentation, accountability, and cost control**.

---

**How it works:**

1. **Requirements phase:** Write detailed specifications (100+ pages). Lock them in.
2. **Design phase:** Architects design the entire system upfront.
3. **Implementation phase:** Developers code based on frozen design.
4. **Testing phase:** QA tests everything. Major bugs found here.
5. **Deployment phase:** Release to production.
6. **Maintenance phase:** Fix issues post-launch.

Going back to change requirements = massive rework, delays, cost overruns.

---

**Strengths (why it still exists):**

- Clear milestones and deadlines
- Detailed documentation (good for compliance, audits)
- Budget predictability
- Works for stable, well-understood requirements
- Easy to manage large teams with clear phases

**Weaknesses (discovered in 1990s-2000s):**

- Requirements change mid-project → entire project breaks
- Testing comes too late — bugs in design caught after coding
- Long delivery cycles (2-3 years) → delayed business value
- Customers see working software only at the end
- If requirements were wrong, entire system is wrong
- No room for learning and pivoting

---

**When/where it's used today:**

- **Government contracts** — regulatory requirement for documentation
- **Healthcare systems** — FDA approval requires predictable processes
- **Infrastructure projects** — changes are expensive mid-way
- **Large embedded systems** — hardware constraints make changes costly
- **Projects with locked budgets and timelines** — no flexibility allowed

---

**Example:** Building a banking system. Requirements locked, design for 6 months, coding for 1 year, testing for 3 months, deploy. If requirements missed a critical feature, it's too late.
