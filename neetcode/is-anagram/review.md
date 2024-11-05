# 💡Approach

### edge cases

- diff string length check ⇒ false right away
- empty string ⇒ true

### brainstorm

- Bruteforce Method:
    - for each character in `s`, check if the character exists in `t`
    - pop the character that has already been checked to also check the number of chars
- You can make it into a list and sort it, then compare
- You can use hashing somehow?

### plan

- sort the string, then compare them

### time complexity

$O(n \cdot logn)$

- Sorting takes `O(n * logn)`
- Comparing takes `O(n)`

### space complexity

$O(n)$ or $O(1)$ 

- Sorting creates new list taking `O(n)` / `O(1)` space
- Depends on the interviewer, some just assumes that it’s `O(1)`

# 💡 Problem Analysis

### summary

- given string `s` and `t`, return if they’re anagrams of each other
- ie: return if the have the same number of chars

### alternative approach

`#hashmap`

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        
        hashS, hashT = {}, {}

        for i in range(len(s)):
            # .get() to give default value when its init
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        for h in (hashS):
            if hashS[h] != hashT.get(h, 0): return False
        
        return True
```

### failures during alternative approach

```python
# not a correct syntax:
hashS, hashT = {}

# correct:
hashS, hashT = {}, {}
```

```python
# can lead to errors when something that exists in hashS doesn't in hashT
for h in (hashS):
	if hashS[h] != hashT[h]: return False
	
# soln 1: use the .get() and set default values to be 0
for h in (hashS):
	if hashS[h] != hashT.get(h, 0): return False
	
# soln 2: you can just direct compare (may not be allowed sometimes)
return hashS == hashT
```

### take aways & key points

<aside>
💡

`sorted()` vs `.sort()`

- `sort()` : sorts the list in-place, mutating the list, returning `None`
- `sorted()` :  returns a new sorted list leaving the original list unchanged
</aside>

<aside>
💡

`hashmap` vs `hashtable`

- **hashmap**
    - basically a dictionary in python
    - allows `Null` keys and values
- **hashtable**
    - not a distinct type in python
    - does not allow `Null` keys or tables
</aside>

# 💡 One Line Summary

<aside>
📌

create list → sort → compare || create a hashmap where keys are alph, vals are # of alph → compare

</aside>