# 💡Approach

### edge cases

- one char ⇒ 1
- when you dont have to use all k replacements
- replacing it at diff. places result diff. lengths
- when there are 2+ diff chars

### brainstorm

- Bruteforce
    - for ever char, you check the combination of each chars?
- 2 Pointers
    - set `l`, `r`, and increment r.
    - if `r` is not the same char as `l`, check the `k` val and current k val, update max
    - move `l` if you run out of `k`, then reset

### plan

- 2 Pointers
    - set `l`, `r`, and increment r.
    - if `r` is not the same char as `l`, check the `k` val and current k val, update max
    - move `l` if you run out of `k`, then reset

### time complexity

$O(n)$

- go through one element each in the string
- there is max(), but since it’s bounded to always being 26, reduces to `O(1)`

### space complexity

$O(1)$

- since count is always length 26, reduces to `O(1)`

# 💡 Problem Analysis

### summary

- given string `s`, replace max `k` amount of characters to create the longest substring consisted of the same char.

### code

```python
# https://neetcode.io/problems/longest-repeating-substring-with-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxS = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxCount = max(count.values())

            if (r - l + 1) - maxCount <= k:
                maxS = r - l + 1
            else:
                count[s[l]] -= 1
                l += 1
                
        return maxS
```

### cause of failure

- Was doing `O(n^2)` with sliding window (no point of tdoing this)

### take aways & key points

- don’t forget about hashmap when finding the max

# 💡 One Line Summary

<aside>
📌

create a dict → add `s[l]` and `s[r]` value as key and increment the value → find the maximum occurrences of a char in dict → check if `r - l + 1 <= k` → move `l` pointer to the right → decrease the count dict value

</aside>