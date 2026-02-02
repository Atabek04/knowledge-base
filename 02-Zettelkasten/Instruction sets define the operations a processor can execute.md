An instruction set is the complete list of operations a processor can execute, specified as binary codes that the processor recognizes and implements.

Each instruction specifies:
- Operation: what to do (add, move, compare, jump)
- Operands: what data to operate on (register addresses, memory addresses, immediate values)
- Result: where to store the result (register or memory)

Example x86-64 instructions:
- MOV: move data from one location to another
- ADD: add two values
- JMP: jump to different instruction address (control flow)
- CMP: compare values (sets flags for conditional branching)
- CALL: call a procedure (function)

Instruction set architecture (ISA) defines the processor model:
- x86/x86-64: Intel and AMD processors (desktop, server, laptop)
- ARM: mobile devices, embedded systems, increasingly server
- RISC-V: open-source ISA, emerging in embedded and academic settings
- MIPS: older ISA, still used in embedded systems

RISC vs. CISC:
- RISC (Reduced Instruction Set Computer): simple instructions, each executes in one cycle, benefits from pipelining
- CISC (Complex Instruction Set Computer): complex instructions that do multiple operations, fewer instructions needed per program

Modern processors blur this distinction: internally, they decode complex instructions into simple microoperations that pipeline efficiently.

Instruction width:
- 16-bit: ARM Thumb mode, RISC-V compressed
- 32-bit: most common (x86, ARM, MIPS, RISC-V)
- 64-bit: rare (x86-64 uses fixed 32-bit instructions with additional addressing modes)

Program execution:
1. Instruction fetched from memory at program counter address
2. Decoded into operation and operands
3. Operands retrieved from registers or memory
4. ALU executes operation
5. Result written to destination
6. Program counter incremented (or changed by jump instructions)

Compatibility:
- x86-64 maintains backward compatibility with 32-bit x86 (introduced 1978)
- ARM processors support both 32-bit and 64-bit instruction modes
- ISA changes are rare because they break existing software

The instruction set is the boundary between hardware and software: software (programs) is written as instructions; hardware implements the execution mechanism.

Links: [[Von Neumann architecture separates processor, memory, and control units]], [[Logic gates are the fundamental building blocks of digital circuits]]
