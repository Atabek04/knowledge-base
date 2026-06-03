---
difficulty: Hard
status: Not started
topic: [Trees]
tags: [tree, dfs, bfs, design, string, binary-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/"
---

### Problem
Design an algorithm that converts a binary tree to a string (serialize) and then reconstructs the original tree from that string (deserialize). There is no restriction on the format you choose — the only requirement is that serialize followed by deserialize returns the original tree structure.

### Constraints
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000

### Examples
```
serialize([1,2,3,null,null,4,5])  →  some string S
deserialize(S)                    →  [1,2,3,null,null,4,5]

serialize([])  →  ""
deserialize("") →  []
```

### Next solve approach
1. Brute Force first — BFS level-order serialize using "#" for nulls, split on deserialize
2. Optimized — DFS preorder serialize with "#" markers; reconstruct recursively using an index pointer

---

### Java

```java
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
public class Codec {

    // TODO: implement
    public String serialize(TreeNode root) {
        // TODO
        return "";
    }

    // TODO: implement
    public TreeNode deserialize(String data) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Codec codec = new Codec();

        // Tree: [1,2,3,null,null,4,5]
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(5);

        String data = codec.serialize(root);
        System.out.println(data); // expected: some non-null string

        TreeNode rebuilt = codec.deserialize(data);
        System.out.println(rebuilt.val);            // expected: 1
        System.out.println(rebuilt.left.val);       // expected: 2
        System.out.println(rebuilt.right.val);      // expected: 3
        System.out.println(rebuilt.right.left.val); // expected: 4

        // Empty tree
        String empty = codec.serialize(null);
        TreeNode rebuiltEmpty = codec.deserialize(empty);
        System.out.println(rebuiltEmpty);           // expected: null
    }
}
```

### Python

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        # TODO: implement
        pass

    def deserialize(self, data: str) -> TreeNode:
        # TODO: implement
        pass


codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

data = codec.serialize(root)
rebuilt = codec.deserialize(data)
print(rebuilt.val)            # expected: 1
print(rebuilt.right.left.val) # expected: 4
```
