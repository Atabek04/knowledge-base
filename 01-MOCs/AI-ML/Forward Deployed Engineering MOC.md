---
created: 2026-10-10
tags: [moc]
aliases: [FDE, Forward Deployed Engineer]
---

A forward deployed engineer (FDE) is a software engineer embedded with a customer, who builds and ships production software inside the customer's environment and owns the result after the sale.

The role sits between three things this vault already covers: building AI products ([[AI Engineering MOC]]), designing systems ([[System Design - MOC]]), and working with people ([[Soft Skills & Leadership - MOC]]). This MOC is the roadmap for the skills that only the combination demands.

## The Role

- [ ] FDE: a product engineer who ships inside the customer's production, not a consultant
- [ ] Forward deployed: military origin, working at the front instead of headquarters
- [ ] Palantir's Delta and Echo: engineer and deployment strategist paired on one customer
- [ ] FDE vs sales engineer vs solutions engineer: who owns production after the sale
- [ ] Field fixes become product features: the FDE as the product team's discovery channel
- [ ] Why AI labs hire FDEs: models are general, value appears only inside one workflow

## Technical Discovery

- [ ] Technical discovery: turning a vague complaint into a scoped, testable problem
- [ ] Workflow mapping before building: find where the work actually happens
- [[BRD captures why the system is being built before any technical work begins|BRD: the business why, written before any technical work]]
- [[SRS bridges business requirements and technical implementation|SRS: translates business requirements into technical ones]]
- [[User stories express requirements as role-action-benefit statements|User stories: role, action, benefit]]
- [[BPMN comes before UML because process understanding precedes system design|BPMN before UML: understand the process, then design the system]]

## Deploying LLM Systems for a Customer

- [[RAG retrieves the documents a question needs at query time so the model reads only those|RAG: fetch only the documents a question needs]]
- [[Context engineering curates everything in the window and not the wording of one message|Context engineering: curate the whole window, not one prompt]]
- [ ] Evals decide whether a customer deployment works, not demos
- [ ] MCP servers connect a model to a customer's own systems
- [ ] Enterprise constraints: security review, data access, and legacy systems shape the design
- [ ] Production ownership: monitoring, on-call and rollback after go-live

## Working With Customers

- [ ] Translating trade-offs into money, time and risk for non-engineers
- [ ] Scope creep without a spec: saying no while keeping the account
- [ ] Measuring adoption after launch: shipped is not the same as used

## Career Path

- [ ] SWE to FDE: the gap is discovery and ambiguity, not code
- [ ] AI engineer to FDE: the stack is there, the customer half is missing
- [ ] FDE interview loops: decomposition and explain-to-a-non-engineer rounds
- [ ] FDE trade-offs: travel, burnout, and the services-in-disguise risk
- [ ] Reading an FDE posting: engineering org or professional services org

### Read more

- [[AI Engineering MOC]]
- [[Agentic Engineering MOC]]
- [[System Design - MOC]]
- [[Behavioral Interview - MOC]]
- [[Soft Skills & Leadership - MOC]]
