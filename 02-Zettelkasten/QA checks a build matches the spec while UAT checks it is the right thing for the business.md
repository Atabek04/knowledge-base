---
created: 2026-10-14
aliases: [UAT, user acceptance testing, QA vs UAT, UAT environment]
tags: [devops, deployment-environments, testing]
---

A build can pass every QA test and still be rejected by the people who asked for it. The checkout flow works exactly as the ticket described, and the finance team says the ticket was wrong.

Those are two different failures, and teams that sign contracts or answer to business owners test for them separately.

---

### Two questions about the same build

<mark style="background: #FFF3A3A6;">QA asks "did we build it right?", meaning does the build match the specification. UAT asks "did we build the right thing?", meaning does it actually serve the business that will use it.</mark>

User acceptance testing (UAT) takes its name from contracts: the client *accepts* delivery of the work, the way a buyer accepts goods. Until the users sign, the release is not accepted.

| | QA | UAT |
|---|---|---|
| Run by | QA engineers | Business users, product owners, the client |
| Checks against | The specification | Real workflows and business needs |
| Finds | Defects, regressions | Missing or misunderstood requirements |
| Produces | A defect report | A formal sign-off that authorizes release |

---

### Why UAT gets its own environment

Business users test real workflows, so the data has to look real: realistic customers, realistic order volumes, the reports they actually read. A QA environment full of mock records and half-tested builds gives them nothing they can judge.

They also need the build to stay frozen while they work through it, often for days, which would block QA from testing the next build.

<mark style="background: #ADCCFFA6;">UAT starts only after QA has passed the build; business users should never be the people finding broken APIs or missing validation.</mark>

---

### When UAT disappears

<mark style="background: #FF5582A6;">A product company with no external client often has no UAT environment at all: the product owner reviews on staging or on a per-PR preview, and the sign-off is a merge approval rather than a document.</mark>

UAT survives where acceptance is contractual or regulated: outsourcing shops, banks, government and healthcare.

---

### Read more
- [[An integration environment absorbs breakage so the QA environment can stay stable]]
- [[Staging mirrors production config, data and infrastructure so the deploy itself can be rehearsed]]
- [[Ephemeral preview environments give each pull request its own isolated copy instead of a shared queue]]
- [[Each deployment environment exists to keep one workload from corrupting another's results]]
- [[DevOps - MOC]]
- [[Testing - MOC]]

### External Resources
- [Playcode: UAT vs QA, separate acceptance from quality assurance](https://playcode.io/blog/uat-vs-qa)
