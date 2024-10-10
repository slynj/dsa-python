# 💡  problem analysis & summary

- Find the minimum number of worms needed to protect the cabbages in a field from pests. Cabbages that are adjacent (left, right, up, or down) to each other can share a worm, as the worm can move between connected cabbages.
- The input provides multiple test cases, where each test case consists of:
    - The dimensions of the field (width `M` and height `N`).
    - The number of cabbages `K` and their positions.
- The goal is to determine the number of separate groups (clusters) of connected cabbages, as each group will require at least one worm.

# 💡  algorithm structure

1. **Graph Representation:**
    - The field can be treated as a grid where each cell represents a possible cabbage position.
    - If a cell contains a cabbage, it is marked as `1`, otherwise it is `0`.
2. **Finding Connected Components:**
    - Use a search algorithm (DFS / BFS) to traverse the grid and find connected components of cabbages.
    - When a cabbage is found, start a traversal to mark all cabbages in the same cluster as visited.
    - Increment the worm count for each new traversal.
3. **Traversal Details:**
    - For each unvisited cabbage, perform DFS/BFS again to mark all connected cabbages.
    - The search should move in four possible directions (up, down, left, right).

# 💡  code

```python
#dfs

def dfs(x, y):
    stack = [(x, y)]
    field[y][x] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        current_x, current_y = stack.pop()

        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy

            if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
                stack.append((nx, ny))
                field[ny][nx] = 0

T = int(input()) 

for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    worm_count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1: 
                dfs(x, y)
                worm_count += 1 

    print(worm_count)

```

# 💡  time complexity

`O(N * M)`

- Grid Initialization: `O(N * M)`, where `N` is the height and `M` is the width of the field.
- Traversal (DFS/BFS): `O(N * M),` because each cell is visited once.

# 💡  cause of failure

- Initializing the queue at first and marking the cabbages
- Boundary errors

# 💡  fix & alternative approach

- You can also use BFS for a similar result

```python
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    field[y][x] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current_x, current_y = queue.popleft()

        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy

            if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
                queue.append((nx, ny))
                field[ny][nx] = 0

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    # create M by N
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    worm_count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1: 
                bfs(x, y) 
                worm_count += 1 

    print(worm_count)
```

# 💡  take aways & key points

- **DFS vs. BFS:** Both approaches solve the problem.
- **Grid Representation:** Converting a problem into a grid and using graph traversal algorithms like DFS/BFS is a common technique for connected component problems.
- **Boundary Checking:** Always check array bounds when navigating through grids to prevent out-of-bounds errors.