1. Bytecode loading & verification
2. Bytecode execution:
	1. Interpretation
	2. JIT compilation
3. Memory management
	- heap for objects
	- stack for method calls
	- Garbage Collection
4. Platform (OS & CPU architecture) abstraction
	- Provides consistent API regardless of underlying OS
		- API, means interfaces to interact with the platform.
	- Handles OS specific operations
	- Translates Java threading model to OS threads
5. Runtime optimization
	- Profiles code during exec
		- Profiling - JVM monitors and measures code while it's running
	- Optimizes hot code paths (JIT)
	- Inlining methods
		- read more here: [[Method inlining - replacing method call with method's actual code]]
	- Elimanating Dead Code
		- read more here: [[Eliminate dead code that never executes]]
