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
