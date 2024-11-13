# 💡Approach

### edge cases

- all 0s ⇒ just 0s

### brainstorm

- Bruteforce
    - for every element, choose an element, and check if their `sum * -1` exists in the list excluding themselves
- 2 Ptr
    - do the ptr method, just look for `num * -1`
- sort
    - sort the array and

### plan

- For each element:
    - look for a pair that adds up to the `num * -1`

### time complexity

$O(n^2)$

- Worst case checks for all the combinations

### space complexity

$O(1)$

- No additional storage

# 💡 Problem Analysis

### summary

- give an array of numbers, return all the possible triplets that sums up to be a 0.
- all the indices must be unique

### code

```python
# https://neetcode.io/problems/three-integer-sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
# TC: O(n^2)
# SC: O(1)
```

### cause of failure

- didn’t know that there could be duplicated values that are needed

# 💡 One Line Summary

<aside>
📌

sort array → check if this is a duplicate starting value → 2 ptrs to find the sum

</aside>