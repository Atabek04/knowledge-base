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
Given a binary tree and an integer array representing a sequence, determine whether a root-to-leaf path in the tree matches that sequence exactly — same values in the same order, and the path length must equal the sequence length (no extra or missing nodes).

### Constraints
- Sequence length >= 1
- Node values and sequence values can be any integer
- Path must go from root all the way to a leaf
- Input fits in memory

### Examples
```
Tree: 1→7→9, 1→9→2, 1→9→9  |  seq=[1,9,9]  →  true   (path 1→9→9 exists)
Tree: 1→0→1, 1→1→6, 1→1→5  |  seq=[1,0,7]  →  false  (no path 1→0→7)
Tree: 1→0→1, 1→1→6, 1→1→5  |  seq=[1,1,6]  →  true   (path 1→1→6 exists)
```

### Next solve approach
1. Brute Force first — enumerate all root-to-leaf paths and compare each to the sequence
2. Optimized (Tree DFS) — track a sequence index; advance it at each node; return true only when index exhausted exactly at a leaf

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
    public static boolean findPath(TreeNode root, int[] sequence) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(0);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(1);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(5);

        System.out.println(findPath(root, new int[]{1, 0, 7})); // expected: false
        System.out.println(findPath(root, new int[]{1, 1, 6})); // expected: true
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


def find_path(root: TreeNode, sequence: list[int]) -> bool:
    # TODO: implement
    pass


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print(find_path(root, [1, 0, 7]))  # expected: False
print(find_path(root, [1, 1, 6]))  # expected: True
```
