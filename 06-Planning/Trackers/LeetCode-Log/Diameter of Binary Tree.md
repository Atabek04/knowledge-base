---
difficulty: Easy
status: Not started
topic: [Trees]
tags: [tree, dfs, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/diameter-of-binary-tree/"
---

### Problem
Given the root of a binary tree, return the length of its diameter — the longest path between any two nodes measured in number of edges. This path does not have to pass through the root.

### Constraints
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100

### Examples
```
[1,2,3,4,5]  →  3   (path 4->2->1->3 or 5->2->1->3)
[1,2]        →  1
```

### Next solve approach
1. Brute Force first — for every node compute left height + right height, take max (O(n^2))
2. Optimized — single DFS returning height while updating a global max with left_height + right_height at each node

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
    public int diameterOfBinaryTree(TreeNode root) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Tree: [1,2,3,4,5]
        TreeNode root1 = new TreeNode(1,
            new TreeNode(2, new TreeNode(4), new TreeNode(5)),
            new TreeNode(3));
        System.out.println(sol.diameterOfBinaryTree(root1)); // expected: 3

        // Tree: [1,2]
        TreeNode root2 = new TreeNode(1, new TreeNode(2), null);
        System.out.println(sol.diameterOfBinaryTree(root2)); // expected: 1
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

def diameter_of_binary_tree(root: TreeNode) -> int:
    # TODO: implement
    pass


root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(diameter_of_binary_tree(root1))  # expected: 3

root2 = TreeNode(1, TreeNode(2), None)
print(diameter_of_binary_tree(root2))  # expected: 1
```
