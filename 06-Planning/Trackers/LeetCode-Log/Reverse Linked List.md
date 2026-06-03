---
difficulty: Easy
status: Not started
topic: [Linked List]
tags: [recursion, linked-list, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/reverse-linked-list/"
---

### Problem
Given the head of a singly linked list, return the list with its nodes in reversed order. Each node must point to the node that originally came before it. The operation must be done in-place without allocating extra nodes.

### Constraints
- The number of nodes in the list is in the range [0, 5000]
- -5000 <= Node.val <= 5000

### Examples
```
[1,2,3,4,5]  →  [5,4,3,2,1]
[1,2]        →  [2,1]
[]           →  []
```

### Next solve approach
1. Brute Force first — collect all values into an array, then rebuild the list in reverse
2. Optimized — iterative pointer reversal with prev/curr/next tracking in O(n) time, O(1) space

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
    public ListNode reverseList(ListNode head) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // [1 -> 2 -> 3 -> 4 -> 5]
        ListNode head1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        System.out.println(sol.reverseList(head1)); // expected: [5,4,3,2,1]

        // [1 -> 2]
        ListNode head2 = new ListNode(1, new ListNode(2));
        System.out.println(sol.reverseList(head2)); // expected: [2,1]

        // []
        System.out.println(sol.reverseList(null)); // expected: []
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    # TODO: implement
    pass


head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(reverse_list(head1))  # expected: [5,4,3,2,1]

head2 = ListNode(1, ListNode(2))
print(reverse_list(head2))  # expected: [2,1]

print(reverse_list(None))  # expected: []
```
