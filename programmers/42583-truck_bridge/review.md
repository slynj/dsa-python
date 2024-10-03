# 💡  problem analysis & summary

- Bridge can hold `bridge_length` amount of cars and has a maximum weight limit `weight`, we need to calculate the minimum time ****for all trucks to cross the bridge.
- It was confusing for me to recognize that in order to pass the bridge, you need to actually go through all the “lengths” of the bridge.
- Trucks enter the bridge in a given order `truck_weights`, and the bridge can hold multiple trucks simultaneously, but the total weight of the trucks must not exceed the limit.
- The goal is to simulate the process of trucks crossing the bridge while accounting for the bridge’s weight limit and length, determining the minimum time required.

# 💡  algorithm structure

- Recognize that `queue` was needed for this case since I want to modify the start and the end of the data structure at a `O(1)` time complexity.
- Also was using the FIFO, so had to be `queue`
- Bridge represented with a `queue` using deque, have a variable for the current weight and the time.
- For every second, increment `time`. Shift trucks on the bridge queue by removing the leftmost truck from the and update the `current_weight`.
- If there are waiting trucks and the bridge can support the next truck’s weight, add it to the `deque`. Otherwise, append `0` to indicate an empty space.
- Repeat until all trucks have crossed the bridge and no trucks remain on the bridge.
- The loop ends when there are no more trucks on the bridge and no trucks left to enter the bridge.

# 💡  code

```python
# allows you to add left, pop left with O(1) complexity
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    current_weight = 0
    time = 0
    
    truck_weights = deque(truck_weights)
    
    while truck_weights or current_weight > 0:
        time += 1
        
        truck_out = bridge.popleft()
        current_weight -= truck_out
        
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck_in = truck_weights.popleft()
                bridge.append(truck_in)
                current_weight += truck_in
            else:
                bridge.append(0)
    
    return time
```

# 💡  time complexity

`O(n)`, where `n` is the number of trucks, ie:`len(truck_weights)`

- Each truck enters and exits the bridge exactly once, resulting in a linear time complexity.

# 💡  cause of failure

- Trucks need to fully exit the bridge instead of just “leaving” ⇒ it needs to go through the whole lenght of the bridge

# 💡  fix & alternative approach

- Initialized the dequeue so that it has that many length at the first place instead of appending each trucks.

# 💡  take aways & key points

- Using  `deque` is important for efficiently.
- Simulation problems often require carefully tracking the state of all variables at each step to avoid errors.