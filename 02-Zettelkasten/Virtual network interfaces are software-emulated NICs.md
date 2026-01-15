---
created: 2026-01-06
tags: [virtualization/containers]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

A **virtual network interface** is software that emulates a physical Network Interface Card (NIC). The operating system kernel pretends that a hardware NIC exists, but the "NIC" is entirely software—there's no physical device.

**Physical vs Virtual NIC:**

A physical NIC is a hardware component:
- Has circuitry to transmit/receive electrical signals
- Has a unique MAC address burned into ROM
- Physically connects to network cable or WiFi antenna
- Cannot be duplicated (one device = one NIC)

A virtual NIC is software:
- Kernel simulates network behavior in code
- Can have any MAC address (software-assigned)
- Doesn't connect to physical medium (software routes packets)
- Can create unlimited virtual NICs (one physical can support many virtual)

**How Virtual NICs Work:**

When a container (in NET namespace) configures a network interface, it's configuring a virtual NIC. The kernel:

1. Creates a virtual interface (e.g., `eth0` inside container)
2. Assigns it a software MAC address
3. Simulates sending/receiving packets through code

When the container sends a network packet to eth0, the kernel intercepts it and routes it appropriately (to another container, to host, or to outside world).

**Example:**

```bash
# Inside container
ip link set eth0 up
ip addr add 172.17.0.2/16 dev eth0
```

This configures a virtual interface that doesn't physically exist. The container believes eth0 is a real network card. The kernel makes it behave exactly like a real card from the container's perspective.

**Virtual MAC Addresses:**

Each virtual NIC has a unique MAC address:
- Container A eth0: `02:42:ac:11:00:02`
- Container B eth0: `02:42:ac:11:00:03`

These MAC addresses are software-generated. The kernel remembers which container owns which MAC. When a packet arrives for MAC `02:42:ac:11:00:02`, the kernel delivers it to Container A.

**Comparison to Real NICs:**

| Aspect | Physical NIC | Virtual NIC |
|--------|--------------|------------|
| **Hardware** | Actual device | Software only |
| **Count** | Limited by hardware | Unlimited |
| **MAC Address** | Hardware-burned | Software-assigned |
| **Speed** | Limited by medium | Limited by CPU/memory |
| **Latency** | Microseconds | Microseconds (very low) |

Virtual NICs are fast enough for practical purposes. Container-to-container communication has minimal overhead.

## Links
- [[NET namespace gives each container isolated network stack]]
- [[Docker bridge connects container networks to host NIC]]
- [[Namespaces isolate what container processes can see]]
- [[Hypervisor creates and manages virtual machines by dividing physical resources]]
- [[VMs & Containers MOC]]
