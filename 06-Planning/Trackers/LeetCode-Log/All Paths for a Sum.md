---
difficulty: Medium
status: Not started
topic: [Tree DFS, Trees, Backtracking]
tags: [tree-dfs, tree, backtracking, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a binary tree and a target sum S, collect every root-to-leaf path whose node values add up to S. Return all such paths as lists of node values. Unlike the single-path variant, here you need to gather every qualifying path, not just check if one exists.

### Constraints
- Tree can have 0 or more nodes
- Node values can be positive or negative integers
- Multiple paths with the same sum are all valid outputs
- Input fits in memory

### Examples
```
Tree: 1→7→4, 1→7→5, 1→9→2, 1→9→7  |  S=12  →  [[1,7,4], [1,9,2]]
Tree: 12→7→4, 12→1→10, 12→1→5      |  S=23  →  [[12,7,4], [12,1,10]]
```

### Next solve approach
1. Brute Force first — enumerate all root-to-leaf paths and filter by sum, O(n²) space for copying paths
2. Optimized (Tree DFS) — carry a running path list down the recursion; add to results at each leaf where sum matches, then backtrack

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
    public static List<List<Integer>> findPaths(TreeNode root, int sum) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(12);
        root.left = new TreeNode(7);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(4);
        root.right.left = new TreeNode(10);
        root.right.right = new TreeNode(5);

        int sum = 23;
        List<List<Integer>> result = findPaths(root, sum);
        System.out.println("Tree paths with sum " + sum + ": " + result); // expected: [[12, 7, 4], [12, 1, 10]]
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


def find_paths(root: TreeNode, sum: int) -> list[list[int]]:
    # TODO: implement
    pass


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(find_paths(root, 23))  # expected: [[12, 7, 4], [12, 1, 10]]
```
