# 💡Approach

### edge cases

- 1 element list ⇒ 0
- All same values ⇒ 0

### brainstorm

- Bruteforce
    - for every element, check the rest of the elements if they are any numbers that are greater than current number
- Sliding Window
    - have 2 pointers at the start (0, 1)
    - then move the pointers to the back and compare

### plan

- have `l` ptr at index 0, `r` ptr at index 1
- move the `r` ptr to the right
- move `l` only when the value of `prices[l] > prices[r]` since that means the current value is higher than the right one (meaning that it can’t cause any max revenue)

### time complexity

$O(n)$

- You are going through the array once, comparing everything on the spot with pointers

### space complexity

$O(1)$

- No additional storage

# 💡 Problem Analysis

### summary

- given a list of numbers, return the max revenue if the numbers represent the price of the stocks

### code

```python
# https://neetcode.io/problems/buy-and-sell-crypto

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0

        while (l < r and r < len(prices)):
            if prices[l] > prices[r]: 
                l = r
            else:
                maxP = max(maxP, prices[r] - prices[l])

            r += 1
        
        return maxP
```

### alternative approach

`DP`

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
        
# TC: O(n)
# SC: O(1)
```

### cause of failure

```python
# WRONG!
if prices[l] > prices[r]: 
    l += 1

# SOLUTION:
if prices[l] > prices[r]: 
    l = r
```

- I added one to the left pointer thinking that it would work as it moves one to the right
- however it needs to move all the way to the right as that would be the lowest point to start at

### take aways & key points

- `Sliding Window` : 2 Pointers are pointers at each ends, sliding window is pointer at the first one and wherever the second one needs to be at

# 💡 One Line Summary

<aside>
📌

have 2 ptrs pointing at the first 2 elements → when the right ptr value is smaller than current value, update l = r bc we would rather wait and buy cheaper → update max 

</aside>