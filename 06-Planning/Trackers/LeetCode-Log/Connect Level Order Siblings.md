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
Given a binary tree where each node has an extra `next` pointer, wire up every node's `next` to point to the node immediately to its right within the same level. The rightmost node at each level should have its `next` set to null.

### Constraints
- Tree can be empty (no-op)
- Modification is in-place — do not return a new tree
- Node values can be any integer

### Examples
```
Tree: 1 → [2,3] → [4,5,6,7]
After: 1->null, 2->3->null, 4->5->6->7->null

Tree: 12 → [7,1] → [9,10,5]
After: 12->null, 7->1->null, 9->10->5->null
```

### Next solve approach
1. Brute Force first — BFS into a list per level, iterate each list linking node.next to the next element
2. Optimized (Tree BFS) — BFS with level-size snapshot; link each dequeued node's next to the next node in the queue, setting null at level boundaries

---

### Java

```java
import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode next;

    TreeNode(int x) { val = x; left = right = next = null; }

    void printLevelOrder() {
        TreeNode nextLevelRoot = this;
        while (nextLevelRoot != null) {
            TreeNode current = nextLevelRoot;
            nextLevelRoot = null;
            while (current != null) {
                System.out.print(current.val + " ");
                if (nextLevelRoot == null) {
                    if (current.left != null) nextLevelRoot = current.left;
                    else if (current.right != null) nextLevelRoot = current.right;
                }
                current = current.next;
            }
            System.out.println();
        }
    }
}

public class Solution {

    // TODO: implement
    public static void connect(TreeNode root) {
        // TODO
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
        connect(root1);
        root1.printLevelOrder();
        // expected: 1 | 2 3 | 4 5 6 7 (each row linked via next, ends with null)

        // Example 2
        TreeNode root2 = new TreeNode(12);
        root2.left = new TreeNode(7);
        root2.right = new TreeNode(1);
        root2.left.left = new TreeNode(9);
        root2.right.left = new TreeNode(10);
        root2.right.right = new TreeNode(5);
        connect(root2);
        root2.printLevelOrder();
        // expected: 12 | 7 1 | 9 10 5
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
        self.next: Optional['TreeNode'] = None

    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(current.val, end=" ")
                if next_level_root is None:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
            print()

def connect(root: Optional[TreeNode]) -> None:
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
connect(root1)
root1.print_level_order()  # expected: 1 / 2 3 / 4 5 6 7

# Example 2
root2 = TreeNode(12)
root2.left = TreeNode(7)
root2.right = TreeNode(1)
root2.left.left = TreeNode(9)
root2.right.left = TreeNode(10)
root2.right.right = TreeNode(5)
connect(root2)
root2.print_level_order()  # expected: 12 / 7 1 / 9 10 5
```
