import sys
input = sys.stdin.read

def max_volume(N, S, M, V):
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][S] = True

    for i in range(N):
        for j in range(M + 1):
            if dp[i][j]:
                if j + V[i] <= M:
                    dp[i + 1][j + V[i]] = True
                if j - V[i] >= 0:
                    dp[i + 1][j - V[i]] = True

    for vol in range(M, -1, -1):
        if dp[N][vol]:
            return vol

    return -1

data = input().split()
N, S, M = map(int, data[:3])
V = list(map(int, data[3:]))

print(max_volume(N, S, M, V))
