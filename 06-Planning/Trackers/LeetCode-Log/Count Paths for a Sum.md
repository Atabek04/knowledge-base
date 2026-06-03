---
difficulty: Medium
status: Not started
topic: [Tree DFS, Trees]
tags: [tree-dfs, tree, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a binary tree and a target sum S, count all paths whose node values sum to S. Unlike the root-to-leaf variant, paths here can start and end at any node in the tree, but they must always go downward from parent to child — you cannot go upward or skip nodes.

### Constraints
- Tree can have 0 or more nodes
- Node values can be positive or negative integers
- Paths must follow the parent-to-child direction only
- Input fits in memory

### Examples
```
Tree: 1→7→6, 1→7→5, 1→9→2, 1→9→3  |  S=12  →  3   (7→5, 1→9→2, 9→3)
Tree: 12→7→4, 12→1→10, 12→1→5      |  S=11  →  2   (7→4, 1→10)
```

### Next solve approach
1. Brute Force first — for every node, DFS downward summing all paths starting there; O(n²) time
2. Optimized (Tree DFS) — use a prefix-sum map to find how many ancestors produce the needed complement; O(n)

---

### Java

```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution {

    // TODO: implement
    public static int countPaths(TreeNode root, int S) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(12);
        root.left = new TreeNode(7);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(4);
        root.right.left = new TreeNode(10);
        root.right.right = new TreeNode(5);

        System.out.println("Tree has path: " + countPaths(root, 11)); // expected: 2
    }
}
```

### Python

```python
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def count_paths(root: TreeNode, s: int) -> int:
    # TODO: implement
    pass


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(count_paths(root, 11))  # expected: 2
```
