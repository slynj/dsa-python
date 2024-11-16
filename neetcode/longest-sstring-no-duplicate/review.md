# 💡Approach

### edge cases

- all same ⇒ 1

### brainstorm

- Bruteforce
    - check every substring and have a variable that stores the max. length
    - substring created by stopping when same char is met

### plan

- Sliding Window
    - have `l` and `r` and a set that stores the element of the strings
    - increment r, and when `s[r]`  exists in the string, remove the `s[1]` until there are no duplicates
    - this would give you a substring with no duplicates
    - update max. length

### time complexity

$O(n)$

- Since we are going through the set, it is O(n)

### space complexity

$O(n)$

- Since we are creating a set

# 💡 Problem Analysis

### summary

- return the maximum length of the substring where there are no duplicates

### code

```python
# https://neetcode.io/problems/longest-substring-without-duplicates

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charS = set()
        l = 0
        lenS = 0

        for r in range(len(s)):
            while s[r] in charS:
                charS.remove(s[l])
                l += 1
            charS.add(s[r])
            lenS = max(lenS, r - l + 1)
        
        return lenS
```

### cause of failure

N/A

### take aways & key points

- You don’t have to worry about not checking all the combinations because every r, you will update the lenS

# 💡 One Line Summary

<aside>
📌

create a set → 2 ptrs for each ends of the substr → move r → check if there are duplicates by checking the set → if there is a duplicate move the left ptr until it doesn’t contain a duplicate → update max length

</aside>