---
created: 2026-10-29
tags: [networking/dns, kubernetes]
aliases: [hosts file, etc hosts, hostAliases]
---

Before asking any [[DNS resolves a domain name to an IP address by asking a resolver|DNS resolver]], an operating system checks a local text file of fixed name-to-IP pairs.

<mark style="background: #FFF3A3A6;">The hosts file (`/etc/hosts` on Linux, `C:\Windows\System32\drivers\etc\hosts` on Windows) maps names to IPs on one machine and is checked before DNS, so its entries override whatever DNS would answer.</mark>

<mark style="background: #FFF3A3A6;">Kubernetes `hostAliases` is a list in the pod spec that the kubelet writes into the pod's `/etc/hosts`, so it overrides DNS for that pod only.</mark>

---

#### Why teams use it

When there is no [[Split-horizon DNS gives different answers for the same name depending on who asks|internal DNS]] that returns private addresses, the hosts file is how one machine gets them anyway.

---

#### Why it does not scale

<mark style="background: #FF5582A6;">Every machine and every deployment manifest carries its own copy, so changing one IP means editing every copy, and a missed one keeps the old address silently.</mark>

<mark style="background: #FF5582A6;">On Windows the first matching line wins, so a stale duplicate above the correct line shadows it.</mark>

<mark style="background: #ADCCFFA6;">Use the hosts file for a local experiment; for shared infrastructure, put the records in internal DNS once.</mark>

---

### Read more
- [[DNS resolves a domain name to an IP address by asking a resolver]]
- [[Split-horizon DNS gives different answers for the same name depending on who asks]]
- [Kubernetes: Adding entries to Pod /etc/hosts with HostAliases](https://kubernetes.io/docs/tasks/network/customize-hosts-file-for-pods/)
- [[Networking MOC]]
