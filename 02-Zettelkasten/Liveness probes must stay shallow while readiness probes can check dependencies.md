---
created: 2026-06-23
tags: [orchestration/kubernetes]
aliases: [shallow liveness deep readiness, probe depth]
---

Liveness and readiness probes use the *same* delivery [[Kubernetes probes run via httpGet, tcpSocket, exec, or gRPC|mechanisms]] — `httpGet`, `tcpSocket`, `exec`, `grpc`. So the real difference between them is **not how they are called**. It is <mark style="background: #FFF3A3A6;">what your code checks inside the endpoint</mark>.

The rule:

> **Liveness must be shallow. Readiness can be deep.**

```
/livez  → return 200 immediately. "Am I deadlocked?" Nothing external.
/readyz → ping DB pool, Redis, broker. Return 503 if any are down.
```

---

#### Why the asymmetry exists — it comes from the reactions

The two probes trigger opposite kubelet reactions, and that dictates what they may safely check:

- [[A failing liveness probe makes the kubelet restart the container|Liveness failure → restart]]. Restarting is destructive. If liveness checked the database and the DB blipped, every pod would restart in a loop — and restarting fixes nothing about a down database. So liveness must depend on **nothing external**.
- [[A failing readiness probe removes the pod from Service endpoints|Readiness failure → drain traffic]]. Pulling a pod out of rotation is cheap and reversible. So readiness is the *right* place to check dependencies: a struggling pod stops receiving traffic until its dependencies recover, then rejoins.

<mark style="background: #FF5582A6;">Putting a dependency check in liveness is the classic mistake</mark> — it converts a recoverable outage into a cluster-wide restart storm.

---

#### The official phrasing

The Kubernetes docs put it directly: a liveness probe that depends on external services could cause **cascading failures** across your system. The liveness probe passes when the app itself is healthy; the readiness probe additionally checks that each required back-end service is available.

---

### Read more
- [[A failing liveness probe makes the kubelet restart the container]]
- [[A failing readiness probe removes the pod from Service endpoints]]
- [[Kubernetes probes let the kubelet check container health the app reports]]
- [[Kubernetes probes run via httpGet, tcpSocket, exec, or gRPC]]
- [[Spring Boot Actuator exposes ready-made liveness and readiness probe groups]]
- [[DevOps - MOC]]
