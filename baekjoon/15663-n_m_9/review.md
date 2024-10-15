# 💡  problem analysis & summary

- Generate all possible sequences of length `M` by choosing elements from a list of `N` natural numbers.
- The key requirements:
    - The sequence must be in lexicographical order (hence we sort the list initially).
    - Duplicate sequences must not be printed (even though the input list may contain duplicates).
    - The sequence generation should be done using backtracking to explore all possible valid combinations.

# 💡  algorithm structure

- **Sorting the Input**: First, the input list is sorted to ensure that the sequences are generated in lexicographical order.
- **Backtracking**:
    - The `backtrack` function takes the current sequence (`path`), a boolean list to track visited elements (`visited`), and recursively builds all valid sequences.
    - If the length of the `path` equals `M`, the sequence is printed. **(base case)**
    - The `prev` variable ensures that duplicates are not used in the same recursive depth (so no repeated sequences are printed).
- **Visited Check**: The `visited` array ensures that each element is used only once per sequence.
- **Duplicate Check**: The `prev` variable helps skip over duplicate values in the same level of recursion, ensuring no redundant sequences are generated.

# 💡  code

```python
def backtrack(sequence, path, N, M, visited):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return

    prev = -1
    for i in range(N):
        if not visited[i] and sequence[i] != prev:
            visited[i] = True
            backtrack(sequence, path + [sequence[i]], N, M, visited)
            visited[i] = False
            prev = sequence[i]

N, M = map(int, input().split())
sequence = list(map(int, input().split()))

sequence.sort()
visited = [False] * N
backtrack(sequence, [], N, M, visited)
```

# 💡  time complexity

$O(N^M)$

- Backtracking goes into all the combinations of length `M` for a list of `N` numbers

# 💡  cause of failure

- Was unable to figure out a solution where I check for the duplicates
- Usage of `prev` and `visited` !

# 💡  fix & alternative approach

- You can avoid unnecesasry recursive calls by checking the condition `seequence[i] == seqnece[i-1]`
- This has the time complexity of $O(N \enspace log N)$, where $N$is the number of elements

```python
def backtrack(sequence, path, N, M, used):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return

    for i in range(N):
        if not used[i]:
            if i > 0 and sequence[i] == sequence[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            backtrack(sequence, path + [sequence[i]], N, M, used)
            used[i] = False

N, M = map(int, input().split())
sequence = list(map(int, input().split()))

sequence.sort() 
used = [False] * N
backtrack(sequence, [], N, M, used)
```

# 💡  take aways & key points

- When you do `lst.sort()`, it returns `None` so you shouldn’t put it in the parameter (`backtrack(sequence.sort(), [], N, M, ...)` will return `None` for sequence!)
- When tracking is needed, use another variable and data struct.