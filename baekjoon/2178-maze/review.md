# 💡  problem analysis & summary

- We are tasked with finding the shortest path through a maze that is represented as a grid.
- Each cell in the grid either allows movement (represented by 1) or blocks movement (represented by 0).
- The goal is to determine the minimum number of steps required to move from the start point (top-left corner) to the end point (bottom-right corner) while only moving to adjacent cells that allow movement.

# 💡  algorithm structure

- BFS to traverse the maze, as BFS is ideal for finding the shortest path in an unweighted grid.
- Starting from the top-left corner, we explore all possible moves (up, down, left, right), marking each cell with the number of steps it takes to reach it.
- Once we reach the bottom-right corner, the number stored in that cell will be the minimum number of steps needed.

# 💡  code

```python
# https://www.acmicpc.net/problem/2178

from collections import deque

def bfs(maze, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    
    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

print(bfs(maze, n, m))
```

# 💡  time complexity

$O(N * M)$

- The time complexity is **`O(N * M)`**, where N is the number of rows and M is the number of columns in the maze. This is because each cell is processed exactly once during the BFS traversal.

# 💡  cause of failure

- Failing to check the boundaries

# 💡  fix & alternative approach

- Ensure that boundary checks are properly applied

# 💡  take aways & key points

- Ensure boundary conditions are handled correctly!
- BFS ensures that the first time a cell is reached, it is with the minimum number of steps, making it an optimal solution for this problem.