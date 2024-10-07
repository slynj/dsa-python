# https://www.acmicpc.net/problem/1260

from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# Input parsing
n, m, v = map(int, input().split())  
graph = [[] for _ in range(n + 1)]

# Read the edges
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Sort the adjacency list to visit nodes in increasing order
for i in range(1, n + 1):
    graph[i].sort()

# DFS
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()

# BFS
visited = [False] * (n + 1)
bfs(graph, v, visited)
print()