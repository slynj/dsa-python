# 💡  problem analysis & summary

- Given a list of stock pricing, return the list of the number of seconds that the price did NOT go down for.
- Once the price drops, the “number of seconds” does not change.
- The last pricing is automatically set to 0 seconds as it cannot rise or drop.

# 💡  example

<aside>
<img src="/icons/arrow-right-line_gray.svg" alt="/icons/arrow-right-line_gray.svg" width="40px" />

[2, 2, 5, 1, 3, 0]

</aside>

<aside>
<img src="/icons/sign-out_gray.svg" alt="/icons/sign-out_gray.svg" width="40px" />

[3, 2, 1, 2, 1, 0]

</aside>

<aside>
<img src="/icons/arrow-right-line_gray.svg" alt="/icons/arrow-right-line_gray.svg" width="40px" />

[2, 2, 3, 1, 5]

</aside>

<aside>
<img src="/icons/sign-out_gray.svg" alt="/icons/sign-out_gray.svg" width="40px" />

[3, 2, 1, 1, 0]

</aside>

# 💡  algorithm structure

- Nested list with 3 elements: `price`, `seconds`, `is_set`
    - `price` is the price of the stock
    - `seconds` is how long it didn’t go down for
    - `is_set` is if the seconds can be modified (ie. did it ever drop)
- 2 for loops iterating through the given list, and the list prior to it for every element.
- If the element `price` is greater that the current `price` , `is_set` is set to `False` and there are no more modification to the `seconds`.
    - Otherwise, if the `is_set` is `True`, add 1 to `seconds`

# 💡  code

<aside>
⚠️

did not pass the efficiency test — timeout

</aside>

```python
def solution(prices):
    ps = []
    for p in prices:
        ps.append([p, 0, True])
        
        for i in range(len(ps)-1):
            ps[i][1] += 1 if ps[i][2] else 0
            ps[i][2] = False if (ps[i][0] > p and ps[i][2]) else ps[i][2]
            
    return ([p[1] for p in ps])
```

# 💡  time complexity

- `O(n^2)`, where `n` is the number of elements in the given list `prices`

# 💡  cause of failure

### 1. Logic to update `is_set`

- I had trouble with the logic inside the second for loop.
- My initial code was:
    
    ```python
    ps[i][2] = False if (ps[i][0] > p) else True
    ```
    
- This was wrong because I had to check if `is_set` was `True` first, and change the bool value iff it is true (as if its set, you don’t change)
- There was also an issue with the else, since I just made it `True` every time the condition wasn’t met. Setting it back to `True` every time made it no point of having the bool.

### 2. Efficiency

- The code above and my original logic did pass all the test cases, but it did not pass any of the time complexity requirements.

# 💡  fix & alternative approach

- Alternative approaches that meets the time requirement:

<aside>
<img src="/icons/clock_gray.svg" alt="/icons/clock_gray.svg" width="40px" />

$O(n^2)$, where `n` is the length of the list

</aside>

```python
# meets the time requirements

def solution(prices):
    answer = []

    for i in range(len(prices)):
        time = 0

        for j in range(i+1, len(prices)):
            time += 1
            if prices[i] > prices[j]:
                break
        
        answer.append(time)
        
		return answer
```

- **Outer loop**
    
    This loop runs `n` times, where `n` is the length of the `prices` list.
    
- **Inner loop**
    
    $(n−1)+(n−2)+(n−3)+...+1+0=n(n−1)2(n-1) + (n-2) + (n-3) + ... + 1 + 0 = \dfrac{n(n-1)}{2}$
    
    Proportional to `O(n^2)`
    
- the overall BigO time complexity is the same, but my approach takes up more memory as you are saving more things in the array, and constantly accessing the nested elements.

<aside>
<img src="/icons/clock_gray.svg" alt="/icons/clock_gray.svg" width="40px" />

$O(n)$, where `n` is the length of the list

</aside>

```python
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
          while stack != [] and stack[-1][1] > prices[i]:
              past, _ = stack.pop()
              answer[past] = i - past
        stack.append([i, prices[i]])
        
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
        
    return answer
```

- You first initialize the empty stack, then make a list with the length of `n`
- Loop through each prices (just index)
    - for each price, we check if its lower than the price at the index stored at the top of the stack (`stack[-1][1]`)
    - then we find the point where it dropped
    - then pop the top element and store the index
    - then store how many “steps” it took to find the dropping point.
- Then, we calculate the cases it hasn’t dropped as the first for loop only checks for the ones that have dropped.

# 💡  take aways & key points

- Same BigO does not necessarily mean they are the same efficiency
- You do not necessarily need to save all the info you check as a data structure, try to compute them and get it “done” with instead of holding on to them