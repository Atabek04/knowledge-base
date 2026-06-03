---
difficulty: Easy
status: Not started
topic: [Trees]
tags: [tree, dfs, binary-tree, string-matching, hash-function, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/subtree-of-another-tree/"
---

### Problem
Given the roots of two binary trees root and subRoot, return true if subRoot appears as a subtree somewhere in root. A subtree is a node in root together with all its descendants. A tree is considered a subtree of itself.

### Constraints
- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4

### Examples
```
root=[3,4,5,1,2], subRoot=[4,1,2]                        →  true
root=[3,4,5,1,2,null,null,null,null,0], subRoot=[4,1,2]  →  false
```

### Next solve approach
1. Brute Force first — at each node of root, check if the subtree rooted there equals subRoot using isSameTree; O(n*m)
2. Optimized — serialize both trees to strings and use KMP/Rabin-Karp for substring matching; O(n+m)

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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // root=[3,4,5,1,2], subRoot=[4,1,2]
        TreeNode root1 = new TreeNode(3,
            new TreeNode(4, new TreeNode(1), new TreeNode(2)),
            new TreeNode(5));
        TreeNode sub1 = new TreeNode(4, new TreeNode(1), new TreeNode(2));
        System.out.println(sol.isSubtree(root1, sub1)); // expected: true

        // root=[3,4,5,1,2,null,null,null,null,0], subRoot=[4,1,2]
        TreeNode extra = new TreeNode(4,
            new TreeNode(1, null, new TreeNode(0)),
            new TreeNode(2));
        TreeNode root2 = new TreeNode(3, extra, new TreeNode(5));
        TreeNode sub2 = new TreeNode(4, new TreeNode(1), new TreeNode(2));
        System.out.println(sol.isSubtree(root2, sub2)); // expected: false
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

def is_subtree(root: TreeNode, sub_root: TreeNode) -> bool:
    # TODO: implement
    pass


root1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
sub1 = TreeNode(4, TreeNode(1), TreeNode(2))
print(is_subtree(root1, sub1))  # expected: True

root2 = TreeNode(3, TreeNode(4, TreeNode(1, None, TreeNode(0)), TreeNode(2)), TreeNode(5))
sub2 = TreeNode(4, TreeNode(1), TreeNode(2))
print(is_subtree(root2, sub2))  # expected: False
```
