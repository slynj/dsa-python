# https://www.acmicpc.net/problem/1890

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
