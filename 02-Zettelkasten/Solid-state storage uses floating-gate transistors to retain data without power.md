Solid-state storage (SSDs, USB drives, SD cards) uses floating-gate transistors to store data persistently—data remains even when power is removed.

A floating-gate transistor (also called a flash memory cell) has an extra gate terminal, electrically isolated within the transistor structure. Electrons trapped on this floating gate change the transistor's electrical properties, representing stored data.

Two main types of floating-gate storage:

SLC (Single-Level Cell): stores one bit per transistor
- Uses two voltage states (high and low)
- Fast, reliable, but low density and expensive per bit

MLC/TLC/QLC (Multi/Triple/Quad-Level Cell): stores multiple bits per transistor
- MLC: 2 bits per cell (4 voltage states)
- TLC: 3 bits per cell (8 voltage states)
- QLC: 4 bits per cell (16 voltage states)
- More bits per transistor increases density and reduces cost
- But distinguishing between many voltage levels becomes error-prone

Storage process (program):
- High voltage applied to write transistor forces electrons onto floating gate
- Electrons accumulate, changing transistor threshold voltage
- State persists indefinitely (decades) without power

Erasure process:
- Flash cells cannot be erased individually; entire blocks must be erased together
- Erase applies even higher voltage, forcing accumulated electrons off floating gate
- This block-level erase is a limitation that SSD controllers manage through complex algorithms

Wear problem:
- Each erase cycle stresses the insulating layer around the floating gate
- After 1,000-100,000 erase cycles (depending on cell type), cells become unreliable
- SSDs implement wear leveling: distributing writes across many cells to extend lifespan

Advantages of solid-state storage:
- Persistent: survives power loss
- No moving parts: faster than mechanical hard drives, more reliable
- High capacity: 1+ terabytes common

Disadvantages:
- Finite write cycles (wear)
- More expensive per gigabyte than hard drives
- Degradation over time (bit rot, electron leakage)

Links: [[Transistors are semiconductor devices that amplify or switch electronic signals]], [[Hard disk drives store data in rotating magnetic platters]]
