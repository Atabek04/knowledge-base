---
created: 2026-01-06
tags: [virtualization/vms]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

Before virtualization existed, one physical server ran one operating system which ran one application. This created several critical business and technical problems.

**Underutilization and Waste** — a typical application uses only 10-20% of server CPU and memory. The remaining 80-90% sat idle, doing nothing. A company needed 100 servers for its 100 applications, even though each server had 90% unused capacity. This was extremely wasteful.

**Cost** — buying 100 physical servers is expensive. Each needs electricity, cooling, physical space in a data center, and IT staff to maintain. The cost of unused hardware was enormous.

**Slow Provisioning** — provisioning a new server meant ordering hardware, waiting for delivery (weeks), installing it physically, configuring OS, installing software, and testing. This entire process took weeks or months. Responding to business needs was slow.

**Application Isolation Problems** — if multiple applications ran on the same OS, conflicts occurred. One application might require Java 8, another Java 11. One might bind port 8080, another needs the same port. Restarting one application for updates affected all others.

Virtualization solved all these problems by allowing **multiple isolated operating systems on a single physical machine**. A server with 90% idle capacity could now run 9 virtual machines, each with its own OS and application. This multiplied hardware efficiency immediately.

New VMs could be created in minutes instead of weeks. Each VM had isolated configuration, independent Java versions, independent ports. Applications no longer affected each other.

Virtualization became the foundation of cloud computing and modern data centers. Companies like Amazon, Microsoft, and Google built their cloud services entirely on virtualization technology.

## Links
- [[Virtual Machine emulates complete physical computer in software]]
- [[Hypervisor creates and manages virtual machines by dividing physical resources]]
- [[VMs & Containers MOC]]
