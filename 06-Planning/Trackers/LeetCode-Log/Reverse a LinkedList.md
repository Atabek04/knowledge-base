---
difficulty: Easy
status: Not started
topic: [In-place Reversal of a LinkedList, Linked List]
tags: [in-place-reversal, linked-list, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given the head of a singly linked list, reverse the entire list in-place and return the new head. Each node's `next` pointer must point to its previous neighbor, and the original head becomes the new tail pointing to null.

### Constraints
- List length >= 1
- Node values are integers
- Input fits in memory

### Examples
```
2 -> 4 -> 6 -> 8 -> 10 -> null  →  10 -> 8 -> 6 -> 4 -> 2 -> null
```

### Next solve approach
1. Brute Force first — collect all node values into an array, rebuild the list in reverse order, O(n) space
2. Optimized (In-place Reversal) — walk with three pointers (prev, curr, next), redirect each node's pointer as you go, O(1) space

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
    public static ListNode reverse(ListNode head) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(2);
        head.next = new ListNode(4);
        head.next.next = new ListNode(6);
        head.next.next.next = new ListNode(8);
        head.next.next.next.next = new ListNode(10);
        ListNode result = reverse(head); // expected: 10 8 6 4 2
        while (result != null) {
            System.out.print(result.value + " ");
            result = result.next;
        }
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None


def reverse(head: 'ListNode') -> 'ListNode':
    # TODO: implement
    pass


head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(6)
head.next.next.next = ListNode(8)
head.next.next.next.next = ListNode(10)

result = reverse(head)  # expected: 10 8 6 4 2
while result:
    print(result.value, end=" ")
    result = result.next
```
