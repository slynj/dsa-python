# 💡  problem analysis & summary

- Given an `N x N` board with numbers, each number represents the distance you can jump right or down.
- Starting from the top-left corner `(0, 0)`, you must reach the bottom-right corner `(N-1, N-1)` by jumping right or down according to the number in each cell.
- A cell with a `0` indicates a dead-end, where no further moves are allowed.
- The goal is to determine the number of distinct paths from the start to the end.

# 💡  algorithm structure

- **Input Parsing**: Read `N` and the `N x N` board.
- **Dynamic Programming (DP) Setup**: Create a 2D DP array, where `dp[i][j]` represents the number of ways to reach cell `(i, j)` from the starting cell `(0, 0)`.
- **DP Transition**:
    - Start from `(0, 0)` and traverse the board.
    - For each cell `(i, j)` with a positive number, calculate the reachable cells `(i + jump, j)` (down) and `(i, j + jump)` (right) if they are within bounds.
    - Accumulate the number of ways in `dp[i + jump][j]` and `dp[i][j + jump]` based on `dp[i][j]`.
- **Result Extraction**: The answer is the value of `dp[N-1][N-1]`, which contains the total paths to the bottom-right cell.

# 💡  code

```python
import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
board = [list(map(int, data[i * N + 1:(i + 1) * N + 1])) for i in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        jump = board[i][j]
        if jump == 0:
            continue
        if j + jump < N:
            dp[i][j + jump] += dp[i][j]
        if i + jump < N:
            dp[i + jump][j] += dp[i][j]

print(dp[N - 1][N - 1])

```

# 💡  time complexity

$O(N^2)$

- Visit each cell once and update possible moves within constant time.

# 💡  cause of failure

- 

# 💡  fix & alternative approach

- 

```python

```

# 💡  take aways & key points

- DP to accumulate path counts without recalculating routes, significantly reducing redundant computations.