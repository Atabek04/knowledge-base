---
difficulty: Medium
status: Not started
topic: [Trees]
tags: [tree, dfs, bst, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/"
---

### Problem
Given a BST and two nodes p and q that are guaranteed to exist in it, find their lowest common ancestor — the deepest node that has both p and q as descendants. A node counts as a descendant of itself, so if p is an ancestor of q, p is the LCA.

### Constraints
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.

### Examples
```
root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=8  →  6   (LCA is root)
root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=4  →  2   (p is ancestor of q)
root=[2,1], p=2, q=1                           →  2
```

### Next solve approach
1. Brute Force first — find root-to-p and root-to-q paths, then find last common node
2. Optimized — exploit BST property: if both p and q are less than current, go left; if both greater, go right; otherwise current node is LCA

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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Tree: [6,2,8,0,4,7,9,null,null,3,5]
        TreeNode n0 = new TreeNode(0);
        TreeNode n3 = new TreeNode(3);
        TreeNode n5 = new TreeNode(5);
        TreeNode n4 = new TreeNode(4); n4.left = n3; n4.right = n5;
        TreeNode n2 = new TreeNode(2); n2.left = n0; n2.right = n4;
        TreeNode n7 = new TreeNode(7);
        TreeNode n9 = new TreeNode(9);
        TreeNode n8 = new TreeNode(8); n8.left = n7; n8.right = n9;
        TreeNode root = new TreeNode(6); root.left = n2; root.right = n8;

        TreeNode lca1 = sol.lowestCommonAncestor(root, n2, n8);
        System.out.println(lca1.val); // expected: 6

        TreeNode lca2 = sol.lowestCommonAncestor(root, n2, n4);
        System.out.println(lca2.val); // expected: 2
    }
}
```

### Python

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # TODO: implement
    pass


n0, n3, n5 = TreeNode(0), TreeNode(3), TreeNode(5)
n4 = TreeNode(4); n4.left = n3; n4.right = n5
n2 = TreeNode(2); n2.left = n0; n2.right = n4
n7, n9 = TreeNode(7), TreeNode(9)
n8 = TreeNode(8); n8.left = n7; n8.right = n9
root = TreeNode(6); root.left = n2; root.right = n8

print(lowest_common_ancestor(root, n2, n8).val)  # expected: 6
print(lowest_common_ancestor(root, n2, n4).val)  # expected: 2
```
