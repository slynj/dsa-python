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

- 

### space complexity

- 

# 💡 Problem Analysis

### summary

- given string `s`, replace max`k` amount of characters to create the longest substring consisted of the same char.

### code

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                    
                res = max(res, r - l + 1)
        return res
```

### alternative approach

```python

```

### cause of failure

### take aways & key points

- `(r - l + 1) - count > k` ensures that the number of characters to replace does not exceed `k`.

# 💡 One Line Summary

<aside>
📌

Create a set → loop through elements in the set → use 2 pointers for substring bounds → move the right pointer → check if replacements exceed `k` → if so, move the left pointer → update max substring length.

</aside>