---
difficulty: Hard
status: Not started
topic: [Linked List]
tags: [recursion, linked-list, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/reverse-nodes-in-k-group/"
---

### Problem
Given the head of a linked list and a positive integer k, reverse the nodes in every consecutive group of k nodes and return the modified list. If the remaining nodes at the end are fewer than k, leave them as-is. Node values must not be changed; only the node pointers may be modified.

### Constraints
- The number of nodes in the list is n
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

### Examples
```
head=[1,2,3,4,5], k=2  →  [2,1,4,3,5]
head=[1,2,3,4,5], k=3  →  [3,2,1,4,5]
```

### Next solve approach
1. Brute Force first — collect nodes in an array, reverse chunks of k, rebuild the list
2. Optimized — use a dummy head; for each group walk k steps to verify enough nodes exist, extract the group, reverse it in-place, reattach, advance the pre-pointer to the tail of the just-reversed group

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
    public ListNode reverseKGroup(ListNode head, int k) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        ListNode head1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        System.out.println(sol.reverseKGroup(head1, 2)); // expected: [2,1,4,3,5]

        ListNode head2 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        System.out.println(sol.reverseKGroup(head2, 3)); // expected: [3,2,1,4,5]
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head: ListNode, k: int) -> ListNode:
    # TODO: implement
    pass


head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(reverse_k_group(head1, 2))  # expected: [2,1,4,3,5]

head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(reverse_k_group(head2, 3))  # expected: [3,2,1,4,5]
```
