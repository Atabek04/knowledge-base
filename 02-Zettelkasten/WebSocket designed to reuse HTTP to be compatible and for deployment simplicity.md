---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket designed to reuse HTTP to be compatible and for deployment simplicity

WebSocket was designed to use **HTTP upgrade on ports 80/443** for **compatibility and deployment simplicity**.

## Problems if WebSocket required new ports

If WebSocket used a different port (e.g., 9000):
- Every **firewall admin** would need to reconfigure
- Every **proxy** would need updates
- Many **corporate networks** would never allow it
- WebSocket **adoption** would be severely limited

## The benefit of HTTP reuse

By piggybacking on existing HTTP infrastructure, WebSocket works **out of the box** in most network environments without requiring:
- Firewall rule changes
- Proxy updates
- New port allocations
- Special network configurations

This design decision prioritized **real-world deployability** over protocol purity.

---

## Links

- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[WebSocket can't start directly without HTTP upgrade]]
- [[Designing WebSocket with its own port creates massive problems]]
- [[WebSocket MOC]]
