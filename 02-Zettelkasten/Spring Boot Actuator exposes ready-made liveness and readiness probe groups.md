---
created: 2026-06-23
tags: [orchestration/kubernetes, spring/actuator]
aliases: [actuator probes, actuator health groups]
---

You rarely have to hand-code `/livez` and `/readyz` for a Spring Boot service. **Spring Boot Actuator** ships ready-made [[Kubernetes probes let the kubelet check container health the app reports|probe]] endpoints, split into two health **groups** that map exactly onto Kubernetes' two probes:

```
/actuator/health/liveness   → is the application context running?
/actuator/health/readiness  → are the app's dependencies usable?
```

Wire them into the manifest directly:

```yaml
livenessProbe:
  httpGet:
    path: /actuator/health/liveness
    port: 8080
readinessProbe:
  httpGet:
    path: /actuator/health/readiness
    port: 8080
```

Enable with `management.endpoint.health.probes.enabled=true` (auto-enabled when Spring detects it's running in Kubernetes).

---

#### Why the grouping matters — it enforces the depth rule for you

Actuator wires the right indicators into each group automatically, honoring [[Liveness probes must stay shallow while readiness probes can check dependencies|shallow liveness, deep readiness]]:

- <mark style="background: #FFF3A3A6;">**Liveness group** stays shallow</mark> — it only reflects whether the Spring application context is live. No DataSource, no Redis.
- <mark style="background: #ADCCFFA6;">**Readiness group** is deep</mark> — it folds in your `DataSource`, Redis, Kafka, etc. health indicators.

So a database outage flips **readiness** to `DOWN` (pod drains traffic) without touching **liveness** (no restart) — <mark style="background: #FF5582A6; font-weight: bold;">exactly the split that avoids restart-loops</mark>, with no manual endpoint coding.

---

### Read more
- [[Liveness probes must stay shallow while readiness probes can check dependencies]]
- [[Kubernetes probes let the kubelet check container health the app reports]]
- [[A failing readiness probe removes the pod from Service endpoints]]
- [[DevOps - MOC]]
