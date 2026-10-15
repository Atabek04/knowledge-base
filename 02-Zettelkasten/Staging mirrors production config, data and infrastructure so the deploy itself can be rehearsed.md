---
created: 2026-10-14
aliases: [staging, staging environment, pre-production, pre-prod]
tags: [devops, deployment-environments, release]
---

Code can be correct and the release can still fail. A migration that took two seconds on a test database locks a 500-million-row table for forty minutes, a secret is missing from the production vault, or the load balancer rejects the new health-check path.

None of those are logic bugs, so QA cannot catch them. They show up only where the configuration, data and infrastructure match production.

---

### Production without the users

<mark style="background: #FFF3A3A6;">Staging is an environment built to match production as closely as possible (same infrastructure, same configuration, production-sized data) so a release can be tried there before real users see it.</mark>

The name comes from a *staging area*: the place where goods or troops are assembled and checked before the final move.

It usually receives the exact artifact that will go live, which is why [[Immutable artifact promotion promotes the same build through environments without rebuilding|building once and promoting the same artifact]] matters. A rebuilt binary would make the rehearsal test something other than what ships.

---

### What staging catches that QA cannot

<mark style="background: #ABF7F7A6;">Staging tests the deploy, not just the code: migrations against realistic data volumes, production configuration and secrets, network rules, and the rollback procedure itself.</mark>

- **Migrations**: run against a recent copy of production data, so duration and locking are realistic.
- **Configuration**: the real feature toggles, connection pools, timeouts and certificates.
- **Infrastructure**: the same load balancer, the same autoscaling rules, the same service mesh.
- **Performance**: load tests on prod-class hardware, kept off QA so they do not distort testers' results.

---

### Why it costs more than any other environment

Matching production means paying for production-class machines and keeping a refreshed, anonymized copy of production data. That is why staging is rarely used for everyday feature testing.

<mark style="background: #FF5582A6;">A staging copy of production data must be anonymized before anyone tests on it; real customer records in a less protected environment are a breach waiting to happen.</mark>

---

### Read more
- [[Immutable artifact promotion promotes the same build through environments without rebuilding]]
- [[Staging always drifts from production so passing there gives false confidence]]
- [[Each deployment environment exists to keep one workload from corrupting another's results]]
- [[Database migrations version schema changes while backups recover data loss — they are never substitutes]]
- [[DevOps - MOC]]

### External Resources
- [Increment: Best practices for staging environments](https://increment.com/development/center-stage-best-practices-for-staging-environments/)
- [Shipyard: Staging environments vs test environments](https://shipyard.build/blog/staging-environments-vs-test-environments/)
