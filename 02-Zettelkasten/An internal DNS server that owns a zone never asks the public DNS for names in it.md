---
created: 2026-10-29
tags: [networking/dns]
aliases: [DNS zone, authoritative zone, zone shadowing, SOA record]
---

A [[DNS resolves a domain name to an IP address by asking a resolver|resolver]] that does not know a name normally asks further up the chain until it finds the server responsible for it. One configuration stops that chain.

<mark style="background: #FFF3A3A6;">A DNS zone is the set of names under one domain, such as everything ending in `.example.com`; the server that holds the zone is authoritative for it, and its SOA (Start of Authority) record names the zone's primary server.</mark>

---

#### Why a local copy hides the public records

When an internal DNS server holds its own copy of a public company's zone, it believes it is the authority for every name in it.

<mark style="background: #ABF7F7A6;">An authoritative server answers from its own records only: a name missing from the local copy gets "does not exist" (NXDOMAIN), and the server never forwards the question to public DNS.</mark>

So the same name can resolve fine from home and fail at the office.

---

#### How to tell which server owns a zone

Ask both resolvers for the zone's SOA record and compare the primary server names, for example `Resolve-DnsName example.com -Type SOA -Server <resolver>` on Windows or `dig SOA example.com @<resolver>` on Linux.

<mark style="background: #ADCCFFA6;">A different SOA primary inside and outside means two separate copies of the zone, and every name must be added to both.</mark>

---

### Read more
- [[DNS resolves a domain name to an IP address by asking a resolver]]
- [[Split-horizon DNS gives different answers for the same name depending on who asks]]
- [[Networking MOC]]
