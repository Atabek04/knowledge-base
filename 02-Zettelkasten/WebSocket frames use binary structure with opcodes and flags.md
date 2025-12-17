---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket frames use binary structure with opcodes and flags

WebSocket frames use a **binary structure** with specific fields for metadata and payload.

## Frame structure (simplified)

```
Byte 0-1:  FIN + RSV + Opcode, MASK + Payload length
Byte 2-3:  Extended payload length (if needed)
Byte 4-7:  Masking key (if MASK=1)
Byte 8+:   Payload data
```

## Key fields

### FIN (Final) bit
- `1` = this is the final frame
- `0` = more fragments are coming

### Opcode (4 bits) — frame type

**Data frames:**
- `0x1` — UTF-8 text payload
- `0x2` — raw binary data (images, files)
- `0x0` — continuation of fragmented message

**Control frames:**
- `0x8` — initiate connection close
- `0x9` — ping (heartbeat check)
- `0xA` — pong (ping response)

### MASK bit
- `1` — payload is masked
- `0` — payload is not masked

### Payload length
- Length of message data
- Uses extended length field if > 125 bytes

---

## Links

- [[Frame is the basic unit of WebSocket communication]]
- [[Masking is XORing the payload]]
- [[Ping-Pong frames detect dead connections and prevent timeouts]]
- [[WebSocket frames are binary data chunks, not HTTP requests]]
- [[WebSocket MOC]]
