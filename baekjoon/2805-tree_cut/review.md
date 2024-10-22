# 💡  problem analysis & summary

- Given the heights of trees and the required amount of wood `M`, you need to find the maximum height `H` to set on the saw such that the total amount of wood collected is at least `M`.
- Each tree taller than `H` will contribute the portion of its height that exceeds `H` to the wood collected.

# 💡  algorithm structure

- Use binary search to determine the optimal cutting height `H`.
    - Start with bounds: `low=0` and `high=max(tree heights)`.
    - For each middle value, simulate cutting the trees and calculate the total wood collected.
    - Adjust bounds based on whether the wood collected is sufficient.
- For a given height `H`, iterate through each tree. If the tree's height is greater than `H`, add the difference tree height−`H` to the total wood collected.

# 💡  code

```python
# https://www.acmicpc.net/problem/2805

def wood_collected(trees, height):
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height
    return total

def find_max_height(trees, M):
    low, high = 0, max(trees)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        total_wood = wood_collected(trees, mid)
        
        if total_wood >= M:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(find_max_height(trees, M))
```

# 💡  time complexity

$O(Nlog(max(tree heights)))$

 where `N` is the number of trees.

- The binary search on the possible cutting height has a time complexity of $O(log(max(tree heights)))$.
- For each binary search step, calculating the wood collected involves iterating over the `N` trees, which takes $O(N)$.

# 💡  cause of failure

- 

# 💡  fix & alternative approach

- 

```python

```

# 💡  take aways & key points

- edge cases-when the required wood is exactly equal to the total wood available