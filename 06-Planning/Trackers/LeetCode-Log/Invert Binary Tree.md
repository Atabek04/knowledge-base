---
difficulty: Easy
status: Not started
topic: [Trees]
tags: [tree, dfs, bfs, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/invert-binary-tree/"
---

### Problem
Given the root of a binary tree, mirror it by swapping the left and right children at every node. The operation must be applied recursively to every node in the tree. Return the root of the inverted tree.

### Constraints
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

### Examples
```
[4,2,7,1,3,6,9]  →  [4,7,2,9,6,3,1]
[2,1,3]           →  [2,3,1]
[]                →  []
```

### Next solve approach
1. Brute Force first — recurse and swap left/right children at each node
2. Optimized — BFS level-order traversal swapping children as you dequeue

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
    public TreeNode invertTree(TreeNode root) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Tree: [4,2,7,1,3,6,9]
        TreeNode root1 = new TreeNode(4,
            new TreeNode(2, new TreeNode(1), new TreeNode(3)),
            new TreeNode(7, new TreeNode(6), new TreeNode(9)));
        TreeNode r1 = sol.invertTree(root1);
        System.out.println(r1.val);       // expected: 4
        System.out.println(r1.left.val);  // expected: 7
        System.out.println(r1.right.val); // expected: 2

        // Tree: [2,1,3]
        TreeNode root2 = new TreeNode(2, new TreeNode(1), new TreeNode(3));
        TreeNode r2 = sol.invertTree(root2);
        System.out.println(r2.left.val);  // expected: 3

        // Empty tree
        TreeNode r3 = sol.invertTree(null);
        System.out.println(r3);           // expected: null
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

def invert_tree(root: TreeNode) -> TreeNode:
    # TODO: implement
    pass


root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
r1 = invert_tree(root1)
print(r1.left.val)   # expected: 7

root2 = TreeNode(2, TreeNode(1), TreeNode(3))
r2 = invert_tree(root2)
print(r2.left.val)   # expected: 3
```
