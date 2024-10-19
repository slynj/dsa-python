# 💡  problem analysis & summary

- The problem asks for the smallest "good sequence" of length `N`, where the sequence only consists of the numbers 1, 2, and 3. A "good sequence" is defined as one that does not contain any two adjacent subsequences of the same length.
- For example, a sequence like `1213121` is good because no two adjacent subsequences are identical. However, `123123` is a bad sequence because the two subsequences `123` are adjacent and identical.
- The goal is to find the lexicographically smallest such sequence.

---

- **좋은 수열**: 인접한 부분 수열이 같지 않은 수열.
- **나쁜 수열**: 인접한 부분 수열이 동일한 수열.
- **임의의 길이를 가진 인접한 두 개의 부분 수열이 동일하면 안됨**. 나쁜 수열 = 어떤 길이의 부분 수열이든 동일한 두 부분 수열이 인접해 있는 경우.

# 💡  algorithm structure

- **Backtracking** is used to generate sequences incrementally and to check if they are "good."
- For each position in the sequence, we attempt to place a number (1, 2, or 3). We then check if the sequence remains a "good sequence" after adding the number.
- If the sequence is good, we proceed to the next position; otherwise, we backtrack and try a different number.
- The process continues until we generate a sequence of length `N`, at which point the first valid sequence is printed.

# 💡  code

```python
# https://www.acmicpc.net/problem/2661

def good_sequence(seq):
    length = len(seq)

    for i in range(1, (length // 2) + 1):
        if seq[-i:] == seq[-2*i:-i]:
            return False
    
    return True

def backtrack(seq, N):
    if len(seq) == N:
        print(seq)
        return True
    
    for num in "123":
        if good_sequence(seq + num):
            if backtrack(seq + num, N):
                return True

    return False

N = int(input())
backtrack("", N)
```

# 💡  time complexity

$O(3^n)$

- **Worst Case:** every possible combination of 1, 2, and 3 for a sequence of length `N`.
- There are 3 choices for each position in the sequence, so the time complexity is `O(3^N)`.

# 💡  cause of failure

- `seq[-i:] == seq[-2*i:-i]`
- Was not able to come up with this to check for the good sequence.
- Evaluating this was the main part of this question.
- This checks if the last `i` characters of the sequence are equal to the `i` characters before them, which would indicate a bad sequence.
- Also had a return `True` at the wrong place which made the function not print anything

# 💡  fix & alternative approach

```python
seq[-i:] == seq[-2*i:-i]
```

# 💡  take aways & key points

- **String slicing** in Python is highly efficient and very useful for solving problems involving substrings and comparisons.

```python
string[start:stop:step]
```

- **`start`**: The index at which to start the slice (inclusive).
- **`stop`**: The index at which to stop the slice (exclusive).
- **`step`**: The interval between characters in the slice. The default is `1`.

- If `start` or `stop` is not provided, the defaults are:
    - `start` defaults to the beginning of the string (index `0`).
    - `stop` defaults to the end of the string (length of the string).
    - `step` defaults to `1`.

```python
s[:]  # The whole string (equivalent to s[0:len(s)])
s[:5]  # First 5 characters
s[5:]  # From index 5 to the end
s[::-1]  # Reverse the string
```

```python
seq[-i:] == seq[-2*i:-i]  # Compare the last i characters with the preceding i characters
```