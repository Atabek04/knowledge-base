---
difficulty: Medium
status: Not started
topic: [Trees]
tags: [tree, array, hash-table, divide-and-conquer, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/"
---

### Problem
Given a preorder traversal array and an inorder traversal array of the same binary tree (with unique values), reconstruct and return the original tree. The first element of preorder is always the root; find it in inorder to split left and right subtrees, then recurse.

### Constraints
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.

### Examples
```
preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]  →  [3,9,20,null,null,15,7]
preorder=[-1],          inorder=[-1]            →  [-1]
```

### Next solve approach
1. Brute Force first — find root in inorder by linear scan each time; O(n^2)
2. Optimized — precompute a hash map from value to inorder index for O(1) lookup; O(n) total

---

### Java

```java
import java.util.HashMap;
import java.util.Map;

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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] preorder1 = {3, 9, 20, 15, 7};
        int[] inorder1  = {9, 3, 15, 20, 7};
        TreeNode root1 = sol.buildTree(preorder1, inorder1);
        System.out.println(root1.val);       // expected: 3
        System.out.println(root1.left.val);  // expected: 9
        System.out.println(root1.right.val); // expected: 20

        int[] preorder2 = {-1};
        int[] inorder2  = {-1};
        TreeNode root2 = sol.buildTree(preorder2, inorder2);
        System.out.println(root2.val); // expected: -1
    }
}
```

### Python

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # TODO: implement
    pass


root1 = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(root1.val)       # expected: 3
print(root1.left.val)  # expected: 9
print(root1.right.val) # expected: 20

root2 = build_tree([-1], [-1])
print(root2.val)  # expected: -1
```
