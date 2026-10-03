---
aliases: [data center, datacenter, ЦОД, центр обработки данных, DC]
---

Every server is a physical machine sitting somewhere, including the virtual one you rent from a cloud provider. The place it sits is a **data center**, and in Russian infrastructure talk the same thing is called a **ЦОД**.

---

### What a data center supplies

<mark style="background: #FFF3A3A6;">A data center is a building that houses racks of servers and supplies everything they need to run without stopping: power, cooling, network connectivity and physical security.</mark>

- **Power**: two independent feeds from the grid, batteries (UPS) that bridge the seconds of a cut, and diesel generators for longer outages.
- **Cooling**: servers turn almost all their electricity into heat, so air or liquid cooling runs around the clock.
- **Network**: connections to several upstream internet providers, so losing one link does not cut the building off.
- **Physical security**: guards, access cards, cameras. Whoever can touch the machine can read its disks.

A **rack** is the standard metal cabinet that servers are bolted into, stacked one above another. A data center is rows of racks.

#### The name ЦОД

ЦОД stands for *центр обработки данных*, literally a *data processing centre*: the centre where your data is *processed*. Russian documents and job ads use ЦОД where English uses data center or DC.

---

### Where a cloud VM physically runs

Renting a cloud server does not remove the data center; it moves it to the provider. AWS region `eu-central-1` is Frankfurt, and it is split into three **availability zones**, each one or more separate data centers with their own power and network ([AWS docs: Regions and Availability Zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html)).

![[cloud_region_to_server_nesting.svg|620]]

<mark style="background: #ABF7F7A6;">A cloud region is a group of data centers; the provider uses virtualization to slice their physical servers into the VMs it rents out.</mark> Your EC2 instance is a slice of one physical server, in one rack, in one building. The slicing itself is [[Virtualization solves hardware underutilization and application isolation problems|virtualization]].

<mark style="background: #FF5582A6;">"The cloud" does not mean hardware stops mattering: a fire or power loss in one data center takes down every VM inside it.</mark> On 10 March 2021 a fire destroyed OVHcloud's SBG2 data center in Strasbourg and part of the SBG1 building next to it, and customers whose only copy lived there lost their data ([DCD](https://www.datacenterdynamics.com/en/news/ovh-fire-update-four-halls-sbg1-destroyed-well-all-sbg2/), [Uptime Institute](https://journal.uptimeinstitute.com/learning-from-the-ovhcloud-data-center-fire/)). Splitting a region into separate data centers exists so that one building failing is a [[A fault is a component deviating from spec while a failure is the system no longer serving users|fault the system survives, not a failure]].

### Read more

- [[Virtualization solves hardware underutilization and application isolation problems]]
- [[A fault is a component deviating from spec while a failure is the system no longer serving users]]
- [[AWS - MOC]]
- [[DevOps - MOC]]
