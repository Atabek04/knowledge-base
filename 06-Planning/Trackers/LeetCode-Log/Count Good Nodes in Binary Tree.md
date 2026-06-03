---
difficulty: Medium
status: Not started
topic: [Trees]
tags: [tree, dfs, bfs, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/count-good-nodes-in-binary-tree/"
---

### Problem
A node X in a binary tree is "good" if no node along the path from the root to X has a value greater than X's value. Given the root of a binary tree, count and return the total number of good nodes. The root is always good.

### Constraints
- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].

### Examples
```
[3,1,4,3,null,1,5]  →  4   (good nodes: root 3, node 4, node 5, node 3)
[3,3,null,4,2]      →  3   (node 2 is not good because 3 on path is greater)
[1]                 →  1
```

### Next solve approach
1. Brute Force first — DFS tracking the max value seen on the path from root to current node
2. Optimized — same DFS with max passed as parameter; no separate data structure needed

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
    public int goodNodes(TreeNode root) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Tree: [3,1,4,3,null,1,5]
        TreeNode root1 = new TreeNode(3,
            new TreeNode(1, new TreeNode(3), null),
            new TreeNode(4, new TreeNode(1), new TreeNode(5)));
        System.out.println(sol.goodNodes(root1)); // expected: 4

        // Tree: [3,3,null,4,2]
        TreeNode root2 = new TreeNode(3,
            new TreeNode(3, new TreeNode(4), new TreeNode(2)),
            null);
        System.out.println(sol.goodNodes(root2)); // expected: 3

        // Single node
        System.out.println(sol.goodNodes(new TreeNode(1))); // expected: 1
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

def good_nodes(root: TreeNode) -> int:
    # TODO: implement
    pass


root1 = TreeNode(3, TreeNode(1, TreeNode(3), None), TreeNode(4, TreeNode(1), TreeNode(5)))
print(good_nodes(root1))  # expected: 4

root2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)), None)
print(good_nodes(root2))  # expected: 3

print(good_nodes(TreeNode(1)))  # expected: 1
```
