# https://www.acmicpc.net/problem/15663

def backtrack(sequence, path, N, M, used):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return

    for i in range(N):
        if not used[i]:
            if i > 0 and sequence[i] == sequence[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            backtrack(sequence, path + [sequence[i]], N, M, used)
            used[i] = False

N, M = map(int, input().split())
sequence = list(map(int, input().split()))

sequence.sort() 
used = [False] * N
backtrack(sequence, [], N, M, used)