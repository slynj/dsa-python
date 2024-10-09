# 💡  problem analysis & summary

- The problem is to find and label connected components of houses (`1`) on a given `N x N` grid map. Each connected component is defined as a group of houses that are connected vertically or horizontally. Diagonal connections are not considered.
- The task is to count the total number of connected components (complexes) and then list the size of each complex in ascending order.

# 💡  algorithm structure

### Thought Process :

- **Choosing DFS**: Since we need to explore connected components and the grid size is relatively small (at most `25 x 25`, DFS is suitable. We can use a stack to avoid recursion depth issues.
- **Tracking Visits**: Marking cells as '0' during DFS allows us to track visited cells without using a separate visited array.
- **Sorting Component Sizes**: Sorting helps in generating the required output format in ascending order.
- Use DFS to explore each connected component.
    - If a cell is marked as '1', initiate a DFS from that cell to find all connected '1's and count the size of the component.
    - Mark the cells visited during the DFS to avoid re-visiting.
- **Tracking the Sizes of Components**:
    - For each DFS, count the number of cells in the current connected component.
    - Store these counts in a list.
- **Sorting and Output**:
    - Sort the list of component sizes in ascending order.
    - Output the number of components and each component size.

# 💡  code

```python
# https://www.acmicpc.net/problem/2667

n = int(input().strip())
map_data = [list(map(int, input().strip())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    stack = [(x, y)]
    map_data[x][y] = 0
    count = 1
    
    while stack:
        cx, cy = stack.pop()
        # check 4 directions
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # new position is within bounds and is a house:
            if 0 <= nx < n and 0 <= ny < n and map_data[nx][ny] == 1:
                map_data[nx][ny] = 0
                count += 1
                # position to the stack
                stack.append((nx, ny))
    
    return count

# store the size of each complex
complex_sizes = []

# go through each cell in the map
for i in range(n):
    for j in range(n):
        # house -> perform DFS to find the size of the complex
        if map_data[i][j] == 1:
            complex_sizes.append(dfs(i, j))

complex_sizes.sort()

print(len(complex_sizes))
for size in complex_sizes:
    print(size)
```

# 💡  time complexity

`O(N^2)`

- We potentially visit every cell in the grid once, resulting in `O(N^2)` operations for the DFS.
- Sorting the list of complex sizes has a time complexity of `O(KlogK)`, where K is the number of components found. Since K≤N2, the sorting does not dominate the overall time complexity.

# 💡  cause of failure

- Not marking visited nodes could lead to counting the same component multiple times.
- Boundary conditions!

# 💡  fix & alternative approach

- Mark a cell as visited immediately after including it in the DFS stack.

- You could also use BFS:

```python
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    map_data[x][y] = 0
    count = 1
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and map_data[nx][ny] == 1:
                map_data[nx][ny] = 0
                count += 1
                queue.append((nx, ny))
                
    return count
```

# 💡  take aways & key points

- Understanding DFS and BFS is essential for solving problems involving connected components in grids.