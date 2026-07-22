---
created: 2026-06-23
tags: [orchestration/kubernetes]
aliases: [readiness probe, readyz]
---

A **readiness probe** answers a different question from liveness: not "is it alive?" but <mark style="background: #FFF3A3A6; font-weight: bold;">"can it actually serve traffic right now?"</mark> An app can be perfectly alive yet not ready — still warming a cache, still opening its connection pool, or temporarily cut off from a dependency.

When a readiness probe fails, the [[Kubernetes probes let the kubelet check container health the app reports|kubelet]] does **not** restart the container. Instead it <mark style="background: #ADCCFFA6; font-weight: bold;">removes the pod from the Service's endpoints</mark>, so the Service load balancer stops routing requests to it. The pod keeps running; it just receives no traffic until it reports ready again.

A Kubernetes **Service** load-balances across the set of healthy pod IPs (its *endpoints*); readiness is what decides membership in that set.

---

#### Why "remove, don't restart" is the right reaction

Readiness failures are usually *temporary and recoverable* — a dependency blip, a cache rebuild after deploy. Restarting wouldn't help and would throw away warm state. Pulling the pod out of rotation drains traffic to the healthy pods and lets this one recover quietly, then rejoin.

---

#### What a readiness endpoint should check

```
GET /readyz → 200 only if DB pool, Redis, broker are reachable; else 503
```

Unlike liveness, readiness is the *right* place to check dependencies — failing it has no destructive consequence. The reasoning is in [[Liveness probes must stay shallow while readiness probes can check dependencies|the shallow-vs-deep distinction]].

---

### Read more
- [[Kubernetes probes let the kubelet check container health the app reports]]
- [[Liveness probes must stay shallow while readiness probes can check dependencies]]
- [[A failing liveness probe makes the kubelet restart the container]]
- [[A startup probe delays liveness and readiness checks until a slow app finishes booting]]
- [[DevOps - MOC]]
