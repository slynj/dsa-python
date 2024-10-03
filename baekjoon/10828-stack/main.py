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