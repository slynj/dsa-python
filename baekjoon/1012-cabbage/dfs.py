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
