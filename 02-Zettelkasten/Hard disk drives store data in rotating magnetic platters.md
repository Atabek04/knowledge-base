Hard disk drives (HDDs) store data by magnetizing tiny areas on rotating metal platters, persisting indefinitely without power due to permanent magnetic properties.

Each platter is coated with a ferromagnetic material (typically iron oxide). Data is written by passing current through a write head (electromagnet), which magnetizes small regions to represent 1s and 0s.

Reading reverses the process: a read head detects the magnetic field of each magnetized region, recovering stored bits.

Physical organization:
- Tracks: concentric circles on the platter surface
- Sectors: pie-shaped divisions of tracks, typically 512 bytes or 4,096 bytes each
- Cylinders: vertically aligned tracks across multiple platters
- Seek time: delay as read/write head moves to the correct track (milliseconds)

Key characteristics:
- Persistent: data survives power loss indefinitely
- Large capacity: 1+ terabytes economical
- Cheap per gigabyte compared to SSDs or RAM
- Slow: mechanical moving parts mean access times in milliseconds (million times slower than RAM)
- No wear limit: magnetic media can be rewritten indefinitely (unlike flash memory)
- Fragmentation problem: if files are scattered across non-contiguous sectors, seek times accumulate

Speed bottleneck:
- Platter rotation speed: typically 5,400-7,200 rpm (consumer) or 10,000-15,000 rpm (enterprise)
- Average latency: ~4-8ms for random access (waiting for platter to rotate into position)
- Sequential access: significantly faster since head doesn't need to move between adjacent sectors

Why HDDs persist despite SSD availability:
- Cost: $0.02-0.05 per gigabyte vs. $0.08-0.20 for SSDs
- Endurance: no wear limit (data centers may run drives for 6-8 years continuously)
- Reliability: data loss from magnetic field degradation is slower than bit rot in flash memory

Modern systems combine both: fast SSDs for OS and active programs, large HDDs for archival storage.

Links: [[Solid-state storage uses floating-gate transistors to retain data without power]], [[RAM stores data in volatile memory using transistors and capacitors]]
