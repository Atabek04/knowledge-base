---
difficulty: Medium
status: Not started
topic: [Linked List]
tags: [design, hash-table, linked-list, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/lru-cache/"
---

### Problem
Design a data structure implementing a Least Recently Used cache. It supports get and put operations, both running in O(1) average time. When the cache exceeds its capacity after a put, it must evict the least recently used key. Any access (get or put) counts as a "use" and moves that key to most-recently-used position.

### Constraints
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put

### Examples
```
LRUCache(2)
put(1,1) → cache={1=1}
put(2,2) → cache={1=1, 2=2}
get(1)   → 1
put(3,3) → evicts key 2, cache={1=1, 3=3}
get(2)   → -1   (evicted)
put(4,4) → evicts key 1, cache={4=4, 3=3}
get(1)   → -1   (evicted)
get(3)   → 3
get(4)   → 4
```

### Next solve approach
1. Brute Force first — use a list to track insertion order, scan on each get/put to find LRU (O(n) per operation)
2. Optimized — HashMap + doubly linked list: O(1) lookup via map, O(1) move-to-front/evict-tail via DLL with sentinel head/tail nodes

---

### Java

```java
import java.util.HashMap;
import java.util.Map;

public class Solution {

    static class Node {
        int key, val;
        Node prev, next;
        Node() {}
        Node(int key, int val) { this.key = key; this.val = val; }
    }

    static class LRUCache {
        private int size;
        private int capacity;
        private Node head = new Node();
        private Node tail = new Node();
        private Map<Integer, Node> cache = new HashMap<>();

        // TODO: implement
        public LRUCache(int capacity) {
            // TODO
        }

        public int get(int key) {
            // TODO
            return 0;
        }

        public void put(int key, int value) {
            // TODO
        }
    }

    public static void main(String[] args) {
        LRUCache lru = new LRUCache(2);
        lru.put(1, 1);           // expected: null
        lru.put(2, 2);           // expected: null
        System.out.println(lru.get(1));    // expected: 1
        lru.put(3, 3);           // expected: null (evicts key 2)
        System.out.println(lru.get(2));    // expected: -1
        lru.put(4, 4);           // expected: null (evicts key 1)
        System.out.println(lru.get(1));    // expected: -1
        System.out.println(lru.get(3));    // expected: 3
        System.out.println(lru.get(4));    // expected: 4
    }
}
```

### Python

```python
class LRUCache:
    def __init__(self, capacity: int):
        # TODO: implement
        pass

    def get(self, key: int) -> int:
        # TODO: implement
        pass

    def put(self, key: int, value: int) -> None:
        # TODO: implement
        pass


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))   # expected: 1
lru.put(3, 3)
print(lru.get(2))   # expected: -1
lru.put(4, 4)
print(lru.get(1))   # expected: -1
print(lru.get(3))   # expected: 3
print(lru.get(4))   # expected: 4
```
