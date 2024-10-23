# 💡  problem analysis & summary

- We need to find the maximum length of a LAN cable that can be cut from `K` existing cables such that at least `N` cables can be produced.
- The goal is to ensure that all cables are of equal length, and no leftover cable segments are used.
- The challenge is to maximize the length of each new cable while still meeting or exceeding the requirement of `N` cables.

# 💡  algorithm structure

- For each midpoint `mid` (possible cable length), we calculate how many cables of length `mid` can be cut from the existing cables.
- If we can cut `N` or more cables, we try longer lengths (move to the right half of the search space).
- If we can't meet the requirement, we try shorter lengths (move to the left half of the search space).

# 💡  code

```python

# https://www.acmicpc.net/problem/1654

K, N = map(int, input().split())
lanes = [int(input()) for _ in range(K)]

start, end = 1, max(lanes)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(lane // mid for lane in lanes)

    if total >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
```

# 💡  time complexity

$O(K \times log(max\_length)$ where `max_length` is the length of the longest cable.

- For each iteration, we calculate how many cables can be made by dividing the existing cables by `mid`. This takes $O(K)$, where `K` is the number of cables.

# 💡  cause of failure

- 

# 💡  fix & alternative approach

- 

```python

```

# 💡  take aways & key points

-