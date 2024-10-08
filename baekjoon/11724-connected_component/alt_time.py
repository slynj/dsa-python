import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

n, m = map(int, input().split()) 
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

component_count = 0

for i in range(1, n + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        component_count += 1

print(component_count)
