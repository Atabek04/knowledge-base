---
difficulty: Easy
status: Not started
topic: [Tree BFS, Trees]
tags: [tree-bfs, tree, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Find the minimum depth of a binary tree, defined as the number of nodes on the shortest path from the root down to any leaf node. A leaf is a node with no children.

### Constraints
- Tree can be empty (return 0)
- Node values can be any integer
- Input fits in memory

### Examples
```
Tree: 12 → [7,1] → [10,5]            →  minimum depth: 2   (12→1→10 or 12→1→5, but 12→7 is depth 2 and 7 has no children... wait: 7 has no children, so leaf at depth 2)
Tree: 12 → [7,1] → [9,10,5] → [11]  →  minimum depth: 3   (12→1→5, leaf at depth 3; 12→7→9 also depth 3)
```

### Next solve approach
1. Brute Force first — DFS, track depth of every leaf, return the minimum
2. Optimized (Tree BFS) — BFS level by level; the first node with no children is the shallowest leaf — return that level immediately

---

### Java

```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution {

    // TODO: implement
    public static int findDepth(TreeNode root) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        // Example 1: 12 -> [7,1] -> [10,5]  (7 is a leaf at depth 2)
        TreeNode root = new TreeNode(12);
        root.left = new TreeNode(7);
        root.right = new TreeNode(1);
        root.right.left = new TreeNode(10);
        root.right.right = new TreeNode(5);
        System.out.println(findDepth(root)); // expected: 2

        // Example 2: add 9 under 7 and 11 under 10
        root.left.left = new TreeNode(9);
        root.right.left.left = new TreeNode(11);
        System.out.println(findDepth(root)); // expected: 3
    }
}
```

### Python

```python
from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

def find_depth(root: Optional[TreeNode]) -> int:
    # TODO: implement
    pass


# Example 1: 12 -> [7,1] -> [10,5]
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(find_depth(root))  # expected: 2

# Example 2: add 9 under 7 and 11 under 10
root.left.left = TreeNode(9)
root.right.left.left = TreeNode(11)
print(find_depth(root))  # expected: 3
```
