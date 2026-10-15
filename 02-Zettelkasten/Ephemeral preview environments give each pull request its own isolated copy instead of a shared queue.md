---
created: 2026-10-14
aliases: [preview environment, ephemeral environment, per-PR environment, review app]
tags: [devops, deployment-environments, ci-cd]
---

A team with one shared QA or staging server can test only one set of changes at a time. Ten open pull requests either queue for the server or get merged together and tested as a blur, and when something breaks nobody knows which change did it.

---

### One throwaway environment per pull request

<mark style="background: #FFF3A3A6;">An ephemeral preview environment is a complete, isolated copy of the application that CI creates automatically for one pull request and destroys when the pull request is merged or closed.</mark>

*Ephemeral* comes from the Greek for "lasting a day": the environment is built to be thrown away.

A typical setup creates, per pull request:

- a Kubernetes namespace running that branch's build
- its own database, seeded with test data
- a unique URL, posted as a comment on the pull request

Reviewers, testers and the product owner click the link and see that change running end to end, with nothing else mixed in.

---

### What it fixes about shared environments

<mark style="background: #ABF7F7A6;">Because each pull request gets its own environment with no shared state, parallel changes stop waiting for each other and a failure points to exactly one change.</mark>

It also removes slow drift, since every environment is built fresh from the same definition instead of being patched by hand for months.

Plane, Vercel and Uber (with its internal SLATE tool) describe replacing most shared-staging use this way.

---

### The hard part is data and dependencies

Spinning up the application is easy. The difficulty is everything it talks to: databases, queues, third-party APIs and the other microservices it calls. Options include a seeded database per environment, database branching, or routing calls to shared stable versions of other services.

<mark style="background: #FF5582A6;">A preview environment must never point at production data; it is short-lived, widely shared by link, and rarely protected like production.</mark>

Preview environments replace the shared queue for feature review, but they rarely replace staging's production-sized data and infrastructure for load tests and migration rehearsals.

---

### Read more
- [[Each deployment environment exists to keep one workload from corrupting another's results]]
- [[Staging always drifts from production so passing there gives false confidence]]
- [[Staging mirrors production config, data and infrastructure so the deploy itself can be rehearsed]]
- [[Trunk-based development keeps a single main branch with short-lived feature branches]]
- [[DevOps - MOC]]
- [[Kubernetes - MOC]]

### External Resources
- [Plane: How we replaced shared staging with ephemeral deployment previews](https://plane.so/blog/how-we-replaced-shared-staging-with-ephemeral-deployment-preview)
- [Vercel: Ephemeral environments](https://vercel.com/i/ephemeral-environments)
- [Signadot: Why staging doesn't scale for microservice testing](https://dev.to/signadot/why-staging-doesnt-scale-for-microservice-testing-d4j)
