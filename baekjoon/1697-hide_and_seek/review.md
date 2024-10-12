# 💡  problem analysis & summary

- You need to find the shortest time for수빈 to reach her brother using three possible movements: walking left `(X-1)`, walking right `(X+1)`, or teleporting `(2*X)`.
- Each movement takes 1 second, and the target is to determine the minimum time to move from position

# 💡  algorithm structure

1. **Breadth-First Search (BFS):** This problem can be visualized as finding the shortest path.
2. **Initialization:** Start with initial position and time 0. Use a queue to keep track of positions to explore next, along with the time taken to reach those positions.
3. **Movement Exploration:** For each position, calculate the three possible next positions (X-1, X+1, 2*X). If a position is within bounds and hasn't been visited, add it to the queue.
    - While the queue is not empty, process the current position and explore the three possible moves
    - For each move, check if the new position is within the valid range (0 to 100,000) and hasn't been visited yet.
    - If the sibling's position K is reached, return the current time + 1 as the result.
    - If not, mark the position as visited and add it to the queue with the incremented time.
4. **Termination:** If you reach K, return the time taken.

# 💡  code

```python
from collections import deque

def find_min_time(N, K):
    if N == K:
        return 0
    
    visited = [False] * 100001
    queue = deque([(N, 0)])  # (위치, 걸린 시간)
    visited[N] = True
    
    while queue:
        position, time = queue.popleft()
        
        next_positions = [position - 1, position + 1, position * 2]
        
        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:

                if next_pos == K:
                    return time + 1
                
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

N, K = map(int, input().split())

print(find_min_time(N, K))
```

# 💡  time complexity

`O(N)` 

- where N is the range of possible positions (up to 100,000).
- In the worst case, the algorithm explores each position once, leading to a linear time complexity.

# 💡  cause of failure

- Case where N=K, in which the answer is immediately 0 seconds, as no movement is needed.

# 💡  fix & alternative approach

- 

```python

```

# 💡  take aways & key points

- BFS is effective for finding the shortest path in unweighted graphs, which makes it ideal for problems involving minimal time or distance.
- Correctly tracking visited nodes is crucial to avoid redundant computations and infinite loops.
- Handling edge cases early (like when `N==K`) can simplify the solution and prevent unnecessary computations.