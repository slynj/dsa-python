# 💡Approach

### edge cases

- what if there are more than one unique sets of indices? ⇒ always 1 solution
- empty list or 1 element ⇒ always 2+ elements in the given list

### brainstorm

- Bruteforce
    - for each element, check the rest of the elements to check if they add up to the target
    - if they do, return current index’s list
- We should probably use the fact that it is sorted in a non-decreasing order
- List and in
    - check if target - current number is in the list

### plan

- check if target - current number is in the list

### time complexity

$O(n)$

- Worst case, you would be checking for all the numbers

### space complexity

$O(1)$

- No additional space other than the returning list is required

# 💡 Problem Analysis

### summary

- given a sorted list, return the indices of a pair of number that adds up to a given target

### code

```python
# https://neetcode.io/problems/two-integer-sum-ii
          
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         for n in numbers:
            if (target - n) in numbers:
                return [numbers.index(n) + 1, numbers.index(target-n) + 1]
```

### alternative approach

`2 ptrs`

- have 2 ptrs that points at each ends
- since the list is in non-decreasing order:
    - if the current sum is smaller than the target, move the left pointer + 1
    - if the current sum is bigger than the target, move the right pointer - 1
- otherwise, return empty list

```python
# https://neetcode.io/problems/two-integer-sum-ii

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr = numbers[l] + numbers[r]

            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return []

# TC: O(n)
# SC: O(1)
```

### cause of failure

N/A

### take aways & key points

- `index()` : returns the index of the number of that element

# 💡 One Line Summary

<aside>
📌

for each element find the index of the target-cur value → return the index list || have 2 pointers start at each end → if current sum is smaller move the left ptr, if current sum is bigger move right ptr → return the ptrs in list

</aside>