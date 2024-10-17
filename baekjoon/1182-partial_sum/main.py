# https://www.acmicpc.net/problem/1182


def sum(idx, current_sum):
    global count

    if (idx == length):
        return
    
    current_sum += lst[idx]

    if (current_sum == s):
        count += 1
    
    sum(idx + 1, current_sum)

    # not selecting current one
    sum(idx + 1, current_sum-lst[idx])


length, s = map(int, input().split())

lst = list(map(int, input().split()))

count = 0

sum(0, 0)

print(count)