# https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3

def solution(n, times):
    low = 1
    high = max(times) * n
    answer = high
    
    while low <= high:
        mid = (low + high) // 2
        total = 0
        
        for t in times:
            total += mid // t
        
        if total >= n:
            answer = mid
            high  = mid - 1
        else:
            low = mid + 1
    
    return answer