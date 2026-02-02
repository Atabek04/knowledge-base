Alan Turing, an English mathematician, proved in 1936 that there exists a universal computing machine—a device that, given appropriate instructions, could perform any computable operation.

This theoretical device, now called a Turing machine, consists of:
- An infinite tape divided into cells, each containing a symbol
- A read/write head that examines one cell at a time
- A state register tracking the machine's internal state
- A transition function defining what to do based on current symbol and state

The Turing machine has no special knowledge of any specific problem—it is purely mechanical symbol manipulation. Yet Turing proved that any computable problem could be solved by appropriate instructions (a program) for a Turing-complete machine.

This theoretical result has profound practical implications:
- Any modern computer is fundamentally a Turing machine (though with finite memory)
- The specific hardware details don't matter—what matters is Turing completeness
- Sufficiently powerful computers can run any program (within memory and time constraints)

The Church-Turing thesis (developed independently by Alonzo Church) states that any computable function can be computed by a Turing machine. This remains unproven but is accepted universally in computer science.

Consequences for computing:
- Programming languages compile to machine instructions, but the abstract logic is universal
- One computer can emulate any other computer (given sufficient time and memory)
- There exist uncomputable problems—things no computer (Turing machine or otherwise) can solve
- The halting problem is undecidable: no algorithm can determine whether an arbitrary program will halt or run forever

Turing's work connected mathematical logic to practical computation, establishing that computing is fundamentally about symbol manipulation according to mechanical rules.

During World War II, Turing designed Colossus, an electronic computer that broke German Enigma encryption through massive parallel computation—a practical application of his theoretical insights.

Links: [[Charles Babbage designed the first programmable computing machine in 1822]], [[Von Neumann architecture separates processor, memory, and control units]]
