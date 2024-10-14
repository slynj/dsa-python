# 💡  problem analysis & summary

- Given `n` and `m`, you need to print out `m` number of numbers between 1 and `n`.
- Repetition is allowed, so a number can appear multiple times in a sequence.
- Print the numbers in an increasing.

# 💡  algorithm structure

- Start by trying each number from 1 to `n` in each position of the sequence.
- After placing a number in the sequence, recursively fill the next position.
- Once a sequence of length `m` is formed, print it.
- Recursion!

# 💡  code

```python
# https://www.acmicpc.net/problem/15651

def backtrack(sequence, N, M):
    # Base case: if the sequence length is M, print the sequence
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    # Try every number from 1 to N
    for i in range(1, N + 1):
        sequence.append(i)  # Choose the number
        backtrack(sequence, N, M)  # Recur to form the next part of the sequence
        sequence.pop()  # Backtrack to try another number

N, M = map(int, input().split()) 
backtrack([], N, M) 

```

# 💡  time complexity

$O(N^M)$

- For each of the `m` positions in the sequence, we can choose any number from 1 to `n`.

# 💡  cause of failure

- Tried to use for loops at first, but realized the recursive approach was more accurate in this case.
- Base case was wrong at first

# 💡  fix & alternative approach

- Iterative approach

```python
def iterative_backtrack(N, M):
    stack = [[]]
    while stack:
        sequence = stack.pop()
        if len(sequence) == M:
            print(' '.join(map(str, sequence)))
        else:
            for i in range(1, N + 1):
                stack.append(sequence + [i])

N, M = map(int, input().split())
iterative_backtrack(N, M)
```

# 💡  take aways & key points

- Recursion vs. Iteration
    - While recursion is natural for backtracking, iteration (using a stack) can avoid issues like recursion depth limits and may offer better control over memory usage.