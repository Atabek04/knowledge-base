---
difficulty: Medium
status: Not started
topic: [Tree BFS, Trees]
tags: [tree-bfs, tree, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a binary tree, traverse it level by level but alternate the direction at each level: left-to-right for odd levels (1st, 3rd, …) and right-to-left for even levels (2nd, 4th, …). Return each level as its own sub-array.

### Constraints
- Tree can be empty (return empty list)
- Node values can be any integer
- Input fits in memory

### Examples
```
Tree: 1 → [2,3] → [4,5,6,7]              →  [[1],[3,2],[4,5,6,7]]
Tree: 12 → [7,1] → [9,10,5] → [20,17]   →  [[12],[1,7],[9,10,5],[17,20]]
```

### Next solve approach
1. Brute Force first — BFS normally, then reverse every other level's list
2. Optimized (Tree BFS) — use a deque per level; append to front or back based on a left-to-right boolean flag

---

### Java

```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution {

    // TODO: implement
    public static List<List<Integer>> traverse(TreeNode root) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        // Example 1: tree 1 -> [2,3] -> [4,5,6,7]
        TreeNode root1 = new TreeNode(1);
        root1.left = new TreeNode(2);
        root1.right = new TreeNode(3);
        root1.left.left = new TreeNode(4);
        root1.left.right = new TreeNode(5);
        root1.right.left = new TreeNode(6);
        root1.right.right = new TreeNode(7);
        System.out.println(traverse(root1)); // expected: [[1],[3,2],[4,5,6,7]]

        // Example 2: tree 12 -> [7,1] -> [9,10,5] with 10 having children 20,17
        TreeNode root2 = new TreeNode(12);
        root2.left = new TreeNode(7);
        root2.right = new TreeNode(1);
        root2.left.left = new TreeNode(9);
        root2.right.left = new TreeNode(10);
        root2.right.right = new TreeNode(5);
        root2.right.left.left = new TreeNode(20);
        root2.right.left.right = new TreeNode(17);
        System.out.println(traverse(root2)); // expected: [[12],[1,7],[9,10,5],[17,20]]
    }
}
```

### Python

```python
from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

def traverse(root: Optional[TreeNode]) -> list[list[int]]:
    # TODO: implement
    pass


# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
print(traverse(root1))  # expected: [[1],[3,2],[4,5,6,7]]

# Example 2
root2 = TreeNode(12)
root2.left = TreeNode(7)
root2.right = TreeNode(1)
root2.left.left = TreeNode(9)
root2.right.left = TreeNode(10)
root2.right.right = TreeNode(5)
root2.right.left.left = TreeNode(20)
root2.right.left.right = TreeNode(17)
print(traverse(root2))  # expected: [[12],[1,7],[9,10,5],[17,20]]
```
