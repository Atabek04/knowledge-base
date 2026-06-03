---
difficulty: Easy
status: Not started
topic: [Trees]
tags: [tree, dfs, bfs, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/same-tree/"
---

### Problem
Given the roots of two binary trees p and q, check if they are identical — meaning they have the same structure and every corresponding node has the same value. Both null trees are considered the same.

### Constraints
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4

### Examples
```
p=[1,2,3], q=[1,2,3]    →  true
p=[1,2],   q=[1,null,2] →  false   (different structure)
p=[1,2,1], q=[1,1,2]    →  false   (different values)
```

### Next solve approach
1. Brute Force first — DFS simultaneously on both trees, return false on any mismatch
2. Optimized — BFS with two queues, comparing node by node level by level

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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode p1 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode q1 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        System.out.println(sol.isSameTree(p1, q1)); // expected: true

        TreeNode p2 = new TreeNode(1, new TreeNode(2), null);
        TreeNode q2 = new TreeNode(1, null, new TreeNode(2));
        System.out.println(sol.isSameTree(p2, q2)); // expected: false

        TreeNode p3 = new TreeNode(1, new TreeNode(2), new TreeNode(1));
        TreeNode q3 = new TreeNode(1, new TreeNode(1), new TreeNode(2));
        System.out.println(sol.isSameTree(p3, q3)); // expected: false
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

def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    # TODO: implement
    pass


p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(is_same_tree(p1, q1))  # expected: True

p2 = TreeNode(1, TreeNode(2), None)
q2 = TreeNode(1, None, TreeNode(2))
print(is_same_tree(p2, q2))  # expected: False
```
