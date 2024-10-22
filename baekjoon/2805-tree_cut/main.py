# https://www.acmicpc.net/problem/2805

def wood_collected(trees, height):
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height
    return total

def find_max_height(trees, M):
    low, high = 0, max(trees)
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        total_wood = wood_collected(trees, mid)
        
        if total_wood >= M:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(find_max_height(trees, M))
