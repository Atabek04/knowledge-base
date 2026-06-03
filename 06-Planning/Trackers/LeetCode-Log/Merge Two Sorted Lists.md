---
difficulty: Easy
status: Not started
topic: [Linked List]
tags: [recursion, linked-list, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/merge-two-sorted-lists/"
---

### Problem
Given the heads of two sorted linked lists, merge them into a single sorted list by splicing the original nodes together (no new nodes). Both input lists are sorted in non-decreasing order. Return the head of the merged list.

### Constraints
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order

### Examples
```
list1=[1,2,4], list2=[1,3,4]  →  [1,1,2,3,4,4]
list1=[], list2=[]             →  []
list1=[], list2=[0]            →  [0]
```

### Next solve approach
1. Brute Force first — collect all node values into an array, sort, rebuild a new list
2. Optimized — dummy-head iteration: compare front nodes of each list, attach the smaller one, advance that pointer

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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode l2 = new ListNode(1, new ListNode(3, new ListNode(4)));
        System.out.println(sol.mergeTwoLists(l1, l2)); // expected: [1,1,2,3,4,4]

        System.out.println(sol.mergeTwoLists(null, null)); // expected: []

        System.out.println(sol.mergeTwoLists(null, new ListNode(0))); // expected: [0]
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    # TODO: implement
    pass


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
print(merge_two_lists(l1, l2))  # expected: [1,1,2,3,4,4]

print(merge_two_lists(None, None))  # expected: []

print(merge_two_lists(None, ListNode(0)))  # expected: [0]
```
