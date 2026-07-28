---
aliases: [default security group, default SG rules, SG inbound outbound defaults]
---

Every AWS VPC comes with a "default" security group, auto-attached to any EC2 instance that isn't given a custom one.
Its default rules are asymmetric — inbound and outbound behave differently out of the box.

### Default inbound: deny external, allow same-group

<mark style="background: #FFF3A3A6; font-weight: bold;">Only one inbound rule exists by default: allow all traffic from other resources attached to this same security group.</mark>
Source is the security group's own ID, not a CIDR range.

Anything from outside — your laptop, the internet, another SG — is dropped.
Two EC2 instances sharing the default SG can freely talk to each other on any port; nothing from the internet gateway reaches either one.

### Default outbound: allow everything

<mark style="background: #FFF3A3A6; font-weight: bold;">Outbound has two default rules: allow all IPv4 (0.0.0.0/0) and all IPv6 (::/0) traffic, any port, any protocol.</mark>
Instance can freely reach the internet — package updates, API calls — with zero configuration.

This is why the common assumption "AWS blocks everything by default" is half-true: it's inbound-only.

### Blocked traffic times out, doesn't refuse

<mark style="background: #FFCCBCA6;">A security group drops disallowed packets silently — no SYN-ACK, no RST — so the client just waits until its own timeout fires.</mark>

`Connection refused` means the opposite: the SG *let the packet through*, but no process is listening on that port, so the OS sent back an RST.

Rule of thumb while debugging:
- **Timeout** → check the security group.
- **Refused** → check whether the service is running/listening.

### Not the same as statefulness

Security groups are also *stateful* — response traffic for an allowed request is let back in automatically, regardless of what the rules say.
That's a separate mechanism from these default rules: statefulness governs *replies to already-permitted traffic*; the defaults above govern *what gets permitted in the first place*.

### Read more
- [[AWS - MOC]]
