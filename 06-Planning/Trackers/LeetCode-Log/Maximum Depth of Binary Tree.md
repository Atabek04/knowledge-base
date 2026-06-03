---
difficulty: Easy
status: Not started
topic: [Trees]
tags: [tree, dfs, bfs, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/maximum-depth-of-binary-tree/"
---

### Problem
Given the root of a binary tree, find the maximum depth — that is, the number of nodes along the longest path from the root down to the farthest leaf. An empty tree has depth 0.

### Constraints
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100

### Examples
```
[3,9,20,null,null,15,7]  →  3
[1,null,2]               →  2
```

### Next solve approach
1. Brute Force first — recursive DFS returning 1 + max(left depth, right depth)
2. Optimized — iterative BFS counting levels

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
    public int maxDepth(TreeNode root) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Tree: [3,9,20,null,null,15,7]
        TreeNode root1 = new TreeNode(3,
            new TreeNode(9),
            new TreeNode(20, new TreeNode(15), new TreeNode(7)));
        System.out.println(sol.maxDepth(root1)); // expected: 3

        // Tree: [1,null,2]
        TreeNode root2 = new TreeNode(1, null, new TreeNode(2));
        System.out.println(sol.maxDepth(root2)); // expected: 2

        // Empty tree
        System.out.println(sol.maxDepth(null));  // expected: 0
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

def max_depth(root: TreeNode) -> int:
    # TODO: implement
    pass


root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(max_depth(root1))  # expected: 3

root2 = TreeNode(1, None, TreeNode(2))
print(max_depth(root2))  # expected: 2

print(max_depth(None))   # expected: 0
```
