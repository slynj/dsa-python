# https://www.acmicpc.net/problem/2661

def good_sequence(seq):
    length = len(seq)

    for i in range(1, (length // 2) + 1):
        if seq[-i:] == seq[-2*i:-i]:
            return False
    
    return True



def backtrack(seq, N):
    if len(seq) == N:
        print(seq)
        return True
    
    for num in "123":
        if good_sequence(seq + num):
            if backtrack(seq + num, N):
                return True

    return False

N = int(input())
backtrack("", N)
