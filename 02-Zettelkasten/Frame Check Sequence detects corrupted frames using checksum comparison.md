---
created: 2025-12-15
tags: [networking/datalink]
sr-due:
sr-interval:
sr-ease:
---

# Frame Check Sequence detects corrupted frames using checksum comparison

FCS is the trailer portion of a Data Link frame.

**Sender side:**
1. Calculate checksum of entire frame (header + data)
2. Append checksum as FCS in trailer
3. Send frame

**Receiver side:**
1. Recalculate checksum of received frame
2. Compare with FCS value
3. Match → frame is valid
4. Mismatch → frame is corrupted, discard it

FCS catches transmission errors but doesn't correct them — corrupted frames are simply dropped.

## Links
- [[Data Link Layer encapsulates packets into frames with MAC headers]]
- [[Networking MOC]]
