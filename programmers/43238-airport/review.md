# 💡  problem analysis & summary

- We need to find the minimum time required for `n` people to complete immigration checks at multiple booths, where each booth takes different times to process one person.
- Given that each person can only be processed by one booth at a time, we must optimize the distribution of people across booths to minimize the total waiting time.

# 💡  algorithm structure

- Basically we are checking how many people they can screen within the given minute.
- Set the min time to 1, max to the longest time * number of people
- Then we keep on checking the midpoint time of that and see how many people they can screen within that time span.
- Ex. 60 min → 30 min → 15 min → etc
- If the current time is sufficient to process `n` people, reduce the time (`mid`).
- If the current time is insufficient, increase the time.
- Continue the binary search until the optimal time is found.

# 💡  code

```python
def solution(n, times):
    low = 1
    high = max(times) * n
    answer = high
    
    while low <= high:
        mid = (low + high) // 2
        total = 0
        
        for t in times:
            total += mid // t
        
        if total >= n:
            answer = mid
            high  = mid - 1
        else:
            low = mid + 1
    
    return answer
```

# 💡  time complexity

$O(m * log(n * max(times)))$

where m is the number of booths, and 

- Between `1` and `n * max(times)`
- Since we use binary search, the time complexity for this part is `O(log(n * max(times)))`.
- For each iteration of binary search, we go through each time value in `times` to calculate how many people can be processed. This is `O(m)` where `m` is the number of booths.
- Overall time complexity is `O(m * log(n * max(times)))`

# 💡  cause of failure

- 

# 💡  fix & alternative approach

- 

```python

```

# 💡  take aways & key points

- You had think about it from a diff perspective
- Initial approach was choosing the booths and it felt impossible to binary search on that