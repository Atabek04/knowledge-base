---
created: 2026-01-06
tags: [virtualization/containers]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

The **Docker bridge** is a virtual network switch that connects all container networks to the host system and the outside world. Without this bridge, containers would be completely isolated from each other and from the network.

**Docker Bridge Design:**

When Docker starts, it creates a virtual bridge interface (typically named `docker0`) on the host:

```
Host System:
┌─────────────────────────────────────────────────┐
│                                                 │
│  docker0 bridge (IP: 172.17.0.1/16)            │
│  ├─ Virtual interface connected to all configs │
│  └─ Acts like a virtual switch                 │
│                                                 │
│       ↑        ↑        ↑        ↑             │
│       │        │        │        │             │
│    Container Container Container ...          │
│     veth0a   veth0b   veth0c                   │
│    172.17.. 172.17.. 172.17..                  │
└─────────────────────────────────────────────────┘
       ↓
    Real NIC (eth0)
       ↓
    Network / Internet
```

**How It Works:**

Each container connects to the bridge through a virtual interface pair:

- **Inside container:** `eth0` (virtual NIC in container's NET namespace)
- **On host side:** `veth0a`, `veth0b`, etc. (virtual Ethernet pair)

These two interfaces are connected directly—packets sent from container eth0 appear on veth0a on the host side.

**Network Path:**

```
Container A (172.17.0.2):
App sends packet to 172.17.0.3 (Container B)
       ↓
eth0 in container's namespace (virtual NIC)
       ↓
vethXXX on host (the paired interface)
       ↓
docker0 bridge (receives packet)
       ↓
Bridge inspects destination IP (172.17.0.3)
       ↓
Delivers to vethYYY (paired to Container B)
       ↓
Container B's eth0 (packet appears here)
       ↓
Container B application receives packet
```

**Accessing Outside World:**

When Container A needs to reach external network (e.g., 8.8.8.8):

```
Container A (172.17.0.2):
App sends packet to 8.8.8.8
       ↓
vethXXX → docker0 bridge
       ↓
Bridge: "172.17.0.2 is not local, route outside"
       ↓
NAT (Network Address Translation)
Rewrites source IP: 172.17.0.2 → host IP (e.g., 192.168.1.100)
       ↓
Real NIC (eth0)
       ↓
Internet (packet leaves with host IP)
       ↓
Response comes back with host IP
       ↓
NAT reverses translation: 192.168.1.100 → 172.17.0.2
       ↓
Container A eth0 (response appears here)
```

Containers appear to communicate with the outside world, but their internal IPs (172.17.x.x) are translated to the host's IP. The outside world never sees container IPs.

**Container-to-Container Communication:**

Containers on the same bridge can communicate directly with their container IPs:

```
Container A → (172.17.0.2:8080) → docker0 → (no NAT needed) → Container B (172.17.0.3)
```

This is why you can have multiple containers on the same host, each with their own IP, and they can all find each other.

## Links
- [[Virtual network interfaces are software-emulated NICs]]
- [[NET namespace gives each container isolated network stack]]
- [[Namespaces provide isolation while cgroups provide resource fairness]]
- [[VMs & Containers MOC]]
