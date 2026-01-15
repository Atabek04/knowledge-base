---
created: 2026-01-06
tags: [virtualization/vms]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

When a **Guest OS** executes instructions that access hardware, the hypervisor intercepts these operations and handles them safely. This interception mechanism is the core of how emulation works.

The Guest OS sends hardware commands expecting real hardware. The hypervisor intercepts each command and responds appropriately, often emulating the hardware's behavior through software.

**How Emulation Works:**

1. Guest OS executes a privileged instruction (hardware operation)
2. CPU detects this is a privileged instruction in Guest mode
3. CPU triggers a trap, switching to hypervisor mode
4. Hypervisor examines the operation
5. Hypervisor performs equivalent operation on real hardware (or simulates it)
6. Hypervisor returns result to Guest OS
7. Guest OS continues, unaware the operation was intercepted

**Concrete Example: Guest OS Writes to Disk**

```
Guest OS: "Write this data to block 12345 on my disk"
         ↓ (attempts privileged disk operation)
Hypervisor intercepts the request
         ↓
Hypervisor: "I'll translate this VM disk operation to a file write"
         ↓
Hypervisor writes data to the VM's disk image file
         (file is stored on real host disk)
         ↓
Hypervisor returns "Write successful" to Guest OS
         ↓
Guest OS: "My disk write completed"
(completely unaware it wrote to a file, not a real disk)
```

The Guest OS believes it successfully wrote to a physical disk. In reality, the hypervisor translated the operation into a file write operation on the Host OS. The Guest OS cannot tell the difference because the hypervisor's response matches exactly what a real disk would return.

This same principle applies to network operations. When Guest OS configures network interface 192.168.1.100, the hypervisor creates a virtual network interface that emulates this behavior. Network packets from the VM are intercepted and routed to the real network through the hypervisor.

The beauty of this design is the Guest OS needs no knowledge of virtualization. It executes normal OS operations, and the hypervisor seamlessly translates them. This allows any OS to run as a Guest—Windows, Linux, macOS, etc.—without modification.

## Links
- [[Virtual Machine emulates complete physical computer in software]]
- [[Hypervisor creates and manages virtual machines by dividing physical resources]]
- [[VM architecture layers from hardware through Guest OS to applications]]
- [[VMs & Containers MOC]]
