# 💡Approach

### edge cases

- empty string ⇒ not valid
- 1 character ⇒ `True`
- special chars

### brainstorm

- Bruteforce
    - for each character, check if its equal to the index of len - current index

### plan

- remove all the special characters
- for 0 - len//2, check if current index is equal to the index of len-index

### time complexity

$O(n)$

- you’re going through half of the string

### space complexity

$O(1)$

- no additional memory

# 💡 Problem Analysis

### summary

- return if the given string is a palindrome or not

### code

```python
# https://neetcode.io/problems/is-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        for c in s:
            if not (c.isalnum()): s = s.replace(c,'')

        index = len(s) - 1

        for i in range(0, len(s)//2):
            if s[i] != s[index-i]: 
                return False
        return True
```

### alternative approach

```python
# https://neetcode.io/problems/is-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        s = s.lower()

        while(l < r):
            if (s[l].isalnum() and s[r].isalnum()): 
                if s[l] != s[r]: return False
                else:
                    l += 1
                    r -= 1
            
            if not s[l].isalnum(): l += 1
            if not s[r].isalnum(): r -= 1

        return True
```

### cause of failure

- did not consider non-alphanumeric chars in the string
- did not consider uper/lower cases

### take aways & key points

- `isalnum()` : returns if char is alphanumeric
- `replace()` : replaces all the occurrences of the char in that string
- 97-122 is the range of ascii codes a-z

# 💡 One Line Summary

<aside>
📌

two pointers that are indexes starting at each end → moves towards the center → skip non-alphanumeric characters → compare case-insensitive matches

</aside>