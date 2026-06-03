---
difficulty: Medium
status: Not started
topic: [Linked List]
tags: [hash-table, linked-list, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/copy-list-with-random-pointer/"
---

### Problem
Each node in the linked list has a val, a next pointer, and a random pointer that can point to any node in the list or null. Produce a deep copy of the entire list: every node must be a brand new object, and the next and random pointers of the copies must mirror the original structure without referencing any original nodes.

### Constraints
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is null or points to some node in the linked list

### Examples
```
[[7,null],[13,0],[11,4],[10,2],[1,0]]  →  [[7,null],[13,0],[11,4],[10,2],[1,0]]
[[1,1],[2,1]]                          →  [[1,1],[2,1]]
[[3,null],[3,0],[3,null]]              →  [[3,null],[3,0],[3,null]]
```

### Next solve approach
1. Brute Force first — two passes with a HashMap: first pass creates all new nodes, second pass wires next and random using the map
2. Optimized — interleave cloned nodes directly after each original node (O(1) space); set random pointers in a second pass; split the interleaved list in a third pass

---

### Java

```java
import java.util.HashMap;
import java.util.Map;

public class Solution {

    static class Node {
        int val;
        Node next;
        Node random;
        public Node(int val) {
            this.val = val;
            this.next = null;
            this.random = null;
        }
    }

    // TODO: implement
    public Node copyRandomList(Node head) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // [[7,null],[13,0],[11,4],[10,2],[1,0]]
        Node n1 = new Node(7);
        Node n2 = new Node(13);
        Node n3 = new Node(11);
        Node n4 = new Node(10);
        Node n5 = new Node(1);
        n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5;
        n1.random = null; n2.random = n1; n3.random = n5; n4.random = n3; n5.random = n1;

        Node copy = sol.copyRandomList(n1);
        System.out.println(copy); // expected: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    }
}
```

### Python

```python
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head: Node) -> Node:
    # TODO: implement
    pass


n1 = Node(7)
n2 = Node(13)
n3 = Node(11)
n4 = Node(10)
n5 = Node(1)
n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5
n1.random = None; n2.random = n1; n3.random = n5; n4.random = n3; n5.random = n1

print(copy_random_list(n1))  # expected: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```
