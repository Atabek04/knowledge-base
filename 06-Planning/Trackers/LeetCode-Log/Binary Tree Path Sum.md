---
difficulty: Easy
status: Not started
topic: [Tree DFS, Trees]
tags: [tree-dfs, tree, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a binary tree and a target sum S, determine whether any root-to-leaf path exists whose node values add up exactly to S. A valid path must go all the way from the root down to a leaf node — you cannot stop at an intermediate node.

### Constraints
- Tree can have 0 or more nodes
- Node values can be positive or negative integers
- S can be any integer
- Input fits in memory

### Examples
```
Tree: 12→7→9, 12→1→10, 12→1→5  |  S=23  →  true   (path 12→1→10)
Tree: 12→7→9, 12→1→10, 12→1→5  |  S=16  →  false  (no root-to-leaf path sums to 16)
```

### Next solve approach
1. Brute Force first — enumerate all root-to-leaf paths and check each sum, O(n)
2. Optimized (Tree DFS) — subtract node value from S as you recurse; return true when a leaf is reached with remaining sum = 0

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
    public static boolean hasPath(TreeNode root, int sum) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(12);
        root.left = new TreeNode(7);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(9);
        root.right.left = new TreeNode(10);
        root.right.right = new TreeNode(5);

        System.out.println(hasPath(root, 23)); // expected: true
        System.out.println(hasPath(root, 16)); // expected: false
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


def has_path(root: TreeNode, sum: int) -> bool:
    # TODO: implement
    pass


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(has_path(root, 23))  # expected: True
print(has_path(root, 16))  # expected: False
```
