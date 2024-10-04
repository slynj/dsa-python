# https://www.acmicpc.net/problem/1966
# 34068 kb
# 60 ms

from collections import deque

def printer_queue(n, m, priorities):
    queue = deque([(i, priority) for i, priority in enumerate(priorities)])
    count = 0 
    
    while queue:
        current = queue.popleft()
        
        if any(current[1] < item[1] for item in queue):
            queue.append(current)
        else:
            count += 1
            if current[0] == m:
                return count

test_cases = int(input())
results = []

for _ in range(test_cases):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    results.append(printer_queue(n, m, priorities))

for result in results:
    print(result)
