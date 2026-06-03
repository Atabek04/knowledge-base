---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [dfs, bfs, graph, hash-table, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/clone-graph/"
---

### Problem
Given a reference to a node in a connected undirected graph, return a deep copy of the entire graph. Each node holds an integer value and a list of its neighbors. The input is always the node with val = 1, and node values match their 1-based index.

### Constraints
- The number of nodes in the graph is in the range [0, 100]
- 1 <= Node.val <= 100
- Node.val is unique for each node
- There are no repeated edges and no self-loops
- The graph is connected and all nodes can be visited from the given node

### Examples
```
adjList = [[2,4],[1,3],[2,4],[1,3]]  →  [[2,4],[1,3],[2,4],[1,3]]     (4-node cycle graph)
adjList = [[]]                        →  [[]]                           (single node, no neighbors)
adjList = []                          →  []                             (empty graph)
```

### Next solve approach
1. Brute Force first — DFS/BFS from the given node, use a HashMap to map original nodes to their clones
2. Optimized — same HashMap + DFS in one pass; the map serves as both the visited set and clone registry

---

### Java

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Node {
    public int val;
    public List<Node> neighbors;
    public Node() { val = 0; neighbors = new ArrayList<>(); }
    public Node(int _val) { val = _val; neighbors = new ArrayList<>(); }
    public Node(int _val, ArrayList<Node> _neighbors) { val = _val; neighbors = _neighbors; }
}

public class Solution {

    // TODO: implement
    public Node cloneGraph(Node node) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Build: 1--2--3--4--1 (adjList = [[2,4],[1,3],[2,4],[1,3]])
        Node n1 = new Node(1);
        Node n2 = new Node(2);
        Node n3 = new Node(3);
        Node n4 = new Node(4);
        n1.neighbors.add(n2); n1.neighbors.add(n4);
        n2.neighbors.add(n1); n2.neighbors.add(n3);
        n3.neighbors.add(n2); n3.neighbors.add(n4);
        n4.neighbors.add(n1); n4.neighbors.add(n3);

        Node cloned = sol.cloneGraph(n1);
        System.out.println(cloned != n1);           // expected: true (deep copy)
        System.out.println(cloned.val);             // expected: 1
        System.out.println(cloned.neighbors.size()); // expected: 2

        // Empty graph
        System.out.println(sol.cloneGraph(null));   // expected: null
    }
}
```

### Python

```python
from typing import Optional

class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: Optional[Node]) -> Optional[Node]:
    # TODO: implement
    pass


# Build: 1--2--3--4--1
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

cloned = clone_graph(n1)
print(cloned is not n1)            # expected: True
print(cloned.val)                  # expected: 1
print(clone_graph(None))           # expected: None
```
