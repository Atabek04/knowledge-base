---
created: 2026-10-29
tags: [networking/nat]
aliases: [hairpin NAT, NAT loopback, NAT reflection, hairpinning]
---

[[Destination NAT forwards traffic from a public IP to a private server|Destination NAT]] handles visitors from the internet. A machine already inside the same network that uses the public address takes a strange route: out to the edge device, then back in.

<mark style="background: #FFF3A3A6;">Hairpin NAT (NAT loopback, NAT reflection) is the edge device accepting traffic from the inside aimed at its own public IP and turning it back inside to the private server.</mark>

The name comes from the path: the packet goes out to the edge and makes a U-turn, like a hairpin bend in a road.

---

#### Why it is often missing

Many firewalls only apply DNAT to traffic arriving on the outside interface. An inside request to the public IP then times out or is refused.

<mark style="background: #ABF7F7A6;">Even when hairpinning works, every inside call takes a detour through the edge device and adds load to it.</mark>

<mark style="background: #ADCCFFA6;">Inside clients should reach inside servers by their private address; the usual way to give them that address is split-horizon DNS.</mark>

---

### Read more
- [[Destination NAT forwards traffic from a public IP to a private server]]
- [[Split-horizon DNS gives different answers for the same name depending on who asks]]
- [[Networking MOC]]
