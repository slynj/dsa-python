# 💡Approach

### edge cases

- single element arrays.
- arrays without rotation (already sorted).

### brainstorm

- Bruteforce
    - go through all the elements to find the target
- Binary Search

### plan

### time complexity

$O(log \cdot n)$

- **Pivot Search**: `O(log n)` using binary search.
- **Binary Search**: `O(log n)` in one of the two halves.
- **Overall**: `O(log n)`

### space complexity

$O(1)$

- no additional space

# 💡 Problem Analysis

### summary

- find the index of a target in a rotated, sorted array with unique elements, or return -1 if the target is not present.

### code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        
        return binary_search(pivot, len(nums) - 1)
```

### alternative approach

```python

```

### cause of failure

### take aways & key points

- **Find the Pivot**:
    - The pivot is the smallest element in the array, which separates the rotated part of the array from the original sorted array.
    - Use binary search to find this pivot.
- **Perform Binary Search on Appropriate Subarray**:
    - Once the pivot is identified:
        - If the target lies between the array indices `0` and `pivot-1`, search in the left half.
        - Otherwise, search in the right half (from `pivot` to `len(nums) - 1`).

# 💡 One Line Summary

<aside>
📌

binary search → calculate middle element → check if subarray is sorted → move to unsorted part if needed → repeat until target is found or bounds are invalid → return the result

</aside>