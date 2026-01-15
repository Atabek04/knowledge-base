---
created: 2026-01-06
tags: [virtualization/vms]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

Hypervisors come in two architecturally different types, distinguished by where they run and what manages the physical hardware.

| Aspect | Type 1 (Bare-metal) | Type 2 (Hosted) |
|--------|-----------|----------|
| **Runs On** | Directly on hardware | On top of Host OS |
| **Host OS Required** | No Host OS needed | Requires Host OS |
| **Privilege Level** | Highest (act as the OS) | Lower (as application) |
| **Primary Use** | Enterprise servers, data centers | Personal computers, development |

**Type 1 Hypervisor (Bare-metal)**

Type 1 hypervisor installs directly on physical hardware with no Host OS in between. The hypervisor **becomes** the operating system—the first software that runs after bootloader. The hypervisor talks to hardware directly.

Examples: VMware ESXi, Microsoft Hyper-V, Xen, KVM

When you power on a server with Type 1, ESXi boots directly. ESXi manages the physical CPU, RAM, and devices. Guest OSs run on top of ESXi as applications managed by the hypervisor.

**Type 2 Hypervisor (Hosted)**

Type 2 hypervisor installs as an application on an existing Host OS. The Host OS manages physical hardware directly. The hypervisor runs as a privileged application under the Host OS. Guest OSs run inside the hypervisor, which is inside the Host OS.

Examples: VirtualBox, VMware Workstation, Parallels

When you install VirtualBox on your Windows laptop, VirtualBox is just another application running under Windows. Windows still controls the real hardware. VirtualBox uses Windows system calls to allocate RAM, access disk, manage network.

![[hypervisor-types.png]]

**Architectural Implications**

Type 1 is simpler architecturally—one layer of privilege. The hypervisor has direct hardware control and can be highly optimized for virtualization.

Type 2 requires the Host OS to mediate hardware access. This adds complexity and overhead.

For enterprise data centers, Type 1 is standard because multiple hypervisor instances can coexist directly on hardware, and performance is critical.

For development and testing, Type 2 is convenient because you run virtualization alongside your normal OS.

## Links
- [[Type 1 hypervisor is faster due to direct hardware access]]
- [[Hypervisor creates and manages virtual machines by dividing physical resources]]
- [[Guest OS runs inside VM while Host OS runs on physical hardware]]
- [[VMs & Containers MOC]]
