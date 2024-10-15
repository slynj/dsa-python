# https://www.acmicpc.net/problem/15663

def backtrack(sequence, path, N, M, visited):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return

    prev = -1
    for i in range(N):
        if not visited[i] and sequence[i] != prev:
            visited[i] = True
            backtrack(sequence, path + [sequence[i]], N, M, visited)
            visited[i] = False
            prev = sequence[i]

N, M = map(int, input().split())
sequence = list(map(int, input().split()))

sequence.sort()
visited = [False] * N
backtrack(sequence, [], N, M, visited)
