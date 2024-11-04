# 💡Approach

### edge cases

- all same numbers
- 1 number

### brainstorm

- use the `in` operator?
- pop the current index and check if the number exists in the rest of the array
- Bruteforce way :
    - $O(n^2)$ where you check each number for the rest of the elements in the list

### plan

- for each element, pop it and check if there’s any more of that element

### TC & SC

- TC : $O(n^2)$
    - $O(n)$ for each of the elements, and $O(n)$ for checking using the `in`
- SC : $O(1)$
    - no additional space required

# 💡 Problem Analysis

### summary

- return `True` if the array contains any duplicated numbers

### alternative approach

<aside>
💡

**sorting**

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
```

TC: $O(n\cdot log⁡n)$ for `.sort()`

SC: $*O(1)*$ since python uses in-place sorting

</aside>

<aside>
💡

**hash set**

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

TC: $O(n)$ goes through the elements once

SC: $O(n)$ new set `seen`

</aside>

<aside>
💡

**hash set length**

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
```

TC: $O(n)$ creates the set

SC: $O(n)$ new set

</aside>

### cause of failure

- couldn’t think of any other better options than bruteforcing

### take aways & key points

- `set(nums)` creates a new set with no duplicates