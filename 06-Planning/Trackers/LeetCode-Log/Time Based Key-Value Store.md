---
difficulty: Medium
status: Not started
topic: [Binary Search]
tags: [design, hash-table, string, binary-search, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/time-based-key-value-store/"
---

### Problem
Design a key-value store that supports storing multiple values for the same key at different timestamps. The set operation records a (key, value, timestamp) triple. The get operation retrieves the value associated with the largest stored timestamp that is less than or equal to the queried timestamp; if no such value exists it returns an empty string. All set timestamps are strictly increasing.

### Constraints
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits
- 1 <= timestamp <= 10^7
- All timestamps passed to set are strictly increasing
- At most 2 * 10^5 calls will be made to set and get

### Examples
```
TimeMap() → null
set("foo","bar",1) → null
get("foo",1)       → "bar"
get("foo",3)       → "bar"    (no value at t=2 or t=3, so falls back to t=1)
set("foo","bar2",4) → null
get("foo",4)       → "bar2"
get("foo",5)       → "bar2"
```

### Next solve approach
1. Brute Force first — store all (timestamp, value) pairs per key, scan backwards on get
2. Optimized — HashMap<key, list of (timestamp,value)>; binary search the list on get for largest timestamp <= query

---

### Java

```java
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class Solution {

    static class TimeMap {

        // TODO: implement
        public TimeMap() {
            // TODO
        }

        public void set(String key, String value, int timestamp) {
            // TODO
        }

        public String get(String key, int timestamp) {
            // TODO
            return "";
        }
    }

    public static void main(String[] args) {
        TimeMap timeMap = new TimeMap();
        timeMap.set("foo", "bar", 1);
        System.out.println(timeMap.get("foo", 1));  // expected: bar
        System.out.println(timeMap.get("foo", 3));  // expected: bar
        timeMap.set("foo", "bar2", 4);
        System.out.println(timeMap.get("foo", 4));  // expected: bar2
        System.out.println(timeMap.get("foo", 5));  // expected: bar2
    }
}
```

### Python

```python
class TimeMap:
    def __init__(self):
        # TODO: implement
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        # TODO
        pass

    def get(self, key: str, timestamp: int) -> str:
        # TODO
        return ""


time_map = TimeMap()
time_map.set("foo", "bar", 1)
print(time_map.get("foo", 1))  # expected: bar
print(time_map.get("foo", 3))  # expected: bar
time_map.set("foo", "bar2", 4)
print(time_map.get("foo", 4))  # expected: bar2
print(time_map.get("foo", 5))  # expected: bar2
```
