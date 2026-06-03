> Cloud infrastructure for backend engineers — services, patterns, and system design context

---

## Resources

| Resource | Type | Focus |
|----------|------|-------|
| [donnemartin/awesome-aws](https://github.com/donnemartin/awesome-aws) | Curated list | Libraries, repos, guides, blogs |
| [iam-veeramalla/aws-devops-zero-to-hero](https://github.com/iam-veeramalla/aws-devops-zero-to-hero) | 30-day course | DevOps, projects, interview questions |
| [mikeroyal/AWS-Guide](https://github.com/mikeroyal/AWS-Guide) | Reference guide | Tools, services, certifications |
| [NotHarshhaa/AWS-Projects](https://github.com/NotHarshhaa/AWS-Projects) | Project-based | CI/CD, IaC, containers, serverless |

---

## Topics

### Compute

#### EC2 (Elastic Compute Cloud)
- [ ] Instance types — general purpose, compute/memory/storage optimized
- [ ] On-demand vs Reserved vs Spot pricing
- [ ] AMIs (Amazon Machine Images) — snapshots for replication
- [ ] Security groups — stateful firewall at instance level
- [ ] Auto Scaling Groups — horizontal scaling + health replacement

#### Lambda (Serverless)
- [ ] Event-driven execution — no server management
- [ ] Cold start problem and mitigation (provisioned concurrency)
- [ ] Execution limits — 15 min timeout, 10GB memory max
- [ ] Use cases: lightweight APIs, event processors, cron jobs
- [ ] Lambda + API Gateway = serverless REST API pattern

#### ECS / Fargate (Containers)
- [ ] ECS — container orchestration (AWS-managed alternative to K8s)
- [ ] Fargate — serverless container runtime (no EC2 management)
- [ ] Task definitions — container config (image, CPU, memory, env vars)
- [ ] Services — maintain N running tasks, integrate with ALB

---

### Networking

#### VPC (Virtual Private Cloud)
- [ ] Isolated network — subnets, route tables, internet gateways
- [ ] Public vs private subnets — what can reach the internet
- [ ] NAT Gateway — private subnet → internet (outbound only)
- [ ] VPC Peering / PrivateLink — connect VPCs or services privately
- [ ] Security groups (instance-level) vs NACLs (subnet-level)

#### Load Balancing
- [ ] **ALB** (Application Load Balancer) — HTTP/HTTPS, path/host routing, Layer 7
- [ ] **NLB** (Network Load Balancer) — TCP/UDP, ultra-low latency, Layer 4
- [ ] **CLB** (Classic) — legacy, avoid in new designs
- [ ] Target groups — route to EC2, ECS, Lambda, or IP
- [ ] Health checks + connection draining

#### Route 53
- [ ] DNS management + health checks
- [ ] Routing policies: simple, weighted, latency-based, failover, geolocation
- [ ] Used for multi-region active-active / active-passive failover

#### CloudFront (CDN)
- [ ] Edge caching — serve static assets from 400+ PoPs globally
- [ ] Origins: S3, ALB, EC2, custom HTTP
- [ ] Cache invalidation — `/*` invalidation costs money, design TTLs carefully
- [ ] Use with S3 for static site hosting or media delivery

---

### Storage

#### S3 (Simple Storage Service)
- [ ] Object storage — not a filesystem; objects are flat with keys
- [ ] Storage classes: Standard, Infrequent Access, Glacier (archive)
- [ ] Bucket policies + IAM for access control
- [ ] **Pre-signed URLs** — server issues time-limited URL → client uploads/downloads directly (no proxy through app server)
- [ ] Multipart upload — required for files >5GB, recommended >100MB
- [ ] Versioning + lifecycle policies
- [ ] Event notifications → Lambda / SQS / SNS on object create/delete
- [ ] Self-hosted alternatives: MinIO (S3-compatible), Garage (S3-compatible, investigate pre-signed URL parity)

#### EBS (Elastic Block Store)
- [ ] Block storage — attached to a single EC2 instance (like a disk)
- [ ] Types: gp3 (general), io2 (high IOPS), st1 (throughput HDD)
- [ ] Snapshots → S3 → cross-region copy

#### EFS (Elastic File System)
- [ ] Shared NFS — multiple EC2/ECS instances mount same filesystem
- [ ] Use when multiple services need to read/write the same files

---

### Databases

#### RDS (Relational Database Service)
- [ ] Managed PostgreSQL, MySQL, MariaDB, SQL Server, Oracle
- [ ] Multi-AZ deployment — synchronous standby replica for failover
- [ ] Read replicas — asynchronous, for read scaling
- [ ] Aurora — AWS-native MySQL/PostgreSQL compatible, faster replication, serverless option

#### DynamoDB
- [ ] Fully managed key-value + document store
- [ ] Partition key + optional sort key — design drives everything
- [ ] Hot partition problem — bad key → uneven load → throttling
- [ ] Global tables — multi-region active-active replication
- [ ] DynamoDB Streams — change capture → Lambda triggers
- [ ] On-demand vs provisioned capacity

#### ElastiCache
- [ ] Managed Redis or Memcached
- [ ] Redis: rich data structures, persistence, pub/sub, Lua scripting
- [ ] Memcached: simple, multi-threaded, no persistence
- [ ] Use for session storage, leaderboards, caching DB queries

---

### Messaging & Async

#### SQS (Simple Queue Service)
- [ ] Standard queues — at-least-once delivery, best-effort ordering
- [ ] FIFO queues — exactly-once, strict ordering, lower throughput
- [ ] Visibility timeout — message hidden while being processed; re-queued if not deleted
- [ ] Dead Letter Queue (DLQ) — failed messages after N retries
- [ ] Long polling — reduces empty receives and cost

#### SNS (Simple Notification Service)
- [ ] Pub/Sub — one message → fan out to multiple subscribers
- [ ] Subscribers: SQS, Lambda, HTTP, email, SMS
- [ ] SNS → SQS fan-out pattern — durable async broadcast

#### EventBridge
- [ ] Event bus — route events from AWS services or custom apps
- [ ] Rule-based routing by event pattern
- [ ] Replaces CloudWatch Events; more powerful filtering

#### Kinesis
- [ ] Real-time data streaming (like Kafka)
- [ ] Kinesis Data Streams — ordered, sharded, 1–7 day retention
- [ ] Kinesis Data Firehose — load streaming data to S3/Redshift/ES
- [ ] Use for: clickstreams, telemetry, real-time analytics

---

### Security & Identity

#### IAM (Identity and Access Management)
- [ ] Users, groups, roles, policies
- [ ] Principle of least privilege — grant only what's needed
- [ ] IAM roles for services — EC2/Lambda assume roles (no hardcoded keys)
- [ ] Policy types: identity-based, resource-based, permission boundaries
- [ ] STS (Security Token Service) — temporary credentials

#### KMS (Key Management Service)
- [ ] Managed encryption keys
- [ ] Envelope encryption — data encrypted with data key, data key encrypted with KMS key
- [ ] Integrate with S3, RDS, EBS, Secrets Manager

#### Secrets Manager
- [ ] Store and rotate DB credentials, API keys, tokens
- [ ] Automatic rotation via Lambda
- [ ] vs SSM Parameter Store — Secrets Manager has rotation + higher cost

---

### Observability

#### CloudWatch
- [ ] Metrics — all AWS services emit metrics automatically
- [ ] Logs — centralized log storage + query (CloudWatch Logs Insights)
- [ ] Alarms — trigger SNS/Auto Scaling on metric threshold
- [ ] Dashboards — visualize cross-service metrics

#### X-Ray
- [ ] Distributed tracing — trace requests across Lambda, ECS, API Gateway
- [ ] Service map — visualize service dependencies and latency

---

### Infrastructure as Code

#### CloudFormation
- [ ] AWS-native IaC — JSON/YAML templates
- [ ] Stacks + change sets + drift detection
- [ ] Limit: verbose, slow feedback loop

#### CDK (Cloud Development Kit)
- [ ] Define infrastructure in TypeScript/Python/Java/Go
- [ ] Compiles to CloudFormation under the hood
- [ ] Better abstractions, IDE support, type safety

#### Terraform (not AWS-native but standard)
- [ ] Provider-agnostic IaC — AWS + GCP + Azure in one codebase
- [ ] State management — remote state in S3 + DynamoDB locking
- [ ] See [[DevOps - MOC]] for Terraform-specific notes

---

### System Design Patterns on AWS

- [ ] Static site: S3 + CloudFront + Route 53
- [ ] Serverless API: API Gateway + Lambda + DynamoDB
- [ ] Containerized microservices: ALB + ECS Fargate + RDS + ElastiCache
- [ ] Async processing pipeline: SQS + Lambda / ECS workers
- [ ] Event-driven fan-out: SNS → SQS (multiple consumers)
- [ ] Media upload: Pre-signed S3 URL → upload → S3 event → SQS → transcoding worker
- [ ] Multi-region active-passive: Route 53 failover + RDS cross-region replica
- [ ] Multi-region active-active: Route 53 latency routing + DynamoDB Global Tables

---

## Related
- [[System Design - MOC]]
- [[DevOps - MOC]]
- [[Databases - MOC]]
- [[VMs & Containers MOC]]
- [[Observability - MOC]]
