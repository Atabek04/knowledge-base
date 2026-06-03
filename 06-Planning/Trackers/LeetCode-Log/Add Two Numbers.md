---
difficulty: Medium
status: Not started
topic: [Linked List]
tags: [recursion, linked-list, math, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/add-two-numbers/"
---

### Problem
Two non-negative integers are represented as singly linked lists where the digits are stored in reverse order (least significant digit first). Add the two numbers and return the result as a linked list in the same reversed-digit format. There are no leading zeros except for the number 0 itself.

### Constraints
- The number of nodes in each linked list is in the range [1, 100]
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros

### Examples
```
l1=[2,4,3], l2=[5,6,4]              →  [7,0,8]        (342 + 465 = 807)
l1=[0], l2=[0]                      →  [0]
l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]  →  [8,9,9,9,0,0,0,1]
```

### Next solve approach
1. Brute Force first — convert each list to an integer, add them, convert result back to a linked list in reverse-digit order
2. Optimized — simulate grade-school addition node by node: track a carry, build result list digit by digit until both lists and carry are exhausted

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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // TODO
        return null;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // 342 + 465 = 807 => [7,0,8]
        ListNode l1a = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode l2a = new ListNode(5, new ListNode(6, new ListNode(4)));
        System.out.println(sol.addTwoNumbers(l1a, l2a)); // expected: [7,0,8]

        // 0 + 0 = 0
        System.out.println(sol.addTwoNumbers(new ListNode(0), new ListNode(0))); // expected: [0]

        // 9999999 + 9999 = 10009998 => [8,9,9,9,0,0,0,1]
        ListNode l1c = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9)))))));
        ListNode l2c = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))));
        System.out.println(sol.addTwoNumbers(l1c, l2c)); // expected: [8,9,9,9,0,0,0,1]
    }
}
```

### Python

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # TODO: implement
    pass


l1a = ListNode(2, ListNode(4, ListNode(3)))
l2a = ListNode(5, ListNode(6, ListNode(4)))
print(add_two_numbers(l1a, l2a))  # expected: [7,0,8]

print(add_two_numbers(ListNode(0), ListNode(0)))  # expected: [0]

l1c = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2c = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
print(add_two_numbers(l1c, l2c))  # expected: [8,9,9,9,0,0,0,1]
```
