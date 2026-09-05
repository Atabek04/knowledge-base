---
created: 2026-06-23
tags: [orchestration/kubernetes]
aliases: [liveness probe, livez]
---

A **liveness probe** answers one question: <mark style="background: #FFF3A3A6;">is the process alive, or has it wedged into a state it can never recover from?</mark> It is the kubelet's tool for self-healing a stuck container.

When a liveness probe fails enough times in a row, the [[Kubernetes probes let the kubelet check container health the app reports|kubelet]] **kills and restarts the container** — on the bet that a fresh start clears the deadlock.

The name is the mnemonic: it checks that the app is still *living*, not that it is useful. A deadlocked or infinite-looping process is "running" to the OS but dead to its users; liveness catches exactly that.

---

#### What a liveness endpoint should return

```
GET /livez → return 200 immediately
```

It answers only "am I deadlocked?" — nothing external. A trivial handler that returns `200 OK` is often the *right* liveness probe.

---

#### The restart-loop trap

Because failure means **restart**, a liveness probe that checks an external dependency is dangerous. If `/livez` pings the database and the DB has an outage, every pod fails liveness, every pod restarts, and you get a cluster-wide <mark style="background: #FF5582A6;">restart loop</mark> — restarting your app does nothing to fix a down database.

This is why liveness must stay shallow. The full rule lives in [[Liveness probes must stay shallow while readiness probes can check dependencies|the shallow-vs-deep distinction]].

---

### Read more
- [[Kubernetes probes let the kubelet check container health the app reports]]
- [[Liveness probes must stay shallow while readiness probes can check dependencies]]
- [[A failing readiness probe removes the pod from Service endpoints]]
- [[Kubernetes probes run via httpGet, tcpSocket, exec, or gRPC]]
- [[DevOps - MOC]]
