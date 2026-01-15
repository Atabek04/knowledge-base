---
created: 2026-01-06
tags: [virtualization/vms]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

Each virtual machine requires a complete, full-featured Guest OS with its own kernel. This architectural requirement makes VMs resource-heavy in terms of memory consumption and disk usage.

A typical Guest OS (Linux, Windows, macOS) includes:

- **OS Kernel** — millions of lines of code for process management, memory management, device drivers, system calls
- **System Libraries** — libc, pthread, system utilities
- **System Services** — init daemon, logging, device management, network stack
- **Device Drivers** — drivers for virtual CPU, virtual disk, virtual network (provided by hypervisor)
- **Shell and Utilities** — bash, ls, grep, and hundreds of other command-line tools

Just the OS kernel and basic system processes consume **several hundred MB to several GB of RAM per VM**. A Linux VM might use 500MB-1GB just for the OS before any application runs.

**Resource Multiplication Problem:**

If you run 10 VMs on a server with 128GB RAM:

- VM 1 OS: 1GB
- VM 2 OS: 1GB
- VM 3 OS: 1GB
- ... (repeated 10 times)
- **Total wasted on duplicate OS instances: 10GB**

That 10GB could have run applications. Instead, it runs 10 independent OS kernels all doing essentially the same work—process scheduling, memory management, device handling—with 90% redundancy.

Each VM also requires its own disk image file. A minimal Linux VM might be 2-5GB. Ten VMs = 20-50GB of disk space just for operating system images. Again, substantial waste.

![[vm-heavy.png]]

**Boot Time Impact:**

Each VM must boot its own OS from scratch. Starting a VM takes minutes (OS initialization, service startup, configuration loading). Starting 10 VMs means waiting 10x boot time.

This is why containers emerged as an alternative. Containers eliminate the Guest OS layer entirely, sharing the Host OS kernel and reducing resource consumption by 90%.

## Links
- [[VM architecture layers from hardware through Guest OS to applications]]
- [[Containerization solves VM heaviness by sharing the Host OS kernel]]
- [[Virtual Machine emulates complete physical computer in software]]
- [[VMs & Containers MOC]]
