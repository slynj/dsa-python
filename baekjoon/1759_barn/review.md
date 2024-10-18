# 💡  problem analysis & summary

- The problem asks for all possible password combinations using a given set of characters. The password should be of length `L`, selected from `C` given characters. Each password must contain at least one vowel (`a, e, i, o, u`) and at least two consonants. Additionally, the characters in each password must be in lexicographical order.
- The goal is to generate all possible valid passwords that meet these conditions and print them in lexicographical order.

# 💡  algorithm structure

- **Input Parsing**: The first line contains two integers, `L` (password length) and `C` (number of available characters). The second line contains the `C` characters, which are used to form the password.
- **Sorting**: The characters are sorted lexicographically to ensure the generated passwords are in the correct order.
- **Recursive Backtracking**:
    - Use a recursive function to generate all possible combinations of length `L` by selecting characters one by one.
    - At each step, the function adds one character to the current password and moves to the next character.
    - Once the password reaches length `L`, it checks if the password contains at least one vowel and two consonants. If so, the password is saved.
- **Validation**: Each generated password is checked to see if it contains at least one vowel and at least two consonants before being added to the result.
- **Output**: All valid passwords are printed, one per line.

# 💡  code

```python
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
```

# 💡  time complexity

$O(C^L×L)$

- The total time complexity you described is based on the combination formula (CL)\binom{C}{L}(LC), which represents the number of ways to choose `L` items from `C` available characters. The validation for each combination takes `O(L)` time. So the overall complexity is:
    
    $O\left( \binom{C}{L} \times L \right) = O\left( \frac{C!}{L!(C-L)!} \times L \right)$ 
    
- But considering the worst case, you can simplify to:
    
    $\binom{C}{L} \approx O(C^L)$ 
    
- So overall becomes the above

# 💡  cause of failure

- Having a list outside and just recursing withe index and the current password made things a lot more easier.
- Was not able to have the correct final list because I was recursing with the list and was having issues with having password values that were not correct also added to the list.

# 💡  fix & alternative approach

- structure the recursion as:

```python
def password(idx, pwd):
```

# 💡  take aways & key points

- What is okay to be mutated outside
- Time complexixty can be with combinatnios