# 모든 경기를 나열 (6개국의 경기 조합)
# [
#  (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),  
#  (1, 2), (1, 3), (1, 4), (1, 5),  
#  (2, 3), (2, 4), (2, 5),  
#  (3, 4), (3, 5),  
#  (4, 5)
# ]

matches = [(i, j) for i in range(6) for j in range(i + 1, 6)]

def backtrack(idx, wins, draws, losses):
    # 모든 경기를 확인했다면
    if idx == len(matches):
        # 모든 팀의 승, 무, 패가 0이어야 함
        return all(w == 0 and d == 0 and l == 0 for w, d, l in zip(wins, draws, losses))

    team1, team2 = matches[idx]

    # 1. team1 승리, team2 패배
    if wins[team1] > 0 and losses[team2] > 0:
        wins[team1] -= 1
        losses[team2] -= 1
        if backtrack(idx + 1, wins, draws, losses):
            return True
        wins[team1] += 1
        losses[team2] += 1

    # 2. team1과 team2 무승부
    if draws[team1] > 0 and draws[team2] > 0:
        draws[team1] -= 1
        draws[team2] -= 1
        if backtrack(idx + 1, wins, draws, losses):
            return True
        draws[team1] += 1
        draws[team2] += 1

    # 3. team1 패배, team2 승리
    if losses[team1] > 0 and wins[team2] > 0:
        losses[team1] -= 1
        wins[team2] -= 1
        if backtrack(idx + 1, wins, draws, losses):
            return True
        losses[team1] += 1
        wins[team2] += 1

    # 모든 경우가 실패하면 False
    return False

# 네 가지 입력 세트 처리
for _ in range(4):
    data = list(map(int, input().split()))
    wins = data[0::3] 
    draws = data[1::3]  
    losses = data[2::3] 

    if sum(wins) + sum(draws) + sum(losses) != 30:  # 총 경기 수가 15 * 2 이어야 함 (승 + 무 + 패 = 30)
        print(0, end=" ")
    else:
        if backtrack(0, wins, draws, losses):
            print(1, end=" ")
        else:
            print(0, end=" ")
