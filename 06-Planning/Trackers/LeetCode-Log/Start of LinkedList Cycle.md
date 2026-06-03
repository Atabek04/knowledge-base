---
difficulty: Medium
status: Not started
topic: [Fast & Slow Pointers, Linked List]
tags: [fast-slow-pointers, linked-list, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given the head of a singly linked list that is guaranteed to contain a cycle, find and return the node where the cycle begins. The cycle start is the first node that would be revisited during an infinite traversal.

### Constraints
- The list is guaranteed to have a cycle
- Number of nodes: 1 to 10^4
- Node values can be any integer

### Examples
```
1→2→3→4→5→6→(back to 3)   →  3  (cycle starts at node with value 3)
1→2→3→4→5→6→(back to 4)   →  4  (cycle starts at node with value 4)
1→2→3→4→5→6→(back to 1)   →  1  (cycle starts at node with value 1)
```

### Next solve approach
1. Brute Force first — store visited nodes in a HashSet; return the first node seen twice
2. Optimized (Fast & Slow Pointers) — find meeting point with fast/slow; then move one pointer to head and advance both one step at a time — they meet at the cycle start

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
    public static ListNode findCycleStart(ListNode head) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        head.next.next.next.next.next = new ListNode(6);

        head.next.next.next.next.next.next = head.next.next; // cycle at node 3
        System.out.println(findCycleStart(head).value); // expected: 3

        head.next.next.next.next.next.next = head.next.next.next; // cycle at node 4
        System.out.println(findCycleStart(head).value); // expected: 4

        head.next.next.next.next.next.next = head; // cycle at node 1
        System.out.println(findCycleStart(head).value); // expected: 1
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def find_cycle_start(head: ListNode) -> ListNode:
    # TODO: implement
    pass


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

head.next.next.next.next.next.next = head.next.next  # cycle at node 3
print(find_cycle_start(head).value)  # expected: 3

head.next.next.next.next.next.next = head.next.next.next  # cycle at node 4
print(find_cycle_start(head).value)  # expected: 4

head.next.next.next.next.next.next = head  # cycle at node 1
print(find_cycle_start(head).value)  # expected: 1
```
