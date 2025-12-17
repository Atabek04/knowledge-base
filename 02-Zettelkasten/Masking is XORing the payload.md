---
created: 2025-12-17
tags: [networking/websocket, networking/security]
sr-due:
sr-interval:
sr-ease:
---

# Masking is XORing the payload

**Masking** is the process of **XORing payload data with a random 32-bit key** before transmission to provide basic obfuscation.

## Masking process

**Sender (client):**
1. Generate a random 32-bit **masking key** (4 bytes)
2. **XOR each payload byte** with `key[i % 4]` (cycling through the 4 key bytes)
3. Send the **key + masked payload** in the frame

**Receiver (server):**
1. Read the masking key from the frame
2. **XOR the masked payload** with the same key
3. Recover the original data (XOR is reversible)

## Masking requirements

**Client → Server frames:** **MUST be masked**
- Protects against cache poisoning attacks

**Server → Client frames:** **MUST NOT be masked**
- Servers don't mask to save bandwidth and processing

---

## Links

- [[WebSocket frames use binary structure with opcodes and flags]]
- [[WebSocket MOC]]
