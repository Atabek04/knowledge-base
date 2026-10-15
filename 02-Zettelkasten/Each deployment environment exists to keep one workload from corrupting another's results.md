---
created: 2026-10-14
aliases: [deployment environments, why so many environments, environment pipeline, dev QA UAT staging prod]
tags: [devops, deployment-environments]
---

A common objection to a long environment pipeline: developers test locally, testers test on a test server, users use production, so two shared environments should be enough.

The objection holds until several groups need that one test server at the same time, for things that ruin each other's results.

---

### One environment per clashing workload

<mark style="background: #ABF7F7A6;">A new environment is added whenever two groups need the same server for incompatible work, so each environment in a pipeline marks a collision that once cost someone time.</mark>

| Environment | Used by | Question it answers |
|---|---|---|
| Local | One developer | Does my change work at all? |
| Integration (dev) | All developers | Does it work with everyone else's merged code? |
| QA (test) | QA engineers | Does the build match the spec, with no regressions? |
| UAT | Business users, the client | Is this the right thing for the business? |
| Staging (pre-prod) | Ops, SRE, release engineers | Will this exact build deploy and run on production-like infrastructure? |
| Production | Real users | Live traffic |

Each split resolves one specific collision:

- **Integration vs QA**: developers need constant deploys and testers need a frozen build. See [[An integration environment absorbs breakage so the QA environment can stay stable|why dev and QA split]].
- **QA vs UAT**: testers check the spec, business users check fitness, and each needs the build frozen for days. See [[QA checks a build matches the spec while UAT checks it is the right thing for the business|QA vs UAT]].
- **QA vs staging**: a load test on the QA box makes testers report slowness that is not a bug, and QA hardware is too cheap to rehearse a real deploy. See [[Staging mirrors production config, data and infrastructure so the deploy itself can be rehearsed|what staging rehearses]].

The same build travels the whole chain unchanged, via [[Immutable artifact promotion promotes the same build through environments without rebuilding|immutable artifact promotion]].

---

### Environment count depends on the company

<mark style="background: #FF5582A6;">The number of environments reflects a company's regulation, contracts and team size, not its engineering skill; fewer environments is not automatically worse.</mark>

#### Startups and product teams: three

Dev, staging and prod is the most common baseline. QA happens on staging, the product owner signs off there, and there is no separate UAT because there is no external client.

#### Enterprises and regulated industries: five or more

Banks, healthcare, government and outsourcing shops run dev, QA, UAT, staging and prod, sometimes with separate performance or disaster-recovery copies. Auditors and client contracts require a documented acceptance step, so the count is set partly outside engineering.

#### Test-in-production teams: no staging

Some high-velocity teams run only local, CI and production, and make production itself safe to test in. See [[Staging always drifts from production so passing there gives false confidence|why they drop staging]].

---

### The cost of each extra environment

Every environment needs servers, data refreshes, configuration and someone to fix it when it breaks. <mark style="background: #ADCCFFA6;">Add an environment only to separate two workloads that actually collide; one that settles no collision is overhead.</mark>

Shared environments also queue work: ten pull requests wait in line for one QA box. [[Ephemeral preview environments give each pull request its own isolated copy instead of a shared queue|Per-PR preview environments]] remove that queue.

---

### Read more
- [[An integration environment absorbs breakage so the QA environment can stay stable]]
- [[QA checks a build matches the spec while UAT checks it is the right thing for the business]]
- [[Staging mirrors production config, data and infrastructure so the deploy itself can be rehearsed]]
- [[Staging always drifts from production so passing there gives false confidence]]
- [[Ephemeral preview environments give each pull request its own isolated copy instead of a shared queue]]
- [[Immutable artifact promotion promotes the same build through environments without rebuilding]]
- [[DevOps - MOC]]

### External Resources
- [AWS Prescriptive Guidance: Understanding the DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/understanding-the-devops-environments.html)
- [Guidewire: Development environments, how many do you need](https://www.guidewire.com/resources/blog/technology/development-environments-how-many-do-you-need)
- [SQLServerCentral: Why do I need all these servers](https://www.sqlservercentral.com/blogs/why-do-i-need-all-these-servers)
