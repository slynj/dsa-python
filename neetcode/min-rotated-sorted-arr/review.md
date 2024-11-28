# 💡Approach

### edge cases

- 

### brainstorm

- Bruteforce
    - Go through each things
- Binary Search

### plan

### time complexity

$O(log \cdot n)$

- Binary search

### space complexity

$O(1)$

- No extra space

# 💡 Problem Analysis

### summary

- Given a rotated sorted array of unique integers, originally sorted in ascending order but rotated between 1 and `n` times. Find the minimum element in this array.

### code

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
```

### alternative approach

`binary search lower bound`

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
```

### cause of failure

### take aways & key points

- If the segment `[left, right]` is sorted (`nums[left] < nums[right]`), the smallest element is at `nums[left]`. Update the result and break out of the loop.
- Otherwise, compute `mid` to divide the array into two parts.
- Update the result by comparing `nums[mid]` to the current result.
- Decide the next range:
    - If `nums[mid] >= nums[left]`, it means the left part is sorted, so search the right part (`left = mid + 1`).
    - Else, search the left part (`right = mid - 1`).

# 💡 One Line Summary

<aside>
📌

binary search → initialize left and right pointers → calculate the middle element → check if the subarray is sorted or rotated → if sorted, move to the unsorted part (adjust left or right) → repeat until the smallest element is found → return the result

</aside>