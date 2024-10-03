# 💡  problem analysis & summary

- eliminating every `k`th person in a circular arrangement. return the elimination sequence of `n` people.

# 💡  algorithm structure

- Brainstormed to used circular queue as the arrangements are ciruclar.
- Initialize the list with people numbered from 1 to `n`.
- Use a circular elimination approach where the current index moves K steps forward after each removal, wrapping around using modular arithmetic.
- Remove the person at the calculated index and repeat until the list is empty.
- Return the order of eliminations.

# 💡  code

```python
# https://www.acmicpc.net/problem/1158

class Josephus:
    def __init__(self, n, k):
        self.n = n 
        self.k = k
        self.seq = list(range(1, n + 1))  
        self.result = [] 
        self.index = 0 

        
    def remove(self):
        while self.seq:
            self.index = (self.index + self.k - 1) % len(self.seq)
            self.result.append(self.seq.pop(self.index))

        return self.result

n, k = map(int, input().split())
josephus = Josephus(n, k)
sequence = josephus.remove()

# maybe using map?
result_string = ", ".join([str(num) for num in sequence])
print("<" + result_string + ">")
```

# 💡  time complexity

- iterates through the list of `n` people and removes each person one by one.
- removing an element from a list ⇒ `O(n)`
- since we do this for every person, the total time complexity is `O(n^2)` , where `n` is a number of people

# 💡  cause of failure

- Was not printing with the correct format
- had the wrong index calculation at first

# 💡  fix & alternative approach

- Maybe I could've done this more efficiently where I check the last remaining people under the amount of people I need to remove.
- Also could’ve used mapping for printing at the end.

```python
print("<" + ", ".join(map(str, sequence)) + ">")
```

# 💡  take aways & key points

- Modular arithmetic `%` is key in circular problems like the Josephus problem to wrap around the list efficiently.