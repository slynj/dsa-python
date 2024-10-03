# 💡  problem analysis & summary

- Determine whether a given string of parentheses is a valid parentheses string (VPS). ⇒ Every open `(` has a corresponding `)`.
- Print "YES" if the string is a valid VPS, otherwise "NO".
- Could be designed in a way to have the flag up and down for every `(` and `)`.

# 💡  algorithm structure

- Stack structure approach to check `(` matching with the `)`.
- Push `(` onto the stack and pop it when a corresponding `)` is encountered.
- If there's no matching `(` when encountering `)`, the string is invalid.
- If the stack is empty after processing the entire string, it is a valid VPS.

# 💡  code

```python
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
```

# 💡  time complexity

`O(n*m)`, where:

- `n` is the number of ps inputs.
- `m` is length of the strings.
- each push and pop are `O(1)`,and we iterate over one string.

# 💡  cause of failure

- not checked when the stack is empty before popping

# 💡  fix & alternative approach

- you could have a counter variable incr/decr for every open and close parenthesis instead of having the typical stack structure.
- this would return `False` faster than my original code.

```python
def is_vps(ps):
    count = 0
    for char in ps:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:  # More closing parentheses than opening
                return False
    return count == 0  # Ensure all opening parentheses are matched

def vps(input_ps):
    results = []
    for ps in input_ps:
        if is_vps(ps):
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input handling
inpt = int(input())  # Read the number of test cases
ps = [input().strip() for i in range(inpt)]  # Read each test case

# Process the test cases and store the results
results = vps(ps)

# Output the results
for result in results:
    print(result)

```

# 💡  take aways & key points

- stack does not necessarily have to be in the typical set up situation with the class, it could just be the idea we process the data with only the functions we need.
- don’t feel pressured to use and always set up the perfect stack “environment” as that’s probably inefficient anyways.