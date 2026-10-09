---
created: 2026-10-09
tags: [moc]
aliases: [Kubernetes MOC, K8s MOC, Kubernetes]
---

> Container orchestration with Kubernetes: from the first Pod to CKAD, CKA and running clusters in production

Kubernetes keeps a cluster's actual state converging on the desired state you declare in YAML.

Part 1 (M1 to M9) is the core every exam shares. Part 2 (M10 to M13) completes the CKAD and CKA scope. Part 3 (M14 to M15) is CKS hardening and production operations.

Teaching Progress: not started (next: M1).

---

## Certification

All exams are booked through the Linux Foundation, online proctored. Each includes one retake and 12 months to schedule. No prerequisites, except that CKS needs a CKA passed at any time (it no longer has to be active).

| Exam | Take it after | Format | Price | Valid |
|---|---|---|---|---|
| [CKAD](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/) | M1 to M12 (M11 is not examined) | 2 h, hands-on at the command line, pass 66%, K8s v1.37 | $445 | 2 years |
| [CKA](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/) | M13 | 2 h, hands-on, pass 66%, K8s v1.35 | $445 | 2 years |
| [CKS](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/) | M14 | 2 h, 15 to 20 hands-on tasks, pass 67%, K8s v1.35 | $445 | 2 years |
| [KCNA](https://training.linuxfoundation.org/certification/kubernetes-cloud-native-associate/) (optional) | M9 | 90 min, multiple choice, pass 75% | $250 | 2 years |
| [KCSA](https://training.linuxfoundation.org/certification/kubernetes-and-cloud-native-security-associate-kcsa/) (optional) | M8 | 90 min, multiple choice, pass 75% | $250 | 2 years |

Recommended path: CKAD, then CKA, then CKS. The two associate exams add little for a working backend engineer.

CKA, CKAD and CKS each include two [killer.sh](https://killer.sh) simulator sessions (36 h access each, 17 graded questions, harder than the real exam). The "SINGLE" registrations exclude them. Activate session 1 two to three weeks before the exam and session 2 in the final week.

Since 2026-06 the CARE program renews your CKA when you pass or renew the CKS, even if the CKA has expired. Official domains and weights: [cncf/curriculum](https://github.com/cncf/curriculum). Prices exclude local taxes; confirm price and Kubernetes version on the booking page before paying.

- [ ] CKAD
- [ ] CKA
- [ ] CKS

---

## M1. Containers and cloud native foundations

- [[Namespaces isolate what container processes can see|Namespaces: limit what a container process can see]]
- [[Cgroups limit how many resources container processes can consume|Cgroups: cap how much a container process can consume]]
- [ ] Images, layers and the OCI image and runtime specs
- [ ] Container runtimes: containerd, CRI-O and the CRI; why Docker shim was removed
- [ ] Why orchestration: scheduling, self-healing, scaling, service discovery
- [ ] Desired state and the reconciliation loop
- [ ] YAML for manifests: maps, lists, multi-document files

## M2. Architecture, kubectl and local clusters

- [ ] Control plane: kube-apiserver, etcd, kube-scheduler, kube-controller-manager
- [ ] Node components: kubelet, kube-proxy, container runtime
- [ ] The API: groups, versions, resources, kinds; `kubectl api-resources`
- [ ] Imperative commands vs declarative `kubectl apply`; server-side apply
- [ ] kubectl fluency: `explain`, `--dry-run=client -o yaml`, output formats, contexts and namespaces
- [ ] Local clusters: kind for multi-node and exam-like kubeadm, minikube for addons, k3d for fast loops
- [ ] Managed clusters: EKS, GKE, AKS and what the provider runs for you

## M3. Core workloads

- [ ] Pods: spec, lifecycle phases, restart policy
- [ ] Multi-container Pods: init containers, native sidecars, ambassador and adapter patterns
- [ ] Labels, selectors and annotations
- [ ] Namespaces as a scope for names, policy and quota
- [ ] ReplicaSets and Deployments
- [ ] Rolling updates and rollbacks: maxSurge, maxUnavailable, revision history
- [ ] Blue/green and canary with plain Deployments and Services
- [ ] DaemonSets
- [ ] StatefulSets: stable identity, ordered rollout
- [ ] Jobs and CronJobs: completions, parallelism, backoffLimit
- [ ] Graceful shutdown: SIGTERM, preStop hooks, terminationGracePeriodSeconds
- [[Kubernetes probes let the kubelet check container health the app reports|Probes: the app reports health, the kubelet checks and reacts]]
    - [[A failing liveness probe makes the kubelet restart the container|Liveness failure: the kubelet restarts the container]]
    - [[A failing readiness probe removes the pod from Service endpoints|Readiness failure: Pod leaves Service endpoints, no restart]]
    - [[A startup probe delays liveness and readiness checks until a slow app finishes booting|Startup probe: shields a slow boot from liveness restarts]]
    - [[Liveness probes must stay shallow while readiness probes can check dependencies|Probe depth: liveness shallow, readiness may check dependencies]]
    - [[Kubernetes probes run via httpGet, tcpSocket, exec, or gRPC|Probe mechanisms: httpGet for apps, tcp or exec for infra]]
    - [[Spring Boot Actuator exposes ready-made liveness and readiness probe groups|Actuator probe groups: liveness and readiness wired for free]]

## M4. Services and networking

- [ ] The networking model: every Pod gets an IP, no NAT between Pods
- [ ] CNI plugins: Cilium, Calico, Flannel
- [ ] Services: ClusterIP, NodePort, LoadBalancer, ExternalName, headless
- [ ] Endpoints and EndpointSlices
- [ ] kube-proxy modes: iptables, IPVS, eBPF replacement
- [ ] CoreDNS and service discovery; ndots and search domains
- [ ] Gateway API: GatewayClass, Gateway, HTTPRoute, GRPCRoute
- [ ] Ingress resources and controllers; ingress-nginx retired in March 2026, migrate with ingress2gateway
- [ ] NetworkPolicies: default deny for ingress and egress, allow DNS explicitly
- [ ] Why a NetworkPolicy does nothing without a CNI that enforces it

## M5. Storage

- [ ] Ephemeral volumes: emptyDir, configMap, secret, projected, downwardAPI
- [ ] hostPath and why it is a security risk
- [ ] PersistentVolumes and PersistentVolumeClaims
- [ ] Access modes and reclaim policies
- [ ] StorageClasses and dynamic provisioning; volumeBindingMode
- [ ] CSI drivers, volume expansion and snapshots
- [ ] StatefulSet volumeClaimTemplates

## M6. Configuration and secrets

- [ ] ConfigMaps: literal, file and env-file sources
- [ ] Secrets: types, base64 is not encryption
- [ ] Consuming config: env, envFrom, volume mounts; which ones update live
- [ ] Immutable ConfigMaps and Secrets
- [ ] Commands and args vs ENTRYPOINT and CMD
- [ ] Encryption at rest with EncryptionConfiguration
- [ ] Spring Boot externalized config from ConfigMaps and Secrets

## M7. Resources, scheduling and autoscaling

- [ ] Requests drive scheduling, limits drive CPU throttling and OOMKill
- [ ] QoS classes: Guaranteed, Burstable, BestEffort; eviction order
- [ ] LimitRange and ResourceQuota per namespace
- [ ] nodeName, nodeSelector, node affinity
- [ ] Pod affinity and anti-affinity
- [ ] Taints and tolerations
- [ ] Topology spread constraints
- [ ] PriorityClasses and preemption
- [ ] Node-pressure eviction and API-initiated eviction
- [ ] Static Pods; multiple schedulers and scheduler profiles
- [ ] HorizontalPodAutoscaler with metrics-server
- [ ] VerticalPodAutoscaler and in-place Pod resize (GA in 1.35)
- [ ] PodDisruptionBudgets: protect against voluntary disruption only
- [ ] JVM sizing in containers: heap vs memory limit, container-aware flags

## M8. Security

- [ ] The 4Cs: cloud, cluster, container, code
- [ ] Authentication: users, certificates, tokens, OIDC
- [ ] kubeconfig: clusters, users, contexts
- [ ] TLS in Kubernetes and the Certificates API
- [ ] Authorization: RBAC Roles, ClusterRoles and bindings
- [ ] ServiceAccounts, projected tokens, automountServiceAccountToken
- [ ] `kubectl auth can-i` and impersonation
- [ ] Admission control: mutating and validating webhooks
- [ ] ValidatingAdmissionPolicy with CEL
- [ ] Pod Security Standards and Pod Security Admission labels
- [ ] securityContext: runAsNonRoot, readOnlyRootFilesystem, capabilities, allowPrivilegeEscalation
- [ ] API deprecations and version migration

## M9. Observability and troubleshooting

- [ ] Container logs: `kubectl logs`, previous container, multi-container
- [ ] Events and why they expire
- [ ] `kubectl describe`, `kubectl debug` and ephemeral containers
- [ ] `kubectl top` and metrics-server vs kube-state-metrics
- [ ] JSONPath and custom-columns output
- [ ] Troubleshooting applications: CrashLoopBackOff, ImagePullBackOff, Pending
- [ ] Troubleshooting Services and networking: selectors, endpoints, DNS
- [ ] Troubleshooting nodes and the control plane: kubelet logs, static Pod manifests, crictl

---

## M10. Helm and Kustomize

- [ ] Helm chart structure: Chart.yaml, values.yaml, templates
- [ ] Templates: values, helpers, conditionals, ranges
- [ ] Releases: install, upgrade, rollback, history
- [ ] Repositories and OCI registries
- [ ] Chart dependencies and hooks
- [ ] Kustomize: bases, overlays, patches, generators, components
- [ ] Choosing Helm vs Kustomize, and Helm plus Kustomize post-rendering

## M11. GitOps and delivery

- [[Immutable artifact promotion promotes the same build through environments without rebuilding|Immutable promotion: one build moves through every environment]]
- [ ] CI pipeline into the cluster: build, scan, push, update manifests
- [ ] GitOps principles: Git as source of truth, pull-based reconciliation
- [ ] Argo CD: Applications, ApplicationSets, app-of-apps, sync waves
- [ ] Flux: GitRepository, Kustomization, HelmRelease
- [ ] Progressive delivery: Argo Rollouts or Flagger canaries
- [ ] Secrets in GitOps: External Secrets Operator, Vault Secrets Operator, Vault Agent Injector, Sealed Secrets

## M12. CRDs and operators

- [ ] CustomResourceDefinitions: schema, versions, status subresource
- [ ] Controllers and the reconcile loop
- [ ] Owner references, finalizers and garbage collection
- [ ] The operator pattern; installing and configuring an operator
- [ ] Building an operator with kubebuilder or Operator SDK

## M13. Cluster administration

- [ ] Preparing nodes: container runtime, kernel modules, swap, sysctl
- [ ] Installing a cluster with kubeadm; joining workers
- [ ] Extension interfaces: CNI, CSI, CRI
- [ ] Highly available control plane: stacked vs external etcd
- [ ] Upgrading with kubeadm: one minor version at a time, drain, uncordon
- [ ] etcd backup and restore with etcdctl and etcdutl
- [ ] Certificate expiry and renewal with `kubeadm certs`
- [ ] Node maintenance: cordon, drain, uncordon
- [ ] Installing cluster components with Helm and Kustomize
- [ ] Kubernetes the Hard Way: PKI, etcd and the control plane by hand

---

## M14. Security hardening

- [ ] CIS benchmark with kube-bench
- [ ] Protecting node metadata and kubelet endpoints
- [ ] Restricting API access and minimizing RBAC exposure
- [ ] Host hardening: minimal OS, AppArmor, seccomp profiles
- [ ] Sandboxed runtimes: gVisor, Kata Containers
- [ ] Pod-to-Pod encryption with Cilium or Istio mTLS
- [ ] Policy engines: Kyverno vs OPA Gatekeeper
- [ ] Supply chain: minimal base images, SBOMs, Trivy scanning, cosign signing, allowed registries
- [ ] Static analysis of manifests: KubeLinter, Kubesec
- [ ] Audit logging policy and log backends
- [ ] Runtime detection with Falco or Tetragon; immutable containers
- [ ] Attack scenarios with Kubernetes Goat

## M15. Production operations

- [ ] Monitoring stack: kube-prometheus, ServiceMonitor, alerting rules
- [ ] OpenTelemetry Operator: collectors and Java auto-instrumentation
- [ ] Event-driven scaling with KEDA
- [ ] Node scaling: Cluster Autoscaler vs Karpenter
- [ ] Multi-tenancy: namespaces, quotas and policy; vcluster and Capsule
- [ ] Service mesh: Istio ambient, Linkerd, and when not to adopt one
- [ ] Cost: requests drive node count, OpenCost allocation, right-sizing
- [ ] Production readiness checklist ([learnkube](https://learnkube.com/production-best-practices))
- [ ] Learning from failure stories ([k8s.af](https://k8s.af))
- [ ] Disaster recovery: Velero backups, multi-cluster

---

## Practice labs

Do each group after its modules. Default cluster: kind with a multi-node config, [cloud-provider-kind](https://github.com/kubernetes-sigs/cloud-provider-kind) for LoadBalancer and Gateway API, Cilium as CNI. Exam drills: [CKAD-exercises](https://github.com/dgkanatsios/CKAD-exercises), [cka-crash-course](https://github.com/bmuschko/cka-crash-course), [Killercoda CKA](https://killercoda.com/cka).

**M1 to M2: foundations and cluster**
- [ ] Run a container with `unshare` and a cgroup memory limit, no Docker; watch it get OOM-killed
- [ ] Create a kind cluster with 1 control plane and 2 workers from a config file
- [ ] Find every control plane component as a static Pod; read its manifest under `/etc/kubernetes/manifests`
- [ ] Generate a Deployment manifest with `--dry-run=client -o yaml`, edit it, apply it, then delete it declaratively

**M3: workloads**
- [ ] Deployment with 4 replicas; roll out a new image with maxUnavailable 0; roll back with `kubectl rollout undo`
- [ ] Pod with an init container that waits for a Service, plus a native sidecar that tails a log file
- [ ] Liveness, readiness and startup probes on a slow-booting app; break each and watch the different reaction
- [ ] CronJob every minute with `concurrencyPolicy: Forbid`; inspect the Jobs it leaves behind
- [ ] StatefulSet of 3; delete Pod 1 and confirm it returns with the same name

**M4 to M6: networking, storage, config**
- [ ] Expose one Deployment as ClusterIP, NodePort and LoadBalancer; reach each from the right place
- [ ] Resolve a Service by short name, namespaced name and FQDN from a debug Pod
- [ ] Gateway with two HTTPRoutes splitting traffic 90/10 between two versions
- [ ] Default-deny NetworkPolicy in a namespace; allow DNS egress and one frontend-to-backend path only
- [ ] PVC with the default StorageClass; write a file, delete the Pod, confirm the data survives
- [ ] Mount a ConfigMap as env and as a volume; change it and see which one updates without a restart
- [ ] Enable encryption at rest; prove with etcdctl that a new Secret is stored encrypted

**M7 to M9: scheduling, security, troubleshooting**
- [ ] Taint a worker; schedule one Pod onto it with a toleration and node affinity
- [ ] Spread 6 replicas evenly with topologySpreadConstraints
- [ ] Create one Pod per QoS class; find the class with `kubectl get pod -o jsonpath`
- [ ] HPA on CPU at 50%; load it with a busybox loop; watch scale-out and scale-in
- [ ] PDB with minAvailable 2; try to drain a node and watch the eviction wait
- [ ] User certificate via the Certificates API; Role allowing only Pod reads; verify with `kubectl auth can-i --as`
- [ ] Label a namespace `enforce=restricted`; fix a Pod until it is admitted
- [ ] Fix three broken scenarios: wrong image tag, Service selector mismatch, kubelet stopped on a node

**M10 to M12: packaging, GitOps, operators**
- [ ] `helm create` a chart; template probes, resources and replicas from values; upgrade and roll back
- [ ] Kustomize base with dev and prod overlays differing in replicas, image tag and a ConfigMap
- [ ] Install Argo CD; deploy an app from a Git repo; change Git and watch it sync; break drift and watch self-heal
- [ ] Write a CRD with an OpenAPI schema; create an instance; prove an invalid one is rejected
- [ ] Install an operator (e.g. CloudNativePG) and create a PostgreSQL cluster from its custom resource
- [ ] Follow the kubebuilder CronJob tutorial to a working controller

**M13: cluster administration** (kubeadm on 3 VMs, or the Killercoda playground)
- [ ] Install a cluster with kubeadm and Cilium; join two workers
- [ ] Upgrade it one minor version: control plane first, then each worker with drain and uncordon
- [ ] Back up etcd, delete a Deployment, restore the snapshot, confirm the Deployment is back
- [ ] Check and renew certificates with `kubeadm certs`
- [ ] Complete Kubernetes the Hard Way once

**M14 to M15: hardening and production**
- [ ] Run kube-bench and fix two failed checks
- [ ] Scan an image with Trivy; sign it with cosign; enforce signatures with Kyverno verifyImages
- [ ] Apply a seccomp RuntimeDefault profile and an AppArmor profile to a Pod
- [ ] Write an audit policy that logs Secret access at Metadata level; find the entries
- [ ] Work through five Kubernetes Goat scenarios
- [ ] Install kube-prometheus-stack; add a ServiceMonitor for an app; write one alert
- [ ] KEDA ScaledObject scaling a consumer from queue depth, down to zero

**Capstone**
- [ ] Spring Boot (Kotlin) service on kind: Helm chart with liveness, readiness and startup probes on Actuator groups; HPA on CPU; PDB and topology spread; config from a ConfigMap; database credentials from Vault through the Vault Secrets Operator with rollout restart on rotation; default-deny NetworkPolicy; Gateway API route; deployed and promoted between dev and prod overlays by Argo CD; metrics scraped by Prometheus

---

### Read more

- [[DevOps - MOC]]
- [[VMs & Containers MOC]]
- [[HashiCorp Vault - MOC]]
- [[Observability - MOC]]
