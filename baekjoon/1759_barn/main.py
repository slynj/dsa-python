# https://www.acmicpc.net/problem/1759

vowles = {'a', 'e', 'i', 'o', 'u'}

L, C = map(int, input().split())
chars = input().split()

chars.sort()

result = []

def password(idx, pwd):
    if len(pwd) == L:
        numv = sum(1 for char in pwd if char in vowles)
        numc = L - numv

        if numv >= 1 and numc >= 2:
            result.append(''.join(pwd))
        
        return
    
    for i in range(idx, C):
        password(i + 1, pwd + [chars[i]])

password(0, [])

for r in result:
    print(r)