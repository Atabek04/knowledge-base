Random Access Memory (RAM) stores data temporarily during computer operation using transistors and capacitors arranged in a grid structure.

Each bit in RAM is stored using a transistor-capacitor pair (in DRAM, the most common type):
- The capacitor holds the bit value: charged (1) or discharged (0)
- The transistor acts as a switch controlling access to the capacitor

Millions or billions of these transistor-capacitor pairs are arranged in a 2D array on a chip. To read or write a specific bit, the memory controller selects a row and column address, which activates the appropriate transistor and capacitor.

Key characteristics of RAM:
- Volatile: data is lost when power is removed (capacitors discharge)
- Fast: access times measured in nanoseconds
- Expensive per bit compared to disk storage
- Limited capacity: typically 4GB-128GB in consumer devices
- Dynamic: capacitors must be refreshed periodically (tens of milliseconds) to prevent charge leakage

SRAM (Static RAM) uses a different approach:
- Uses cross-coupled transistors (a latch) instead of capacitor-transistor pairs
- Faster than DRAM but requires more transistors per bit
- No refresh needed (truly static)
- Used for processor caches where speed matters most

RAM is read-write memory: data can be written (stored) and read (retrieved) equally quickly. This makes it ideal for a processor's working memory during program execution.

The processor continuously uses RAM as its workspace: loading instructions, storing variables, keeping results of intermediate calculations. Modern CPUs are bottlenecked by how fast they can access RAM—they execute instructions faster than RAM can supply them.

Links: [[Transistors are semiconductor devices that amplify or switch electronic signals]], [[Solid-state storage uses floating-gate transistors to retain data without power]]
