---
difficulty: Medium
status: Not started
topic: [Trees]
tags: [tree, dfs, bst, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/validate-binary-search-tree/"
---

### Problem
Given the root of a binary tree, determine whether it is a valid BST. A valid BST requires every node in the left subtree to be strictly less than the node, every node in the right subtree to be strictly greater, and both subtrees must themselves be valid BSTs.

### Constraints
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

### Examples
```
[2,1,3]               →  true
[5,1,4,null,null,3,6] →  false   (right child 4 < root 5)
```

### Next solve approach
1. Brute Force first — in-order traversal to list, then check if strictly ascending
2. Optimized — DFS carrying min/max bounds down the tree; each node must fall strictly within its valid range

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
    public boolean isValidBST(TreeNode root) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Tree: [2,1,3]
        TreeNode root1 = new TreeNode(2, new TreeNode(1), new TreeNode(3));
        System.out.println(sol.isValidBST(root1)); // expected: true

        // Tree: [5,1,4,null,null,3,6]
        TreeNode root2 = new TreeNode(5,
            new TreeNode(1),
            new TreeNode(4, new TreeNode(3), new TreeNode(6)));
        System.out.println(sol.isValidBST(root2)); // expected: false
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

def is_valid_bst(root: TreeNode) -> bool:
    # TODO: implement
    pass


root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(is_valid_bst(root1))  # expected: True

root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(is_valid_bst(root2))  # expected: False
```
