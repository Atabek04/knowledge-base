---
difficulty: Medium
status: Not started
topic: [Linked List]
tags: [linked-list, two-pointers, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/remove-nth-node-from-end-of-list/"
---

### Problem
Given the head of a linked list and an integer n, remove the nth node counting from the end of the list and return the head. The list size sz is at least 1 and n is always a valid position. The goal is to solve it in one pass.

### Constraints
- The number of nodes in the list is sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

### Examples
```
head=[1,2,3,4,5], n=2  →  [1,2,3,5]   (removes 4, which is 2nd from end)
head=[1], n=1          →  []
head=[1,2], n=1        →  [1]
```

### Next solve approach
1. Brute Force first — find list length, then remove node at position (length - n)
2. Optimized — two-pointer gap technique: advance fast pointer n steps ahead, then move both until fast reaches the end; slow is then at the predecessor of the node to remove

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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        ListNode head1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        System.out.println(sol.removeNthFromEnd(head1, 2)); // expected: [1,2,3,5]

        System.out.println(sol.removeNthFromEnd(new ListNode(1), 1)); // expected: []

        ListNode head3 = new ListNode(1, new ListNode(2));
        System.out.println(sol.removeNthFromEnd(head3, 1)); // expected: [1]
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    # TODO: implement
    pass


head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(remove_nth_from_end(head1, 2))  # expected: [1,2,3,5]

print(remove_nth_from_end(ListNode(1), 1))  # expected: []

head3 = ListNode(1, ListNode(2))
print(remove_nth_from_end(head3, 1))  # expected: [1]
```
