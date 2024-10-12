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
