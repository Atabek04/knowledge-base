---
difficulty: Medium
status: Not started
topic: [Greedy]
tags: [greedy, hash-table, two-pointers, string, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/partition-labels/"
---

### Problem
Given a string, split it into as many parts as possible such that each character appears in only one part. Every character that appears in a part must not appear in any other part. Return a list of the sizes of those parts in order.

### Constraints
- 1 <= s.length <= 500
- s consists of lowercase English letters

### Examples
```
"ababcbacadefegdehijhklij"  →  [9,7,8]     ("ababcbaca","defegde","hijhklij")
"eccbbbbdec"                →  [10]
```

### Next solve approach
1. Brute Force first — for each start position, expand the window until all characters in it have no occurrence outside the window
2. Optimized — greedy with last-occurrence map: record last index of each char; sweep and extend current partition end to max last index seen; close partition when i == end

---

### Java

```java
import java.util.List;

public class Solution {

    // TODO: implement
    public List<Integer> partitionLabels(String s) {
        // TODO
        return new java.util.ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.partitionLabels("ababcbacadefegdehijhklij")); // expected: [9, 7, 8]
        System.out.println(sol.partitionLabels("eccbbbbdec"));                // expected: [10]
    }
}
```

### Python

```python
def partition_labels(s: str) -> list[int]:
    # TODO: implement
    pass


print(partition_labels("ababcbacadefegdehijhklij"))  # expected: [9, 7, 8]
print(partition_labels("eccbbbbdec"))                 # expected: [10]
```
