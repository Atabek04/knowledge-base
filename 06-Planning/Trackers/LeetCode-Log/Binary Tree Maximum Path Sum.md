---
difficulty: Hard
status: Not started
topic: [Trees]
tags: [tree, dfs, dynamic-programming, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/binary-tree-maximum-path-sum/"
---

### Problem
A path in a binary tree is a sequence of nodes connected by edges where each node appears at most once; it does not need to pass through the root. Given the root of a binary tree, find the path whose node values sum to the maximum and return that sum. Values can be negative.

### Constraints
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000

### Examples
```
[1,2,3]                    →  6    (path 2->1->3)
[-10,9,20,null,null,15,7]  →  42   (path 15->20->7)
```

### Next solve approach
1. Brute Force first — enumerate all paths via DFS from every node, track max; O(n^2)
2. Optimized — single DFS returning max one-sided gain from each node; update global max with left_gain + node + right_gain at each node

---

### Java

```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val; this.left = left; this.right = right;
    }
}
public class Solution {

    // TODO: implement
    public int maxPathSum(TreeNode root) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Tree: [1,2,3]
        TreeNode root1 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        System.out.println(sol.maxPathSum(root1)); // expected: 6

        // Tree: [-10,9,20,null,null,15,7]
        TreeNode root2 = new TreeNode(-10,
            new TreeNode(9),
            new TreeNode(20, new TreeNode(15), new TreeNode(7)));
        System.out.println(sol.maxPathSum(root2)); // expected: 42
    }
}
```

### Python

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root: TreeNode) -> int:
    # TODO: implement
    pass


root1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(max_path_sum(root1))  # expected: 6

root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(max_path_sum(root2))  # expected: 42
```
