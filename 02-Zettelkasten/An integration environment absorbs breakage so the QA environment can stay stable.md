---
created: 2026-10-14
aliases: [dev environment, integration environment, QA environment, test environment]
tags: [devops, deployment-environments, testing]
---

A developer's laptop proves that one person's change works on its own. It cannot prove that the change still works next to the twenty other changes merged the same day, against a real database and real neighbouring services.

Two shared environments answer that question, and they are kept apart because they need opposite things from the machine they run on.

---

### The integration environment is allowed to break

<mark style="background: #FFF3A3A6;">An integration environment (often just called dev) is a shared server where every merged change is deployed automatically, so the team learns quickly whether their changes work together.</mark>

The name says what it does: it *integrates* separately written changes into one running system.

It receives a new deploy many times a day. A broken migration, a misconfigured service or two incompatible changes will take it down regularly, and that is the point. Every failure found here is one that never reached a tester or a user.

---

### The QA environment must stay still

<mark style="background: #FFF3A3A6;">A QA environment (also called test) is a shared server where testers verify that a specific build behaves as specified and that nothing old has broken.</mark>

A tester running a regression suite needs the ground to stay still. If a new deploy lands halfway through, a failing check can mean either a real bug or a build that changed under them, and the tester cannot tell which.

So QA receives a chosen build on a slower schedule, usually one promoted from integration after it passed there, and keeps it until testing finishes.

---

### Why one shared box fails both groups

<mark style="background: #ABF7F7A6;">Developers need an environment that changes constantly and testers need one that never changes during a test run, so a single shared box makes one group wait or corrupts the other's results.</mark>

Merge them and either developers stop deploying while QA tests, which slows delivery, or QA files bugs caused by half-finished work, which wastes everyone's time.

<mark style="background: #FF5582A6;">Small teams often merge the two and live with the cost; the split pays off once enough people deploy daily that collisions become routine.</mark>

---

### Read more
- [[QA checks a build matches the spec while UAT checks it is the right thing for the business]]
- [[Each deployment environment exists to keep one workload from corrupting another's results]]
- [[Immutable artifact promotion promotes the same build through environments without rebuilding]]
- [[DevOps - MOC]]

### External Resources
- [SQLServerCentral: Why do I need all these servers](https://www.sqlservercentral.com/blogs/why-do-i-need-all-these-servers)
- [AWS Prescriptive Guidance: Understanding the DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/understanding-the-devops-environments.html)
