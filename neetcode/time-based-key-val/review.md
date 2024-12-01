# 💡Approach

### edge cases

### brainstorm

- Bruteforce
    - search thorugh all the time stamps
- Binary Search with Array

### plan

### time complexity

$O(logn)$

- **`O(1)` for `*set*()` and `*O*(*n*)` for `*get*()`.**

### space complexity

$O(m \cdot n)$

- m: Number of unique keys.
- n: Average number of timestamps stored per key.

# 💡 Problem Analysis

### summary

### code

```python
class TimeMap:

    def __init__(self):
        self.keyStore = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
```

### alternative approach

```python

```

### cause of failure

### take aways & key points

- Using a dictionary to group timestamps by keys ensures efficient storage and lookup.

- **Initialize a `TimeMap` class**:
    - Use a dictionary (`keyStore`) to store lists of `[value, timestamp]`.
- **Implement `set`**:
    - Add `[value, timestamp]` to the list corresponding to the `key`.
- **Implement `get`**:
    - Use binary search on the list of timestamps to find the most recent timestamp <= the requested timestamp.

# 💡 One Line Summary

<aside>
📌

binary search → store key-value pairs with timestamps → calculate middle element → check if timestamp ≤ target → update result and adjust left or right pointers → repeat until bounds are invalid → return the most recent value or empty string

</aside>