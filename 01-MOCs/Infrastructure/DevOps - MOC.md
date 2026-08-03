> Infrastructure and deployment skills

---

## Progress

- [ ] Git advanced
- [ ] Linux basics
- [ ] Docker & Docker Compose
- [ ] Kubernetes basics
- [ ] CI/CD (GitHub Actions)
- [ ] Helm charts

---

## Topics

### Git Advanced
- [ ] Branching strategies (GitFlow, trunk-based)
- [ ] Rebasing vs merging
- [ ] Interactive rebase
- [ ] Cherry-picking
- [ ] Stashing
- [ ] Git hooks
- [ ] Bisect for debugging
- [ ] Submodules
- [ ] .gitattributes and .gitignore patterns

### Linux Basics
- [ ] File system navigation
- [ ] File permissions (chmod, chown)
- [ ] Process management (ps, top, kill)
- [ ] Text processing (grep, sed, awk basics)
- [ ] Package management (apt, yum)
- [ ] Systemd services
- [ ] Environment variables
- [ ] SSH and key management
- [ ] Shell scripting basics

### Docker
- [ ] Dockerfile instructions
- [ ] Multi-stage builds
- [ ] Image optimization
- [ ] Docker networking
- [ ] Volumes and bind mounts
- [ ] Docker Compose
- [ ] Health checks
- [ ] Environment variables and secrets
- [ ] Docker best practices for Java

### Docker Compose
- [ ] Service definitions
- [ ] Networks and volumes
- [ ] Depends_on and healthchecks
- [ ] Override files
- [ ] Profiles
- [ ] Local development setup

### Kubernetes Basics
- [ ] Pods, Deployments, Services
- [ ] ConfigMaps and Secrets
- [ ] Namespaces
- [ ] Labels and selectors
- [ ] Resource limits
- [ ] Horizontal Pod Autoscaler (HPA)
- [[Kubernetes probes let the kubelet check container health the app reports|K8s probes — app reports health, kubelet calls it and reacts]]
- [[A failing liveness probe makes the kubelet restart the container|Liveness fail — kubelet restarts the container]]
- [[A failing readiness probe removes the pod from Service endpoints|Readiness fail — pod pulled from Service load balancer, no restart]]
- [[Liveness probes must stay shallow while readiness probes can check dependencies|Liveness shallow, readiness deep — depth follows the reaction]]
- [[Kubernetes probes run via httpGet, tcpSocket, exec, or gRPC|Probe mechanisms — httpGet for apps, tcp/exec for infra]]
- [[A startup probe delays liveness and readiness checks until a slow app finishes booting|Startup probe — guards slow boot from premature liveness restarts]]
- [[Spring Boot Actuator exposes ready-made liveness and readiness probe groups|Actuator probe groups — liveness/readiness wired for free]]
- [ ] Ingress
- [ ] kubectl commands
- [ ] Minikube / kind for local development

### Helm
- [ ] Chart structure
- [ ] Values files
- [ ] Templates
- [ ] Releases
- [ ] Helm repositories
- [ ] Upgrading and rollback

### CI/CD
- [[CI test pipeline splits unit and integration tests into parallel jobs to minimize feedback time|CI test pipeline — parallel unit + integration jobs cut feedback time]]
- [[Spring ApplicationContext cache determines how many times the JVM boots Spring during a test suite|Spring context cache — one JVM boot shared across all integration tests]]
- [[Testcontainers singleton pattern starts containers once per JVM by using a static initializer|Testcontainers singleton — static init starts containers once per JVM]]
- [ ] GitHub Actions workflows
- [ ] Build and test stages
- [ ] Docker image building
- [ ] Deployment automation
- [ ] Secrets management
- [ ] Branch protection and environments
- [ ] Artifact management

### Load Balancing
- [ ] NGINX basics
- [[Reverse proxy hides the origin server's IP by relaying client requests to backend servers|Reverse proxy — hides origin IP, caches, and shields the server]]
- [[Forward proxy hides the client's identity by relaying requests to the destination server|Forward proxy — hides the client's IP from the destination]]
- [[Firewall filters incoming connections by rule before they reach a server|Firewall — gatekeeper rule filter, not a proxy]]
- [[VPN encrypts and tunnels traffic through a forward proxy to hide the client's IP and location|VPN — encrypted, system-wide forward proxy]]
- [ ] Load balancing algorithms
- [ ] Health checks
- [ ] SSL termination

### Infrastructure as Code
- [ ] Terraform — providers, resources, state, modules
- [ ] Remote state (S3 + DynamoDB locking)
- [ ] CI/CD integration

### Deployment Strategies
- [ ] Blue-green deployment
- [ ] Canary deployment
- [ ] Rolling updates
- [ ] Feature flags (LaunchDarkly, Unleash)

---

## Russian Curriculum (Модуль 9)

### Инфраструктура
- [ ] Docker
- [ ] Kubernetes
- [ ] CI/CD пайплайны
- [ ] Infrastructure as Code
- [ ] Cloud платформы

---

## Project Tasks

**E-Commerce Stage 7, 13:**
- [ ] Create Dockerfile for application
- [ ] Set up Docker Compose for local development
- [ ] Create GitHub Actions workflow
- [ ] Write Kubernetes manifests
- [ ] Create Helm chart for deployment

---

## Related
- [[Architecture - MOC]]
- [[AWS - MOC]]
- [[Observability - MOC]]
