# 💡Approach

### edge cases

- Empty string
- Case sensitivity ⇒ everything is lower case

### brainstorm

- Bruteforce way
    - Go through one by one, have a saved string where it’s sorted, compare the sorted string of all the elements and append that to the list.

### plan

- hasmap
- key: sorted str
- val: the actual val
- Go through each element and sort them, then compare them and save them in a hashmap

### time complexity

$O(m \cdot n \cdot logn)$, where `m` is the number of strings, and `n` is the longest length str

- Sorting the string `m` times

### space complexity

$O(n)$

- new hashmap with max `n` elements
- worse case you store all key vals ⇒ `n`

# 💡 Problem Analysis

### summary

- create a list of lists where each lists are anagrams of each other

### alternative approach

```python
# https://neetcode.io/problems/anagram-groups

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        list_h = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                i = ord(c) - ord('a')
                count[i] += 1
            
            list_h[tuple(count)].append(s)
        
        return list(list_h.values())
```

- **TC:** $O(m \cdot n)$, where `m` is the number of strs, and `n` is the length of each string
- **SC:** $O(m)$, since you are creating the hasmap & list
- You can store the count of each alphabets as a key of the hasmap instead of sorting
- Better efficiency

### cause of failure

```python
# WRONG!
lst_h[a] = (lst_h.get(a, [])).append(s)
```

- This is because `.append()` modifies `lst_h[a]` but returns `None`, leading `lst_h[a]` to become `None` on the next loop.

```python
# WRONG!
count[c] += 1
```

- python doesn’t automatically take the numeric value of the `char`
- you need to use `ord(char)`

```python
# WRONG!
list_h[count].append(s)
```

- `count` is a `list`, and they are not hashable (can’t be keys) becuase they are mutable.
- you need to change them to `tuples` (immutable) so that they are hashable!
- do it by simply: `tuple(count)`

### take aways & key points

- `.append()` returns `None`
- `.values()` gives you all the values
- `defaultdict()`
    
    ```python
    res = defaultdict(list)
    ```
    
    - initializes `res` as a dictionary where each new key will automatically be assigned a new empty list `[]` as its value when accessed for the first time.
    - so you don’t need the if statement to check for the key
    - `defaultdict(int)` sets it to `0`
    - `defaultdict(bool)` sets it to `False`
    - `defaultdict(set)`, `defaultdict(float)`, etc.
- `ord(char)`
    
    ```python
    index = ord(c) - ord('a')
    ```
    
    - `ord(char)` basically returns the ascii code
    - to get the number in range 0-25, you subtract the ascii value of ‘a’ (relative position)
- `list` (mutable) is not hashable, but `tuples` (immutable) are hashable!

# 💡 One Line Summary

<aside>
📌

sort → hashmap key → convert values to list || alph counts as keys (convert to tuple) → convert values to list

</aside>