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
Each node in a binary tree holds a single digit (0–9). Every root-to-leaf path spells out a multi-digit number by concatenating the digits top-to-bottom. Return the total sum of all such numbers across every root-to-leaf path in the tree.

### Constraints
- Each node value is a digit: 0 ≤ val ≤ 9
- Tree has at least one node
- Number of nodes fits in memory; total sum fits in a 32-bit integer

### Examples
```
Tree: 1→7→9, 1→9→2, 1→9→9  →  408   (17 + 192 + 199)
Tree: 1→0→1, 1→1→6, 1→1→5  →  332   (101 + 116 + 115)
```

### Next solve approach
1. Brute Force first — collect all root-to-leaf paths as strings, parse each to int, sum them
2. Optimized (Tree DFS) — pass the running number down as `currentNumber = currentNumber * 10 + node.val`; add to total at each leaf

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
    public static int findSumOfPathNumbers(TreeNode root) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(0);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(1);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(5);

        System.out.println("Total Sum of Path Numbers: " + findSumOfPathNumbers(root)); // expected: 332
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


def find_sum_of_path_numbers(root: TreeNode) -> int:
    # TODO: implement
    pass


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print(find_sum_of_path_numbers(root))  # expected: 332
```
