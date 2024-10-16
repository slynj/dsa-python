# 💡  problem analysis & summary

- Given the final match results (wins, draws, losses) of 6 teams in a round-robin tournament where each team plays exactly 5 matches. The challenge is to determine whether the given match results are possible.
    - Each team has played against every other team exactly once, resulting in a total of 15 matches.
    - We need to check if the given results (wins, draws, and losses for each team) can be achieved through valid match outcomes.

# 💡  algorithm structure

1. **Input Parsing**:

- We receive the results for 6 teams, with each team having a number of wins, draws, and losses.
- The input consists of 18 values per test case (6 teams × 3 values for each team).

2. **Backtracking**:

- Each pair of teams will be involved in exactly one match.
- The total number of matches between 6 teams is 15 (since each team plays 5 matches).
- We store these matchups as a set in a `matches` list.
    - `matches = [(0, 1), (0, 2), ..., (4, 5)]` (all possible team combinations).
- For each match between two teams:
    1. Team 1 wins, and Team 2 loses.
    2. Team 2 wins, and Team 1 loses.
    3. Both teams draw.
- We recursively simulate all possible outcomes of matches using backtracking. After every match, we adjust the corresponding wins, draws, and losses, and we explore the next match.
- **Base Case** is when all matches have been processed (15), we check if the number of wins, draws, and losses for all teams has been reduced to 0. If so, the results are valid.

3. **Backtracking Function**:

- **Input Parameters**:
    - `idx`: current match being simulated.
    - `wins`, `draws`, `losses`: lists representing the remaining wins, draws, and losses for each team.
- **Recursive Logic**:
    - If all matches are simulated (`idx == 15`), check if all teams have 0 wins, draws, and losses left. Return `True` if valid, otherwise `False`.
    - For the current match (between team `i` and team `j`):
        1. Try case where `i` wins and `j` loses.
        2. Try case where `i` loses and `j` wins.
        3. Try case where both teams draw.
        - If any valid result is found, return `True`.
        - If no valid outcome exists, backtrack and restore the previous state.

4. **Output**:

- For each test case, output `1` if the match results are valid and `0` otherwise.

# 💡  code

- Only checks if the number of wins are equal to losses and if the draws happen the right amount of time.
- Need to check other cases, missing recursive approach.

```python
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

```

# 💡  time complexity

$O(3^{15})$

- Each match has 3 possible outcomes and there are 15 matches to simulate

# 💡  cause of failure

- You need to check all the possible cases, not only the trivial ones.
- One case partially working or failing does not determine everything, you just do a recursive call.
- The whole structure I was making was wrong T.T
- Check at the end if they sum of to 30 because that’s how many games that is being played.

# 💡  fix & alternative approach

- Structured where you check ALL cases

```python
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

```

# 💡  take aways & key points

- List indexing (start from 1, every 3 = `[1::3]`)
- Recursion structure, think about it before start coding
- Determine the base case before structuring
- Think about all the edge cases