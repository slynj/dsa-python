# https://www.acmicpc.net/problem/12026

import sys

def min_energy(n, blocks):
    dp = [float('inf')] * n
    dp[0] = 0 

    order = {'B': 'O', 'O': 'J', 'J': 'B'}

    for i in range(n):
        for j in range(i+1, n):
            if blocks[j] == order[blocks[i]]:
                dp[j] = min(dp[j], dp[i] + (j - i) ** 2)

    return dp[-1] if dp[-1] != float('inf') else -1

n = int(input())
blocks = input().strip()

print(min_energy(n, blocks))
