---
created: 2026-10-29
tags: [networking/nat]
aliases: [destination NAT, DNAT, port forwarding, public IP, private IP]
---

Servers in a data centre live on [[Routers have private IP for LAN and public IP for internet|private addresses]] such as `10.x.x.x`. The internet cannot route to those addresses at all, so a visitor from outside needs some other way in.

<mark style="background: #FFF3A3A6;">Destination NAT (DNAT, also called port forwarding) is a rule on the edge device that rewrites the destination of incoming traffic from its public IP to a private server's IP, then forwards it inside.</mark>

The name is literal: **N**etwork **A**ddress **T**ranslation applied to the **destination** address.

---

#### How a request flows through it

1. The client connects to the public IP, which belongs to the edge device (a firewall or router), not to the server.
2. The edge device matches a rule, for example "public IP port 443 goes to `10.0.0.5:443`", and rewrites the packet.
3. The server answers; the reply goes back through the same device, which swaps the public address back in.

<mark style="background: #ABF7F7A6;">The client only ever sees the public address, so the real servers stay hidden and only the ports the rules open are reachable.</mark>

---

#### Office building analogy

The public IP is the building's street address with a guard at the door. Rooms inside have their own numbers. Visitors must come through the door and the guard walks them to the room; people already inside walk to the room directly.

<mark style="background: #FF5582A6;">Opening a port in the NAT rule is not enough on its own: most firewalls also need an allow rule for that traffic.</mark>

---

### Read more
- [[Routers have private IP for LAN and public IP for internet]]
- [[Firewall filters incoming connections by rule before they reach a server]]
- [[Hairpin NAT lets an inside client reach an inside server through its public address]]
- [[Networking MOC]]
