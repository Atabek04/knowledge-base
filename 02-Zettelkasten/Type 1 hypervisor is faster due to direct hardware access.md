---
created: 2026-01-06
tags: [virtualization/vms]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

Type 1 and Type 2 hypervisors have fundamentally different performance characteristics because of how they access hardware.

**Type 1 architecture (direct):**
```
VM → Hypervisor → Hardware
(2 layers)
```

**Type 2 architecture (hosted):**
```
VM → Hypervisor → Host OS → Hardware
(3 layers)
```

Every instruction in a Guest OS that needs hardware eventually goes through these layers. With Type 2, each request passes through an extra layer (Host OS), adding overhead at each step. Every disk read, network packet, memory allocation goes through additional Host OS abstraction.

Type 1 eliminates the Host OS layer entirely. The hypervisor talks directly to hardware without intermediary. This means:

- **Fewer system calls** — Type 2 hypervisor must make Host OS syscalls to access resources; Type 1 accesses directly
- **Less context switching** — Type 2 CPU switches between VMs, hypervisor, and Host OS; Type 1 switches only between VMs and hypervisor
- **Better hardware utilization** — Type 1 can apply optimization tricks directly; Type 2 must work within Host OS constraints

In practice, Type 1 performance is 10-30% better than Type 2, depending on workload. For CPU-intensive workloads, the difference grows larger.

The Host OS in Type 2 is not bad—it's necessary for the convenience of running VMs alongside your normal operating environment. But it inherently adds overhead that Type 1 avoids.

Data centers use Type 1 because performance matters. A 20% performance gain across thousands of VMs means significant cost savings (fewer servers needed).

## Links
- [[Hypervisor Type 1 runs on bare metal while Type 2 runs on Host OS]]
- [[VM architecture layers from hardware through Guest OS to applications]]
- [[VMs & Containers MOC]]
