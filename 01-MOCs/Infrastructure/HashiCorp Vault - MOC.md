---
created: 2026-10-09
tags: [moc]
aliases: [Vault MOC, HashiCorp Vault]
---

> Secrets management with HashiCorp Vault: from the Vault Associate 003 exam to running Vault in production

Vault stores, generates and revokes secrets behind one authenticated, audited API.

Part 1 (M1 to M9) is the Associate exam scope. Part 2 (M10 to M15) is production operations, the Operations Professional scope.

Teaching Progress: not started (next: M1).

---

## Certification

Both exams are booked through the [HashiCorp certification portal](https://developer.hashicorp.com/certifications/security-automation), online proctored. No prerequisites to register.

| Exam | Take it after | Format | Price | Valid |
|---|---|---|---|---|
| [Vault Associate (003)](https://developer.hashicorp.com/certifications/vault-associate) | M1 to M9 | 1 h, multiple choice | $70.50 | 2 years |
| [Vault Operations Professional](https://developer.hashicorp.com/certifications/security-automation) | M10 to M15 | 4 h, hands-on lab plus multiple choice | $295, one free retake | 2 years |

Prices exclude local taxes. Confirm price and exam version on the booking page before paying.

Free official prep: [Associate 003 learning path](https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-study-003) and [exam review](https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-review-003). The Professional exam tests Enterprise features; a free 30-day Vault Enterprise trial license covers the practice.

- [ ] Vault Associate (003)
- [ ] Vault Operations Professional

---

## M1. Introduction to Vault

- [ ] What Vault is and how it works
- [ ] Why organizations choose Vault: benefits and use cases
- [ ] Editions: Community, Enterprise, HCP; self-managed vs HashiCorp-managed
- [ ] How Vault improves security posture

## M2. Installing and running Vault

- [ ] Installing Vault: manual install, install with Packer
- [ ] Dev server
- [ ] Running a production server
- [ ] Environment variables: VAULT_ADDR, VAULT_TOKEN, VAULT_NAMESPACE
- [ ] Integrated Storage (Raft) backend
- [ ] Consul storage backend

## M3. Vault architecture

- [ ] Components, architecture and pathing structure
- [ ] Interfaces: CLI, UI, API
- [ ] Data protection: barrier, keyring, root key
- [ ] Seal and unseal: Shamir key shards, cloud KMS auto unseal, transit auto unseal
- [ ] Initialization
- [ ] Configuration file and storage backends
- [ ] Audit devices

## M4. Authentication methods

- [ ] What an auth method is and how to enable one
- [ ] Configuring auth methods via CLI, API, UI
- [ ] Authenticating via CLI, API (incl. API Explorer), UI
- [ ] Entities and identity groups
- [ ] Choosing an auth method: human vs machine auth
- [ ] AppRole, Userpass, Okta, Kubernetes

## M5. Policies

- [ ] Managing policies via CLI, UI, API
- [ ] Anatomy of a policy: path and capabilities
- [ ] Path customization: glob, segment wildcard, templated paths
- [ ] Implementing ACL policies

## M6. Tokens

- [ ] Token prefixes: hvs, hvb, hvr
- [ ] Token hierarchy and orphan tokens
- [ ] Lifecycle: TTL, max TTL, periodic tokens, use limits
- [ ] Service vs batch tokens
- [ ] Managing tokens via CLI, UI, API
- [ ] Root tokens and token accessors
- [ ] Choosing a token for a use case

## M7. Leases

- [ ] Lease ID and lease duration
- [ ] Renewing leases with an increment
- [ ] Revoking leases: single, prefix, force
- [ ] How lease TTL interacts with token TTL

## M8. Secrets engines

- [ ] Static vs dynamic secrets: the value of short-lived credentials
- [ ] Enabling, tuning, moving and disabling an engine
- [ ] Configuring an engine for dynamic credentials
- [ ] KV v1 and KV v2: versioning, metadata, soft delete, destroy
- [ ] Cubbyhole and response wrapping
- [ ] Transit: encrypt, decrypt, rewrap, key rotation, min decryption version
- [ ] AWS engine: IAM user and assumed role
- [ ] Database engine: dynamic credentials
- [ ] PKI engine and TOTP engine
- [ ] Identity secrets engine

## M9. Vault Agent and Vault Secrets Operator

- [ ] Vault Agent: auto-auth, token sink, templating
- [ ] VSO vs the Agent Injector
- [ ] Installing VSO: connectivity and authentication
- [ ] Syncing a secret; dynamic secrets and rotation with VSO

---

## M10. Secure setup and core operations

- [ ] Security hardening
- [ ] Secure initialization with PGP-encrypted unseal keys
- [ ] Regenerating a root token
- [ ] Rekeying and rotating the encryption key
- [ ] Auto unseal
- [ ] Integrated Storage and Raft snapshots

## M11. High availability

- [ ] Configuring an HA cluster
- [ ] Building a cluster: manually, with retry_join, with auto_join
- [ ] Performance standby nodes

## M12. Replication

- [ ] Replication architecture
- [ ] Disaster Recovery replication
- [ ] Promoting a secondary cluster
- [ ] Performance replication
- [ ] Paths filter
- [ ] Configuring replication via CLI and UI

## M13. Monitoring

- [ ] Telemetry
- [ ] Audit logs
- [ ] Operational logs

## M14. Enterprise access control and HSM

- [ ] Identity entities and groups, deep dive; advanced policies
- [ ] Sentinel policies: RGP and EGP
- [ ] Control groups
- [ ] Namespaces
- [ ] HSM auto unseal and seal wrapping

## M15. Vault on Kubernetes and app integration

- [ ] Secure introduction of Vault clients
- [ ] Running Vault in Kubernetes with the Helm chart
- [ ] Vault Agent revisited: auto-auth, token sink, templating
- [ ] Spring Cloud Vault: KV, dynamic DB credentials, lease renewal ([docs](https://docs.spring.io/spring-cloud-vault/reference/))
- [ ] Terraform Vault provider basics

---

## Practice labs

Do each lab after its module, on a local Community Vault (Docker or binary). Ent labs need Vault Enterprise: use the free 30-day trial license.

**M2 to M3: install and architecture**
- [ ] Run `vault server -dev`; set VAULT_ADDR and VAULT_TOKEN; check `vault status`
- [ ] Write a production `config.hcl` (raft storage, TLS listener, `api_addr`, `cluster_addr`); run it as a systemd service
- [ ] `vault operator init -key-shares=5 -key-threshold=3`; unseal with 3 keys; seal and unseal again
- [ ] Transit auto unseal: Vault A holds a transit key, Vault B uses `seal "transit"`; restart B and confirm it unseals itself
- [ ] Enable a file audit device; perform a read; find the HMAC'd entry in the log

**M4 to M6: auth, policies, tokens**
- [ ] Enable userpass and AppRole; log in with each via CLI, `curl` and UI
- [ ] AppRole flow: fetch role_id, generate a response-wrapped secret_id, unwrap, log in
- [ ] Create an entity with two aliases (userpass and AppRole) and put it in a group with a policy
- [ ] Write policies with `*`, `+` and `{{identity.entity.name}}` paths; prove allow and deny with `vault token capabilities`
- [ ] Create parent, child and orphan tokens; revoke the parent and see which survive
- [ ] Create periodic, use-limited and batch tokens; compare `vault token lookup` output and renewability
- [ ] Look up and revoke a token by its accessor only

**M7 to M8: leases and secrets engines**
- [ ] KV v2: write 3 versions, read version 1, soft delete, undelete, destroy, set `max_versions`
- [ ] Transit: create key, encrypt, decrypt, rotate, rewrap, set `min_decryption_version`
- [ ] Database engine on PostgreSQL in Docker: dynamic role with 5m TTL; renew the lease, revoke it, then `vault lease revoke -prefix`
- [ ] Static role on PostgreSQL with automatic password rotation
- [ ] PKI: root CA and intermediate CA; issue a cert for `app.local`; revoke it; read the CRL
- [ ] Response wrapping: wrap a KV secret with 60s TTL; unwrap once; try a second unwrap

**M9: Agent and VSO**
- [ ] Vault Agent with AppRole auto-auth, token sink and a template rendering `application.properties`
- [ ] On kind or minikube: Kubernetes auth and VSO syncing a KV secret and a dynamic DB secret into a K8s Secret

**M10 to M15: operations**
- [ ] Init with `-pgp-keys`; regenerate a root token; rekey to 7/4; `vault operator rotate`
- [ ] 3-node raft cluster with `retry_join`; kill the leader; watch election with `vault operator raft list-peers`
- [ ] Take and restore a raft snapshot
- [ ] Enable telemetry; scrape `/v1/sys/metrics` with Prometheus
- [ ] Ent: DR replication, then promote the DR secondary; performance replication with a paths filter
- [ ] Ent: namespaces with per-namespace admins; a Sentinel EGP; a control group
- [ ] Install Vault on Kubernetes with the Helm chart in HA raft mode

**Capstone**
- [ ] Spring Boot (Kotlin) service on Kubernetes using Spring Cloud Vault: Kubernetes auth, dynamic PostgreSQL credentials with lease renewal, transit encryption of one sensitive column, audit log enabled, all Vault config managed with the Terraform Vault provider

---

### Read more

- [[DevOps - MOC]]
- [[Security - MOC]]
- [[VMs & Containers MOC]]
