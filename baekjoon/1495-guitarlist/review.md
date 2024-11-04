# 💡  problem analysis & summary

- We have `N` songs that need to be played with a varying volume.
- Starting at volume `S`, each song has a volume adjustment value from a list `V`, allowing either an increase or decrease in volume.
- Find the maximum volume possible for the last song, within bounds of `0` and `M`.
- If no valid volume is achievable by the last song, return `1`.

# 💡  algorithm structure

- **Initialize DP Array**: Create a 2D array `dp[i][j]`, where `dp[i][j]` is `True` if volume `j` is achievable after song `i`.
- **Set Initial Volume**: Mark the starting volume `S` as achievable for the first song.
- **Volume Adjustments**: For each song and each achievable volume, mark volumes `j + V[i]` and `j - V[i]` as achievable for the next song if within bounds.
- **Find Maximum Volume**: Check achievable volumes for the last song, and find the maximum. If no volume is achievable, return `1`.

# 💡  code

```python
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
```

# 💡  time complexity

**$O(N * M)$**

- For each song (N), we potentially check every volume level up to `M`.

# 💡  cause of failure

- Changing the state and coming up with overall structure

# 💡  fix & alternative approach

- 

```python

```

# 💡  take aways & key points

-