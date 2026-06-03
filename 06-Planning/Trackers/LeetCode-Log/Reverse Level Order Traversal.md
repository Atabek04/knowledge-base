---
difficulty: Easy
status: Not started
topic: [Tree BFS, Trees]
tags: [tree-bfs, tree, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a binary tree, perform a level-order traversal but return the result in bottom-up order — the deepest level first and the root level last. Within each level, values go left to right.

### Constraints
- Tree can be empty (return empty list)
- Node values can be any integer
- Input fits in memory

### Examples
```
Tree: 1 → [2,3] → [4,5,6,7]    →  [[4,5,6,7],[2,3],[1]]
Tree: 12 → [7,1] → [9,10,5]    →  [[9,10,5],[7,1],[12]]
```

### Next solve approach
1. Brute Force first — BFS into a list, then reverse the list at the end
2. Optimized (Tree BFS) — BFS but prepend each level to the front of a LinkedList so reversal is built-in

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
        return new LinkedList<>();
    }

    public static void main(String[] args) {
        // Example 1
        TreeNode root1 = new TreeNode(1);
        root1.left = new TreeNode(2);
        root1.right = new TreeNode(3);
        root1.left.left = new TreeNode(4);
        root1.left.right = new TreeNode(5);
        root1.right.left = new TreeNode(6);
        root1.right.right = new TreeNode(7);
        System.out.println(traverse(root1)); // expected: [[4,5,6,7],[2,3],[1]]

        // Example 2
        TreeNode root2 = new TreeNode(12);
        root2.left = new TreeNode(7);
        root2.right = new TreeNode(1);
        root2.left.left = new TreeNode(9);
        root2.right.left = new TreeNode(10);
        root2.right.right = new TreeNode(5);
        System.out.println(traverse(root2)); // expected: [[9,10,5],[7,1],[12]]
    }
}
```

### Python

```python
from typing import Optional
from collections import deque

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
print(traverse(root1))  # expected: [[4,5,6,7],[2,3],[1]]

# Example 2
root2 = TreeNode(12)
root2.left = TreeNode(7)
root2.right = TreeNode(1)
root2.left.left = TreeNode(9)
root2.right.left = TreeNode(10)
root2.right.right = TreeNode(5)
print(traverse(root2))  # expected: [[9,10,5],[7,1],[12]]
```
