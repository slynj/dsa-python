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
