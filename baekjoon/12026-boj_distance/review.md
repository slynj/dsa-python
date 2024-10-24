# 💡  problem analysis & summary

- Compute the minimum energy required for a character (starting at the first block labeled `B`) to jump from one end of a sequence of blocks (labeled with `B`, `O`, or `J`) to the other end (the last block).
- The character can only jump according to a strict order: `B` → `O` → `J` → `B`… repeating. Each jump requires an amount of energy equal to the square of the number of blocks jumped over.
- The goal is to minimize the total energy required for the character to reach the last block. If it is impossible to reach the last block following the required sequence, the output should be `1`.

# 💡  algorithm structure

**Dynamic Programming (DP) Approach**

- Use an array `dp` where `dp[i]` represents the minimum energy required to reach block `i`.
- Initialize `dp[0] = 0` since no energy is required to start at block 1.
- Set other entries in `dp` to infinity (`float('inf')`) initially, meaning they haven't been reached yet.
- Loop through each block, and for each block `i`, check all blocks `j` (where `j > i`) to see if it's the next valid block in the sequence (according to the rule: `B` → `O` → `J`).
- If valid, calculate the energy required to jump from `i` to `j` and update `dp[j]` to the minimum value.
- After the loop, check the value of `dp[n-1]` (last block). If it's still infinity, return `1` (indicating the last block is unreachable), otherwise, return `dp[n-1]` as the result.

# 💡  code

```python
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

```

# 💡  time complexity

$O(N^2)$

- The time complexity of this approach is **`O(N^2)`** because, for each block `i`, we potentially check every block `j` that comes after it (`j > i`).
- In the worst case, this leads to approximately `N * (N-1) / 2` comparisons, which simplifies to **`O(N^2)`**.

# 💡  cause of failure

- Was unable to come up with the DP structure after reading the problem

# 💡  fix & alternative approach

- 

```python

```

# 💡  take aways & key points

- 
- For large inputs, brute-force approaches can be inefficient.
-