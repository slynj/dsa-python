# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    ps = []
    for p in prices:
        ps.append([p, 0, True])
        
        for i in range(len(ps)-1):
            ps[i][1] += 1 if ps[i][2] else 0
            ps[i][2] = False if (ps[i][0] > p and ps[i][2]) else ps[i][2]
            
    return ([p[1] for p in ps])