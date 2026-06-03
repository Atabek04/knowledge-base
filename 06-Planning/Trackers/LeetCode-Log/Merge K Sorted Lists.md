---
difficulty: Medium
status: Not started
topic: [K-way Merge, Linked List, Heap]
tags: [k-way-merge, linked-list, heap, grokking-patterns, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/merge-k-sorted-lists/"
---

### Problem
Given an array of K sorted linked lists, merge all of them into a single sorted linked list and return its head. Every input list is already sorted in ascending order; the challenge is to combine them efficiently without flattening and re-sorting all values.

### Constraints
- 1 <= K <= number of lists
- Each list is sorted in ascending order
- Total nodes across all lists fit in memory

### Examples
```
L1=[2,6,8], L2=[3,6,7], L3=[1,3,4]  →  [1,2,3,3,4,6,6,7,8]
L1=[5,8,9], L2=[1,7]                  →  [1,5,7,8,9]
```

### Next solve approach
1. Brute Force first — collect all node values into an array, sort it, rebuild linked list, O(N log N)
2. Optimized (K-way Merge) — use a min-heap of size K; always extract the smallest head and push the next node from that list, O(N log K)

---

### Java

```java
class ListNode {
    int value;
    ListNode next;
    ListNode(int value) { this.value = value; }
}

public class Solution {

    // TODO: implement
    public static ListNode merge(ListNode[] lists) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(6);
        l1.next.next = new ListNode(8);

        ListNode l2 = new ListNode(3);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(7);

        ListNode l3 = new ListNode(1);
        l3.next = new ListNode(3);
        l3.next.next = new ListNode(4);

        ListNode result = merge(new ListNode[]{l1, l2, l3}); // expected: 1 2 3 3 4 6 6 7 8

        ListNode l4 = new ListNode(5);
        l4.next = new ListNode(8);
        l4.next.next = new ListNode(9);

        ListNode l5 = new ListNode(1);
        l5.next = new ListNode(7);

        ListNode result2 = merge(new ListNode[]{l4, l5}); // expected: 1 5 7 8 9
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge(lists: list) -> ListNode:
    # TODO: implement
    pass


# Example 1
l1 = ListNode(2); l1.next = ListNode(6); l1.next.next = ListNode(8)
l2 = ListNode(3); l2.next = ListNode(6); l2.next.next = ListNode(7)
l3 = ListNode(1); l3.next = ListNode(3); l3.next.next = ListNode(4)
merge([l1, l2, l3])  # expected: 1 2 3 3 4 6 6 7 8

# Example 2
l4 = ListNode(5); l4.next = ListNode(8); l4.next.next = ListNode(9)
l5 = ListNode(1); l5.next = ListNode(7)
merge([l4, l5])  # expected: 1 5 7 8 9
```
