A logic gate is the basic building block of digital circuits—a simple circuit that implements a Boolean operation and outputs a result based on its inputs.

The fundamental logic gates are:
- NOT gate: one input, outputs the opposite value
- AND gate: two inputs, outputs 1 only if both are 1
- OR gate: two inputs, outputs 1 if either is 1
- NAND gate: inverted AND, outputs 0 only if both inputs are 1
- NOR gate: inverted OR, outputs 1 only if both inputs are 0
- XOR gate: two inputs, outputs 1 if they differ

NAND and NOR gates are functionally complete—any logic gate can be constructed using only NAND gates (or only NOR gates). This makes them crucial for efficient circuit design.

Each gate is typically implemented with transistors. For example:
- An AND gate with transistors connects two transistors in series: current flows only if both transistors are "on"
- An OR gate connects transistors in parallel: current flows if either transistor is "on"
- A NOT gate uses a single transistor: inverting its input

Multiple gates combine to create more complex circuits:
- Half adders and full adders: perform single-bit addition
- 4-bit adders: add two 4-bit numbers
- Multiplexers: select one of many inputs based on a control signal
- Decoders: convert binary codes into individual output lines
- Latches and flip-flops: store bits (memory)

Processor design begins with gate-level design (logic gates arranged to perform desired functions), which is then optimized, verified, and manufactured as an integrated circuit.

Modern processors contain billions of gates, but their operation ultimately reduces to millions per second of these basic Boolean operations.

Links: [[Boolean logic provides the mathematical foundation for digital circuits]], [[Transistors are semiconductor devices that amplify or switch electronic signals]]
