---
difficulty: Medium
status: Not started
topic: [Trees]
tags: [tree, dfs, bfs, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/binary-tree-right-side-view/"
---

### Problem
Given the root of a binary tree, imagine standing on the right side and looking at the tree. Return the values of the nodes that are visible from the right side, ordered from top to bottom — one value per level (the rightmost node at each level).

### Constraints
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

### Examples
```
[1,2,3,null,5,null,4]         →  [1,3,4]
[1,2,3,4,null,null,null,5]    →  [1,3,4,5]
[1,null,3]                    →  [1,3]
[]                            →  []
```

### Next solve approach
1. Brute Force first — BFS level-order, take the last element of each level
2. Optimized — DFS traversing right child before left; the first node visited at each depth is the rightmost

---

### Java

```java
import java.util.ArrayList;
import java.util.List;

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
    public List<Integer> rightSideView(TreeNode root) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Tree: [1,2,3,null,5,null,4]
        TreeNode root1 = new TreeNode(1,
            new TreeNode(2, null, new TreeNode(5)),
            new TreeNode(3, null, new TreeNode(4)));
        System.out.println(sol.rightSideView(root1)); // expected: [1, 3, 4]

        // Tree: [1,null,3]
        TreeNode root2 = new TreeNode(1, null, new TreeNode(3));
        System.out.println(sol.rightSideView(root2)); // expected: [1, 3]

        // Empty
        System.out.println(sol.rightSideView(null)); // expected: []
    }
}
```

### Python

```python
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view(root: TreeNode) -> List[int]:
    # TODO: implement
    pass


root1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(right_side_view(root1))  # expected: [1, 3, 4]

root2 = TreeNode(1, None, TreeNode(3))
print(right_side_view(root2))  # expected: [1, 3]

print(right_side_view(None))   # expected: []
```
