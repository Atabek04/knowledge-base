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
Given the head of a linked list and a number k, reverse every consecutive group of k nodes starting from the head. If the final group has fewer than k nodes remaining, reverse those remaining nodes as well.

### Constraints
- k >= 1
- List length >= 1
- Node values are integers
- Input fits in memory

### Examples
```
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> null, k=3  →  3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7 -> null
```

### Next solve approach
1. Brute Force first — collect all values into an array, reverse each window of k, rebuild list, O(n) space
2. Optimized (In-place Reversal) — reverse each k-sized segment in-place using three pointers, track the tail of the previous segment to reconnect, O(1) space

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
    public static ListNode reverse(ListNode head, int k) {
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
        head.next.next.next.next.next.next = new ListNode(7);
        head.next.next.next.next.next.next.next = new ListNode(8);
        ListNode result = reverse(head, 3); // expected: 3 2 1 6 5 4 8 7
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


def reverse(head: 'ListNode', k: int) -> 'ListNode':
    # TODO: implement
    pass


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)

result = reverse(head, 3)  # expected: 3 2 1 6 5 4 8 7
while result:
    print(result.value, end=" ")
    result = result.next
```
