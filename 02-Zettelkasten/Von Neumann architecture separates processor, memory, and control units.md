The Von Neumann architecture, proposed by John Von Neumann in 1945, established the fundamental design for stored-program computers that remains dominant today.

Before Von Neumann, computers like ENIAC were programmed by physically rewiring circuits—reprogramming took days or weeks. Von Neumann proposed storing program instructions in memory alongside data, allowing rapid program changes.

Key components of Von Neumann architecture:

Memory:
- Stores both data and program instructions
- Instructions and data are indistinguishable from a storage perspective (they are both binary values)
- Processor fetches instructions from memory sequentially

Control Unit:
- Manages instruction fetching and sequencing
- Maintains program counter (address of next instruction)
- Decodes instructions into control signals for other components

Arithmetic Logic Unit (ALU):
- Performs arithmetic operations (addition, subtraction)
- Performs logical operations (AND, OR, NOT)
- Executes whatever computations the instruction specifies

Input/Output:
- Receives data into memory
- Outputs results from memory to external devices

The fetch-execute cycle:
- Fetch: retrieve instruction from memory at address pointed to by program counter
- Decode: interpret instruction to determine what operation to perform
- Execute: perform the operation (arithmetic, memory access, branching)
- Store: write results back to memory
- Increment program counter and repeat

Consequences of this architecture:
- Self-modifying code: programs can modify their own instructions (rarely useful, generally dangerous)
- Stored programs: programs are as portable as data—same program runs on any Von Neumann machine
- Sequential processing: instructions execute in order (though modern processors break this assumption through pipelining)

Modern processors preserve the Von Neumann model conceptually while optimizing its implementation:
- Instruction caches hold frequently accessed instructions
- Branch prediction attempts to fetch the next instruction before the branch is evaluated
- Pipelining allows multiple instructions to be processed simultaneously

The Von Neumann bottleneck: the bus connecting processor and memory becomes a limiting factor as the processor is capable of executing instructions faster than memory can supply them. Cache hierarchies partially address this problem.

Alternative architectures (Harvard architecture: separate instruction and data memory) exist but are less common in general-purpose computers.

Links: [[Alan Turing proved computability and programmability are universal principles]], [[Cache memory bridges the speed gap between fast processors and slow main memory]]
