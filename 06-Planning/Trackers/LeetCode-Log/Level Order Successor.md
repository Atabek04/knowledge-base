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
Given a binary tree and a target node value, find the node that comes immediately after the target in a level-order (BFS) traversal. If the target is the last node in the traversal, return null.

### Constraints
- Target key is guaranteed to exist in the tree
- Node values are unique
- Input fits in memory

### Examples
```
Tree: 1 → [2,3] → [4,5],  key=3  →  successor val: 4
Tree: 12 → [7,1] → [9,10,5],  key=9   →  successor val: 10
Tree: 12 → [7,1] → [9,10,5],  key=12  →  successor val: 7
```

### Next solve approach
1. Brute Force first — collect full BFS order into a list, find key index, return index+1
2. Optimized (Tree BFS) — BFS with a queue; once the target node is dequeued, immediately return the front of the queue (next node)

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
    public static TreeNode findSuccessor(TreeNode root, int key) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(12);
        root.left = new TreeNode(7);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(9);
        root.right.left = new TreeNode(10);
        root.right.right = new TreeNode(5);

        TreeNode result = findSuccessor(root, 12);
        if (result != null) System.out.println(result.val); // expected: 7

        result = findSuccessor(root, 9);
        if (result != null) System.out.println(result.val); // expected: 10
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

def find_successor(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    # TODO: implement
    pass


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

result = find_successor(root, 12)
print(result.val if result else None)  # expected: 7

result = find_successor(root, 9)
print(result.val if result else None)  # expected: 10
```
