# alt approach by gpt: (returns false faster)

# 31120 kb
# 44 ms

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
