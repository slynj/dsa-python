# https://www.acmicpc.net/problem/15663

def backtrack(sequence, path, N, M, visited):
    # base case
    if len(path) == M:
        print(' '.join(map(str, path)))
        return

    prev = -1
    for i in range(N):
        # number that hasn't ben selected
        # and a number that is not same as the prev one (since it's sorted)
        if not visited[i] and sequence[i] != prev:
            visited[i] = True
            backtrack(sequence, path + [sequence[i]], N, M, visited)
            # reset after backtracking is finished
            visited[i] = False
            prev = sequence[i]

N, M = map(int, input().split())
# need the list() because map() returns a map obj
sequence = list(map(int, input().split()))

sequence.sort()
visited = [False] * N
backtrack(sequence, [], N, M, visited)
