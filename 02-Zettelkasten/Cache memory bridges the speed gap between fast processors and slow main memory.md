Cache memory is a small, fast memory located on or near the processor that stores recently accessed data, reducing the speed gap between processor execution and main memory access.

The memory hierarchy reflects a fundamental tradeoff:
- Faster memory is smaller and more expensive per bit
- Slower memory is larger and cheaper per bit

Modern systems organize memory in layers:
- L1 cache: 32-64 KB per core, ~1 cycle latency (on-chip, SRAM)
- L2 cache: 256 KB per core, ~4 cycles latency (on-chip, SRAM)
- L3 cache: 4-8 MB shared, ~12 cycles latency (on-chip, SRAM)
- Main memory (RAM): 4-128 GB, ~100 cycles latency (off-chip, DRAM)
- Disk storage: terabytes, millions of cycles latency (magnetic or flash)

Cache works by storing copies of recently accessed data:
- When processor requests data, it first checks L1 cache (fast)
- If miss (not found), check L2 cache
- If miss, check L3 cache
- If miss, fetch from main memory (slow, 100+ cycle wait)
- Loaded data is copied back into cache for quick reaccess

Temporal locality: data accessed once is often accessed again soon (loops, repeated operations)
Spatial locality: data near recently accessed data tends to be accessed next (sequential access)

These patterns mean cache is highly effective—hit rates (finding data in cache) often exceed 90%, so typical memory access averages faster than main memory alone.

Cache invalidation challenge:
- If data in cache becomes stale (modified in memory), stale data must be removed or updated
- This is notoriously difficult in multiprocessor systems with multiple caches
- Cache coherency protocols ensure all caches see consistent data

Cache optimization:
- Line size: caches transfer data in fixed-size chunks (typically 64 bytes); accessing sequential data is cheap
- Associativity: determines flexibility in where data can be stored in cache
- Replacement policy: decides what data to remove when cache is full

Without cache, modern processors would be starved for data—they execute instructions much faster than they can fetch data from main memory. Cache is essential to practical computer performance.

Links: [[RAM stores data in volatile memory using transistors and capacitors]], [[Logic gates are the fundamental building blocks of digital circuits]]
