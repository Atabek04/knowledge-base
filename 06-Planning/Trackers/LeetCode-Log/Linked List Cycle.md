---
difficulty: Easy
status: Not started
topic: [Fast & Slow Pointers, Linked List]
tags: [fast-slow-pointers, linked-list, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/linked-list-cycle/"
---

### Problem
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle exists if some node can be reached again by continuously following the `next` pointer.

### Constraints
- The number of nodes is in the range [0, 10⁴]
- -10⁵ <= Node.val <= 10⁵
- `pos` is -1 or a valid index in the linked list (not a parameter — just describes the cycle tail)

### Examples
```
[3,2,0,-4], tail connects to index 1  →  true
[1,2], tail connects to index 0        →  true
[1], no cycle                          →  false
```

### Next solve approach
1. Brute Force — use a HashSet; store visited nodes, return true if a node is seen twice, O(n) time O(n) space
2. Optimized (Fast & Slow) — two pointers: slow moves 1 step, fast moves 2 steps; if they meet → cycle; if fast reaches null → no cycle, O(n) time O(1) space

---

### Java

```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

public class Solution {

    // TODO: implement
    public static boolean hasCycle(ListNode head) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        ListNode n1 = new ListNode(3);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(0);
        ListNode n4 = new ListNode(-4);
        n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2; // cycle at index 1
        System.out.println(hasCycle(n1)); // expected: true

        ListNode a = new ListNode(1);
        System.out.println(hasCycle(a)); // expected: false
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(head: ListNode) -> bool:
    # TODO: implement
    pass


n1 = ListNode(3); n2 = ListNode(2); n3 = ListNode(0); n4 = ListNode(-4)
n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
print(hasCycle(n1))  # expected: True

print(hasCycle(ListNode(1)))  # expected: False
```
