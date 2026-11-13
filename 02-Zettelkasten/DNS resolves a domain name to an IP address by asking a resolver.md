---
created: 2026-10-29
tags: [networking/dns]
aliases: [DNS, DNS resolver, name resolution, NXDOMAIN, UnknownHostException]
---

Computers connect to IP addresses, people remember names. Before any HTTP request leaves a machine, the name in the URL has to become an address.

<mark style="background: #FFF3A3A6;">DNS (Domain Name System) is the internet's phone book: it turns a domain name like `example.com` into the IP address a machine can connect to.</mark>

---

#### Who answers the question

A machine never searches the whole internet itself. It asks one configured server, its **resolver**, and trusts the answer.

- A home PC asks the router or the ISP's resolver.
- An office PC asks the company's internal DNS servers.
- A public resolver such as Google's `8.8.8.8` answers anyone.

<mark style="background: #ABF7F7A6;">The answer depends on which resolver was asked, so two machines can get different addresses, or no address, for the same name.</mark>

---

#### What failure looks like

When the resolver says the name does not exist, the DNS reply code is **NXDOMAIN** ("non-existent domain").

In Java this surfaces as `java.net.UnknownHostException`: the JVM got no IP for the name, so it never even tried to connect.

<mark style="background: #FF5582A6;">`UnknownHostException` is a naming failure, not a network failure: the server may be perfectly reachable by IP.</mark>

---

### Read more
- [[IP addresses flow hierarchically from IANA through RIRs and ISPs]]
- [[Networking MOC]]
