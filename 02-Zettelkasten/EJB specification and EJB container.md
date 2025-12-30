## EJB Specification

EJB (Enterprise JavaBeans) is a specification.
Specification defines interfaces and contracts.

It's created by Sun Microsystems in 1997.
It defines how to build server-side components for enterprise apps.

Companies like IBM, Oracle, RedHat read the spec and build their own implementations.

You add the **EJB API**, write your code against those interfaces, then deploy to a container.

You write simple Java classes focused on business logic.
EJB container (part of the application server)
It automatically provides enterprise services:
- transactions
- security
- concurrency

---

## EJB Container

EJB container is the **runtime environment** inside the app server (like WebLogic, WebSphere, or JBoss)
	It manages the EJB components
It's like a **smart wrapper** around the code.

#### Functions

When you deploy your EJB, the container:
- Intercepts all calls to your business methods
- Start/commits transactions automatically
- Check security permissions
- Manages object lifecycle
- Handle threading and concurrency

> You focus on writing business logic, the container handles infrastructure.
