---
difficulty: Easy
status: Not started
topic: [Fast & Slow Pointers, Linked List]
tags: [fast-slow-pointers, linked-list, grokking-patterns, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/linked-list-cycle/"
---

### Problem
Given the head of a singly linked list, determine whether the list contains a cycle. A cycle exists when a node's `next` pointer points back to a previously visited node, causing traversal to loop forever instead of reaching `null`.

### Constraints
- Number of nodes: 0 to 10^4
- Node values can be any integer
- Input fits in memory

### Examples
```
1→2→3→4→5→6→null          →  false  (no cycle)
1→2→3→4→5→6→(back to 3)   →  true   (cycle at node 3)
1→2→3→4→5→6→(back to 4)   →  true   (cycle at node 4)
```

### Next solve approach
1. Brute Force first — store visited nodes in a HashSet, detect revisit in O(n) space
2. Optimized (Fast & Slow Pointers) — slow moves 1 step, fast moves 2; if they ever meet, a cycle exists — O(1) space

---

### Java

```java
class ListNode {
    int value = 0;
    ListNode next;
    ListNode(int value) { this.value = value; }
}

public class Solution {

    // TODO: implement
    public static boolean hasCycle(ListNode head) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        head.next.next.next.next.next = new ListNode(6);
        System.out.println(hasCycle(head)); // expected: false

        head.next.next.next.next.next.next = head.next.next; // cycle at node 3
        System.out.println(hasCycle(head)); // expected: true

        head.next.next.next.next.next.next = head.next.next.next; // cycle at node 4
        System.out.println(hasCycle(head)); // expected: true
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def has_cycle(head: ListNode) -> bool:
    # TODO: implement
    pass


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
print(has_cycle(head))  # expected: False

head.next.next.next.next.next.next = head.next.next  # cycle at node 3
print(has_cycle(head))  # expected: True

head.next.next.next.next.next.next = head.next.next.next  # cycle at node 4
print(has_cycle(head))  # expected: True
```
