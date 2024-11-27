# 💡Approach

### edge cases

### brainstorm

- Bruteforce
    - Try all possible eating speeds from 1 to the maximum pile size.

### plan

### time complexity

$O(n \cdot logm)$

- **Binary search:** `O(logm)`, where m is the maximum pile size.
- **Iteration:** `O(n)`, where n is the number of piles

### space complexity

$O(1)$

- No additional space

# 💡 Problem Analysis

### summary

- Find the minimum eating speed `k` such that all bananas are eaten within `h` hours. Use binary search to minimize `k`.

### code

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
```

### alternative approach

```python

```

### cause of failure

### take aways & key points

- Initialize `l` to 1 and `r` to the maximum pile size, representing the range of possible eating speeds.
- Use binary search to find the minimum `k`:
    - Calculate `k = (l + r) // 2`.
    - Compute the total time needed at speed `k`.
    - If the total time is within `h`, adjust `r` to `k - 1` and update the result.
    - Otherwise, increase `l` to `k + 1`.
- Return the minimum value of `k`.

# 💡 One Line Summary

<aside>
📌

Use binary search → calculate eating speed k → check if total time ≤ h using k → adjust search range l or r → return minimum k

</aside>