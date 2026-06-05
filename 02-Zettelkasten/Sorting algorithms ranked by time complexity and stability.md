| Algorithm | Best | Avg | Worst | Stable | Space |
|-----------|------|-----|-------|--------|-------|
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | Yes | O(k) |
| Radix Sort | O(nk) | O(nk) | O(nk) | Yes | O(n+k) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | Yes | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | No | O(1) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | No | O(log n) |
| Insertion Sort | O(n) | O(n²) | O(n²) | Yes | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | No | O(1) |
| Bubble Sort | O(n) | O(n²) | O(n²) | Yes | O(1) |

**k** = range of input (Counting/Radix Sort)  
**Stable** = equal elements preserve original order

## Default Implementations

### Python
- `sorted()` and `list.sort()` → **Timsort**
  - Hybrid merge sort + insertion sort
  - Optimized for real-world data with ordered runs

### Java
- `Arrays.sort()` → **Dual-Pivot Quicksort** (primitives) or **Merge Sort** (objects)
- `Collections.sort()` → delegates to `Arrays.sort()`
