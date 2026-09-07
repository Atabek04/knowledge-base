---
created: 2026-06-23
tags: [orchestration/kubernetes]
aliases: [probe mechanisms, httpGet tcpSocket exec grpc]
---

Every [[Kubernetes probes let the kubelet check container health the app reports|Kubernetes probe]] — liveness, readiness, or startup — is delivered by one of **four mechanisms**. The probe *kind* decides what the kubelet does with the result; the *mechanism* decides how the kubelet asks. They are independent: any kind can use any mechanism.

| Mechanism | How the kubelet checks | Success means | Typical use |
|-----------|------------------------|---------------|-------------|
| **`httpGet`** | Sends an HTTP GET to a path + port | status code `2xx`/`3xx` | apps with a health endpoint (Spring Boot, Node) |
| **`tcpSocket`** | Opens a TCP connection to a port | port accepts the connection | databases, brokers with no HTTP |
| **`exec`** | Runs a command **inside** the container | exit code `0` | CLI-based health checks |
| **`grpc`** | Calls the standard gRPC health-checking service | service reports `SERVING` | gRPC services |

---

#### Why infra pods use `tcpSocket` or `exec`, not `httpGet`

<mark style="background: #FFF3A3A6;">Stateful infrastructure usually speaks no HTTP health protocol</mark>, so it cannot answer an `httpGet`. It is probed by opening its port or by running its own CLI tool:

```yaml
# Postgres — readiness via its CLI
exec:
  command: ["pg_isready", "-U", "postgres"]
```

```
Redis → redis-cli ping   (expects PONG)
Kafka → tcpSocket on the broker port, or a broker-API check script
```

So the split in practice:

- <mark style="background: #ADCCFFA6;">Your apps</mark> (Spring Boot, etc.) → `httpGet` against a real health endpoint.
- <mark style="background: #ADCCFFA6;">Stateful infra</mark> (DB, broker, cache) → `tcpSocket` or `exec`, because they don't speak HTTP health.

---

### Read more
- [[Kubernetes probes let the kubelet check container health the app reports]]
- [[Liveness probes must stay shallow while readiness probes can check dependencies]]
- [[A failing liveness probe makes the kubelet restart the container]]
- [[A failing readiness probe removes the pod from Service endpoints]]
- [[DevOps - MOC]]
