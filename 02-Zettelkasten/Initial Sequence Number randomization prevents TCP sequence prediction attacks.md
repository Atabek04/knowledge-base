---
created: 2025-12-08
tags: [networking/tcp, networking/security]
sr-due:
sr-interval:
sr-ease:
---

# Initial Sequence Number randomization prevents TCP sequence prediction attacks

The Initial Sequence Number (ISN) is not always 0 or 1. Instead, TCP chooses a random ISN for each connection.

This randomness prevents **sequence prediction attacks** where an attacker might guess the next sequence number and inject forged data into an active connection.

If ISNs were predictable (e.g., always starting at 0, or incrementing linearly), an attacker could:
- Observe a connection starting with ISN=1000
- Predict the next connection would start at 1100
- Forge packets claiming to be from that predicted ISN

With random ISNs, prediction becomes extremely difficult. Each connection uses an unpredictable starting point.

The randomness is a security feature that makes TCP connections resistant to sequence number-based hijacking attacks.

## Links

- [[TCP sequence numbers track individual bytes for ordering and completeness]]
- [[SYN synchronizes Initial Sequence Numbers between hosts]]
- [[TCP MOC]]
