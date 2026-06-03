---
difficulty: Easy
status: Not started
topic: [Fast & Slow Pointers, Linked List]
tags: [fast-slow-pointers, linked-list, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given the head of a singly linked list, return the middle node. For an odd number of nodes there is one clear middle; for an even number of nodes, return the second of the two middle nodes.

### Constraints
- Number of nodes: 1 to 10^4
- Node values can be any integer
- Input fits in memory

### Examples
```
1→2→3→4→5→null      →  3  (middle of 5 nodes)
1→2→3→4→5→6→null    →  4  (second middle of 6 nodes)
1→2→3→4→5→6→7→null  →  4  (middle of 7 nodes)
```

### Next solve approach
1. Brute Force first — count all nodes, then traverse again to index n/2
2. Optimized (Fast & Slow Pointers) — slow moves 1 step, fast moves 2; when fast reaches the end, slow is at the middle — single pass O(n)

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
    public static ListNode findMiddle(ListNode head) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        System.out.println(findMiddle(head).value); // expected: 3

        head.next.next.next.next.next = new ListNode(6);
        System.out.println(findMiddle(head).value); // expected: 4

        head.next.next.next.next.next.next = new ListNode(7);
        System.out.println(findMiddle(head).value); // expected: 4
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def find_middle(head: ListNode) -> ListNode:
    # TODO: implement
    pass


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(find_middle(head).value)  # expected: 3

head.next.next.next.next.next = ListNode(6)
print(find_middle(head).value)  # expected: 4

head.next.next.next.next.next.next = ListNode(7)
print(find_middle(head).value)  # expected: 4
```
