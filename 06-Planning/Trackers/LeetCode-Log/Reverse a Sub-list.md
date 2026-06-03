---
difficulty: Medium
status: Not started
topic: [In-place Reversal of a LinkedList, Linked List]
tags: [in-place-reversal, linked-list, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given the head of a singly linked list and two 1-based positions p and q, reverse only the nodes between position p and position q (inclusive) and return the head of the modified list. Nodes outside the range stay in their original order.

### Constraints
- 1 <= p <= q <= length of list
- List length >= 1
- Node values are integers

### Examples
```
1 -> 2 -> 3 -> 4 -> 5 -> null, p=2, q=4  →  1 -> 4 -> 3 -> 2 -> 5 -> null
```

### Next solve approach
1. Brute Force first — extract nodes p..q into an array, reverse the array, splice back into the list, O(n) space
2. Optimized (In-place Reversal) — walk to node p-1, then reverse nodes p..q in-place using three pointers, reconnect the ends, O(1) space

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
    public static ListNode reverse(ListNode head, int p, int q) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        ListNode result = reverse(head, 2, 4); // expected: 1 4 3 2 5
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


def reverse(head: 'ListNode', p: int, q: int) -> 'ListNode':
    # TODO: implement
    pass


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = reverse(head, 2, 4)  # expected: 1 4 3 2 5
while result:
    print(result.value, end=" ")
    result = result.next
```
