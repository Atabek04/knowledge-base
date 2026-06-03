---
difficulty: Medium
status: Not started
topic: [Linked List]
tags: [stack, recursion, linked-list, two-pointers, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/reorder-list/"
---

### Problem
Given the head of a singly linked list L0 -> L1 -> ... -> Ln, reorder it in-place to the pattern L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ... Node values must not be changed; only the node pointers may be modified.

### Constraints
- The number of nodes in the list is in the range [1, 5 * 10^4]
- 1 <= Node.val <= 1000

### Examples
```
[1,2,3,4]    →  [1,4,2,3]
[1,2,3,4,5]  →  [1,5,2,4,3]
```

### Next solve approach
1. Brute Force first — store all nodes in an array, then use two-pointer indices to relink nodes
2. Optimized — three-step: find midpoint with slow/fast pointers, reverse second half in-place, then interleave the two halves

---

### Java

```java
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class Solution {

    // TODO: implement
    public void reorderList(ListNode head) {
        // TODO
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        ListNode head1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        sol.reorderList(head1);
        System.out.println(head1); // expected: [1,4,2,3]

        ListNode head2 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        sol.reorderList(head2);
        System.out.println(head2); // expected: [1,5,2,4,3]
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head: ListNode) -> None:
    # TODO: implement
    pass


head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reorder_list(head1)
print(head1)  # expected: [1,4,2,3]

head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reorder_list(head2)
print(head2)  # expected: [1,5,2,4,3]
```
