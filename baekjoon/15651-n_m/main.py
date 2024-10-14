# https://www.acmicpc.net/problem/15651

def backtrack(sequence, N, M):
    # Base case: if the sequence length is M, print the sequence
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    # Try every number from 1 to N
    for i in range(1, N + 1):
        sequence.append(i)  # Choose the number
        backtrack(sequence, N, M)  # Recur to form the next part of the sequence
        sequence.pop()  # Backtrack to try another number

N, M = map(int, input().split()) 
backtrack([], N, M) 

