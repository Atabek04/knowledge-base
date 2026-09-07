---
created: 2026-06-23
tags: [orchestration/kubernetes]
aliases: [probes, health probe, kubelet probe]
---

Kubernetes does not magically know whether your container is healthy. Health is something your **application** must report, and the **kubelet** (the node agent running on every worker) is the one that periodically asks.

This split is the whole mental model: <mark style="background: #FFF3A3A6;">the app owns the health logic, the kubelet only calls it and reacts to the answer.</mark>

A **probe** is a diagnostic the kubelet runs against a container on a schedule. The container exposes an endpoint or command; the kubelet hits it and reads success/failure.

---

### The three probe kinds

Kubernetes defines three probes, each answering a different question:

| Probe | Question | kubelet reaction on failure |
|-------|----------|------------------------------|
| **Liveness** | "Is the process alive, or wedged?" | [[A failing liveness probe makes the kubelet restart the container\|restart the container]] |
| **Readiness** | "Can it serve traffic right now?" | [[A failing readiness probe removes the pod from Service endpoints\|pull it out of the Service load balancer]] |
| **Startup** | "Has it finished booting yet?" | [[A startup probe delays liveness and readiness checks until a slow app finishes booting\|hold off the other two probes]] |

The probes share the *same* delivery [[Kubernetes probes run via httpGet, tcpSocket, exec, or gRPC|mechanisms]] — what differs is the kubelet's reaction and what your code should check inside.

---

### Convention: expose HTTP health endpoints

For normal apps, teams expose HTTP endpoints the kubelet calls:

```
GET /livez   → 200 if the process is alive
GET /readyz  → 200 only if the app can actually serve traffic
```

(`/healthz` is the older name; `/livez` and `/readyz` are the modern convention.)

<mark style="background: #ADCCFFA6;">Infrastructure pods (Postgres, Kafka, Redis) usually have no HTTP health endpoint</mark> — they are probed by TCP or by running a CLI command instead. See the [[Kubernetes probes run via httpGet, tcpSocket, exec, or gRPC|probe mechanisms]] note for which fits what.

---

### Read more
- [[A failing liveness probe makes the kubelet restart the container]]
- [[A failing readiness probe removes the pod from Service endpoints]]
- [[Liveness probes must stay shallow while readiness probes can check dependencies]]
- [[Kubernetes probes run via httpGet, tcpSocket, exec, or gRPC]]
- [[A startup probe delays liveness and readiness checks until a slow app finishes booting]]
- [[Spring Boot Actuator exposes ready-made liveness and readiness probe groups]]
- [[DevOps - MOC]]
