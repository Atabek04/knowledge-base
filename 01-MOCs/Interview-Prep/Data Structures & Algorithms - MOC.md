---
tags: [moc]
---

Core building blocks: data structures that organize data + algorithms that operate on them. Master these → solve any interview problem.

## Data Structures

### Arrays & Sequences
- [ ] Arrays enable O(1) random access but fixed size
- [ ] Linked Lists trade random access for O(1) insertion/deletion at known position
- [ ] Stacks LIFO — push/pop from one end
- [ ] Queues FIFO — enqueue one end, dequeue other

### Hash-based
- [[List comprehension is Python's inline filter-map equivalent to Stream API|Python list comprehensions]]
- [ ] Hash Tables O(1) lookup with collisions → chaining or probing
- [ ] Hash Sets uniqueness + O(1) membership test
- [ ] Hash Maps key-value storage with O(1) get/put

### Trees
- [ ] Binary Trees nodes with ≤2 children
- [ ] Binary Search Trees left < node < right → in-order traversal yields sorted
- [ ] Balanced Trees (AVL, Red-Black) maintain O(log n) operations
- [ ] Tries prefix trees for string search
- [ ] Heaps complete binary tree where parent ≤/≥ children

### Graphs
- [ ] Adjacency List sparse graph representation
- [ ] Adjacency Matrix dense graph representation
- [ ] Directed vs Undirected cycles → topological sort only on DAGs

## Searching Algorithms

- [ ] Linear Search O(n) — no preprocessing needed
- [ ] Binary Search O(log n) — requires sorted array or BST
- [ ] BFS breadth-first → shortest path in unweighted graphs
- [ ] DFS depth-first → explore fully before backtracking

## Sorting Algorithms

- [ ] Quick Sort O(n log n) average, in-place, unstable
- [ ] Merge Sort O(n log n) guaranteed, stable, needs O(n) extra space
- [ ] Heap Sort O(n log n) guaranteed, in-place, unstable
- [ ] Counting Sort O(n + k) for integers in range [0, k]

## Core Techniques

### Sequence & Array
- [[Sliding Window scans contiguous subarrays in O(n) by reusing overlap instead of recomputing|Sliding Window — scans contiguous subarrays by reusing overlap]]
- [ ] Two Pointers converge from ends toward middle
- [ ] Fast & Slow Pointers cycle detection
- [ ] Prefix & Suffix sums precompute range queries

### Optimization Patterns
- [ ] Greedy local best → global optimal
- [ ] Divide & Conquer split problem into independent subproblems
- [ ] Dynamic Programming memoize subproblem results

### Graph Patterns
- [ ] Topological Sort DFS-based ordering for DAGs
- [ ] Union-Find disjoint set operations for connectivity
- [ ] Dijkstra shortest path in weighted graphs

## Specific Problem Techniques

- [ ] Longest Consecutive uses set to O(1) check num±1 existence
- [ ] Subarray Sum uses prefix sum + hash map for O(n) lookup
- [ ] Majority Element Boyer-Moore voting in O(1) space
