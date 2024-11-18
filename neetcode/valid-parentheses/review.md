# 💡Approach

### edge cases

- different types being closed ⇒ `False`
- odd number ⇒ `False`
- `"()[]{}"` ⇒ should be `True`

### brainstorm

- Bruteforce
    - check each element and the corresponding index that ends up to the `len - 1`
    - just keep on removing the valid parentheses
        
        ```python
        class Solution:
            def isValid(self, s: str) -> bool:
                while '()' in s or '{}' in s or '[]' in s:
                    s = s.replace('()', '')
                    s = s.replace('{}', '')
                    s = s.replace('[]', '')
                return s == ''
        ```
        

### plan

- use stack data structure to store the opening of the parentheses and pop each element when the closing of the parentheses is found

### time complexity

$O(n)$

- goes through each char in str

### space complexity

$O(n)$

- creates a stack that stores all the values worst case

# 💡 Problem Analysis

### summary

- given a string `s`, return if the string has a valid pair of parentheses.
- valid parentheses is parentheses that opens and closes with the same type

### wrong code

```python
# WRONG!

# https://neetcode.io/problems/validate-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        brackets = {'(' : ')',
                    '[' : ']',
                    '{' : '}' }

        lenS = len(s)

        for i in range(len(s)//2):
            if s[i] in brackets and brackets[s[i]] != s[lenS - i - 1]: return False
        
        return True
```

### correct implementation

```python
# https://neetcode.io/problems/validate-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        b = {')' : '(',
             '}' : '{',
             ']' : '['}
        
        for c in s:
            if c in b:
                if stack and stack[-1] == b[c]: stack.pop()
                else: return False
            else:
                stack.append(c)
        
        return True if not stack else False
```

### cause of failure

- only considered the case where they are nested in order (`[({})]`)
- did not consider the case like `(){}[]`

### take aways & key points

- make the keys the closed brackets to easily check if the latest char is the opening of the parentheses
- pop the last element if it is valid

# 💡 One Line Summary

<aside>
📌

create a stack → create a dict with closed parentheses key → for each character, if the last element on stack corresponds to the value of the key, it is valid thus pop → if not return False → otherwise if the char is opening, append to stack → return if the stack is empty, ie all valid.

</aside>