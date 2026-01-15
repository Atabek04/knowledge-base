---
created: 2026-01-06
tags: [virtualization/containers]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

The **NET (Network) namespace** isolates the network stack so each container has its own IP address, ports, routing table, and network interfaces. Containers cannot see or interfere with each other's network configuration.

**Isolated Network Components:**

Each NET namespace includes:
- **Virtual network interface** (e.g., eth0)
- **IP address** (e.g., 172.17.0.2)
- **Routing table** (rules for where packets go)
- **Iptables rules** (firewall configuration)
- **Open ports** (network listeners)

All these are completely isolated per namespace. Two containers can both bind to port 80 without conflict because each has its own port space.

**Example: Two Containers with Same Port**

Container A (NET namespace #1):
```
Virtual NIC: eth0
IP: 172.17.0.2
Ports: 80, 443 (isolated)
Routing table: (own copy)
```

Container B (NET namespace #2):
```
Virtual NIC: eth0
IP: 172.17.0.3
Ports: 80, 443 (isolated, different namespace)
Routing table: (own copy)
```

**Port Binding:**

Both containers can bind to port 80. From Container A's perspective, port 80 is open. From Container B's perspective, port 80 is also open. **Zero conflict** because they're in different namespaces.

Without NET namespace isolation: two applications binding port 80 = error (port already in use).

**Isolation Mechanism:**

When Container A sends network traffic, it goes through its isolated network stack. Container B's traffic goes through a completely separate stack. The host kernel manages both stacks independently.

A container cannot:
- See other containers' IP addresses
- Sniff other containers' network traffic
- Send packets that appear to come from other containers' IPs
- Access other containers' open ports

**Network Connectivity:**

Even though containers are isolated, they need to communicate with the outside world. How?

The host creates a **virtual network bridge** (essentially a virtual switch) that connects all container networks:

```
┌────────────────────────────────────────────────────┐
│ Host System                                        │
│                                                    │
│  Container A (NET ns #1)                           │
│  IP: 172.17.0.2                                    │
│      │                                             │
│      └──────┬─────────────────┐                   │
│             │                 │                   │
│  ┌──────────┴─────────────────┴──────────┐        │
│  │  docker0 bridge (172.17.0.1)          │        │
│  │  (virtual switch connecting all)      │        │
│  └───────────────┬────────────────────────┘        │
│                  │                                 │
│             Real NIC (eth0)                        │
│                  │                                 │
│              Internet                              │
└────────────────────────────────────────────────────┘
```

Container A's packets go: veth0 → docker0 bridge → real NIC → Internet.

Container A can communicate with Container B through the bridge, or with outside world through the real NIC. But Container A's network is completely isolated—it doesn't share the host's network stack.

## Links
- [[Virtual network interfaces are software-emulated NICs]]
- [[Docker bridge connects container networks to host NIC]]
- [[Namespaces isolate what container processes can see]]
- [[Namespaces provide isolation while cgroups provide resource fairness]]
- [[VMs & Containers MOC]]
