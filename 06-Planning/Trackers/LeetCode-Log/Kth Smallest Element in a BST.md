---
difficulty: Medium
status: Not started
topic: [Trees]
tags: [tree, dfs, bst, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/kth-smallest-element-in-a-bst/"
---

### Problem
Given the root of a BST and an integer k, return the k-th smallest value (1-indexed) among all node values. Because it's a BST, an in-order traversal visits nodes in sorted order, so stopping at the k-th visit gives the answer.

### Constraints
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

### Examples
```
root=[3,1,4,null,2], k=1  →  1
root=[5,3,6,2,4,null,null,1], k=3  →  3
```

### Next solve approach
1. Brute Force first — in-order traversal into a list, return list[k-1]
2. Optimized — iterative in-order traversal with a stack, decrement k on each visit and return when k reaches 0

---

### Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

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
    public int kthSmallest(TreeNode root, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Tree: [3,1,4,null,2], k=1
        TreeNode root1 = new TreeNode(3,
            new TreeNode(1, null, new TreeNode(2)),
            new TreeNode(4));
        System.out.println(sol.kthSmallest(root1, 1)); // expected: 1

        // Tree: [5,3,6,2,4,null,null,1], k=3
        TreeNode root2 = new TreeNode(5,
            new TreeNode(3,
                new TreeNode(2, new TreeNode(1), null),
                new TreeNode(4)),
            new TreeNode(6));
        System.out.println(sol.kthSmallest(root2, 3)); // expected: 3
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

def kth_smallest(root: TreeNode, k: int) -> int:
    # TODO: implement
    pass


root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(kth_smallest(root1, 1))  # expected: 1

root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)), TreeNode(6))
print(kth_smallest(root2, 3))  # expected: 3
```
