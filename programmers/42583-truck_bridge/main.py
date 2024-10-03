# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3

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
