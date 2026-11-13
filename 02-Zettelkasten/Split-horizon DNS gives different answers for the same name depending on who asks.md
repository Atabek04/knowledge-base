---
created: 2026-10-29
tags: [networking/dns]
aliases: [split-horizon DNS, split DNS, split-brain DNS, internal DNS]
---

A service with a public address for internet users and a private address for internal callers has one name but two correct answers. [[DNS resolves a domain name to an IP address by asking a resolver|DNS]] has to give each caller the right one.

<mark style="background: #FFF3A3A6;">Split-horizon DNS answers the same domain name with different IP addresses depending on where the question comes from: the public IP for the internet, the private IP for the internal network.</mark>

The name is a picture: each side sees its own horizon. Internet users see the front door; insiders see the room.

---

#### How it is usually built

- **Public DNS** holds records pointing at the public IP behind the edge device.
- **Internal DNS** holds the same names pointing at private IPs; office PCs and servers use it as their resolver.

<mark style="background: #ABF7F7A6;">Inside traffic then goes straight to the private server and never needs hairpin NAT through the edge.</mark>

---

#### The maintenance trap

<mark style="background: #FF5582A6;">The two record sets are separate: a name added to public DNS does not appear in internal DNS automatically, and internal clients get "name does not exist" until someone adds it there too.</mark>

Without an internal DNS that owns these records, teams fall back to overriding names per machine, which scales badly.

---

### Read more
- [[DNS resolves a domain name to an IP address by asking a resolver]]
- [[Hairpin NAT lets an inside client reach an inside server through its public address]]
- [[An internal DNS server that owns a zone never asks the public DNS for names in it]]
- [[Hosts file and Kubernetes hostAliases override DNS for one machine or one pod]]
- [[Networking MOC]]
