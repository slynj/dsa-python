# https://www.acmicpc.net/problem/9012
# 31120	kb
# 40 ms

# maybe try using class?

def is_vps(ps):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def vps(input_ps):
    results = []
    for ps in input_ps:
        if is_vps(ps):
            results.append("YES")
        else:
            results.append("NO")
    return results

inpt = int(input())
ps = [input().strip() for i in range(inpt)] 

results = vps(ps)

for result in results:
    print(result)



