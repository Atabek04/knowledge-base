---
difficulty: Easy
status: Not started
topic: [Trees]
tags: [tree, dfs, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/balanced-binary-tree/"
---

### Problem
Given a binary tree, determine if it is height-balanced — meaning the heights of the left and right subtrees of every node differ by at most one. Both subtrees must themselves be balanced.

### Constraints
- The number of nodes in the tree is in the range [0, 5000].
- -10^4 <= Node.val <= 10^4

### Examples
```
[3,9,20,null,null,15,7]         →  true
[1,2,2,3,3,null,null,4,4]       →  false
[]                               →  true
```

### Next solve approach
1. Brute Force first — for each node call a height function separately; O(n^2)
2. Optimized — bottom-up DFS that returns -1 when a subtree is unbalanced, short-circuiting further traversal

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
    public boolean isBalanced(TreeNode root) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Tree: [3,9,20,null,null,15,7]
        TreeNode root1 = new TreeNode(3,
            new TreeNode(9),
            new TreeNode(20, new TreeNode(15), new TreeNode(7)));
        System.out.println(sol.isBalanced(root1)); // expected: true

        // Tree: [1,2,2,3,3,null,null,4,4]
        TreeNode root2 = new TreeNode(1,
            new TreeNode(2,
                new TreeNode(3, new TreeNode(4), new TreeNode(4)),
                new TreeNode(3)),
            new TreeNode(2));
        System.out.println(sol.isBalanced(root2)); // expected: false

        System.out.println(sol.isBalanced(null)); // expected: true
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

def is_balanced(root: TreeNode) -> bool:
    # TODO: implement
    pass


root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(is_balanced(root1))  # expected: True

root2 = TreeNode(1,
    TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
    TreeNode(2))
print(is_balanced(root2))  # expected: False

print(is_balanced(None))   # expected: True
```
