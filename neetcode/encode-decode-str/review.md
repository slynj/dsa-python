# 💡Approach

### edge cases

- empty strings
- “” string

### brainstorm

- Bruteforce
    - have a non ascii code in between

### plan

- add the length of the entire string, then length of each “words” separated by #

### time complexity

$O(n)$

- where $n$ is the max between the length of the list/length of the entire character

### space complexity

$O(n)$

- where $n$ is the the length of the “length” array

# 💡 Problem Analysis

### summary

- create `encode()` and `decode()` where:
    - `encode()`: list → str
    - `decode()`: str → list
- but the list may include numbers and spaces as 1 element

### code

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        word_length = ""
        sentence_length = 0

        for i in range(len(strs)):
            sentence += strs[i]
            if i != 0:
                word_length += "#"
            word_length += str(len(strs[i]))
            sentence_length += len(strs[i])
        
        return  sentence + word_length + "#" + str(sentence_length)

    def decode(self, s: str) -> List[str]:
        if len(s) == 2:
            return []

        length = ""

        for char in s[::-1]:
            if char != "#":
                length = s[-1] + length
                s = s[:-1]
            else:
                break
        
        sentence = s[:int(length)]
        word_length = s[int(length):-1]
        word_length = word_length.split("#")

        sentence_list = []
        index = 0

        for i in word_length:
            i = int(i)
            sentence_list.append(sentence[:i])
            sentence = sentence[i:]

        return sentence_list
```

### alternative approach

```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
```

- they appended the length of each elements in front of the string
- removed it every time they got the length, so they didn’t need the length of the whole string

### cause of failure

- at first, didnt consider that the element of the list can include strs with spaces (i split them with spaces)
- then i missed the case where empty list is given [] and empty string is given “”
    - they were diff: no str → [], empty str “” → [””]

### take aways & key points

# 💡 One Line Summary

<aside>
📌

list for the length of each elements → append in front of sentence with separation char → then when you receive the sentence, parse out the lengths first → then indexing to get the elements

</aside>
