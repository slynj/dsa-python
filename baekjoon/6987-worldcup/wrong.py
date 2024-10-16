# https://www.acmicpc.net/problem/6987



def wordlcup(W, D, L):
    if sum(W) != sum(L): return 0

    dr = 0

    for d in D:
        dr += d if dr <= 0 else -d


    print(dr)
    
    return int(dr == 0)

W = [[], [], [], []]
D = [[], [], [], []]
L = [[], [], [], []]

for j in range(4):
    inp = list(map(int, input().strip().split()))

    for i in range(18):
        if i % 3 == 0:
            W[j] += [inp[i]] 
        elif i % 3 == 1:
            D[j] += [inp[i]]
        else:
            L[j] += [inp[i]]
result = []

for i in range(4):
    result.append(wordlcup(W[i], D[i], L[i]))


print(' '.join(map(str, result)))


