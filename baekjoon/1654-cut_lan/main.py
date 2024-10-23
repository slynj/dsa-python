# https://www.acmicpc.net/problem/1654

K, N = map(int, input().split())
lanes = [int(input()) for _ in range(K)]

start, end = 1, max(lanes)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(lane // mid for lane in lanes)

    if total >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
