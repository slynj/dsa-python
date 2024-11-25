# 💡Approach

### edge cases

### brainstorm

- Bruteforce

### plan

### time complexity

$O(n \cdot logn)$

- 

### space complexity

$O(1)$

- 

# 💡 Problem Analysis

### summary

### code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            i = l + ((r - l) // 2)

            if nums[i] < target: r = i - 1
            elif nums[i] > target: l = i + 1
            else: return i

        return -1
```

### alternative approach

`bisect`

```python
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
```

### cause of failure

- `(l + r) // 2` can lead to overflow

### take aways & key points

# 💡 One Line Summary

<aside>
📌

reduce r if target is smaller, increase l if target is larger → loop while l ≤ r

</aside>