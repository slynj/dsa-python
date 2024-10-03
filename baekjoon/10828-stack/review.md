# 💡problem analysis & summary

- get input and basically perform stack operations
- print out the results for certain operations

# 💡algorithm structure

- pretty obvious from the title that it’s a stack
- created a stack class with pop, push, size, is_empty, and top
- made the class method to print it, but it might’ve been better to print at the end later?

# 💡code

```python
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, value):
    self.stack.append(value)

  
  def pop(self):
    if not self.is_empty():
      print(self.stack.pop())
    else:
      print(-1)

  
  def top(self):
    if not self.is_empty():
      print(self.stack[-1])
    else:
      print(-1)
      
  
  def is_empty(self):
    return self.size() == 0

  
  def size(self):
    return len(self.stack)

n = int(input())
stack = Stack()
data = []

for i in range(n):
  data.append(input())

for d in data:
  ds = d.split(" ")

  if ds[0] == "push":
    stack.push(ds[1])
  elif ds[0] == "pop":
    stack.pop()
  elif ds[0] == "top":
    stack.top()
  elif ds[0] == "empty":
    print(int(stack.is_empty()))
  else:
    print(stack.size())
```

# 💡time complexity

- O(n), where n is the number of input lines
- iterating once per the line
- all the methods in the stack class is O(1)

# 💡 cause of failure

- understood the question wrong, I thought I had to print right after the input but you had to print everything after getting all the inputs

# 💡 fix & alternative approach

- fixed the first mistake by getting all the inputs and putting it in the list

```python
data = []

for i in range(n):
  data.append(input())
```

- alt soln by gpt, it’s 40ms which is about 5 times faster than mine.
- uses sys library which is faster at getting inputs

```python
import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else -1

    def top(self):
        return self.stack[-1] if not self.is_empty() else -1

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Read all input at once
input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
stack = Stack()
result = []

for i in range(1, n + 1):
    cmd = data[i]

    if cmd[:4] == "push":
        stack.push(int(cmd[5:]))
    elif cmd == "pop":
        result.append(str(stack.pop()))
    elif cmd == "top":
        result.append(str(stack.top()))
    elif cmd == "empty":
        result.append(str(int(stack.is_empty())))
    elif cmd == "size":
        result.append(str(stack.size()))

# Output all results at once
sys.stdout.write("\n".join(result) + "\n")

```

# 💡 take aways & key points

- substrings are less efficient than splitting