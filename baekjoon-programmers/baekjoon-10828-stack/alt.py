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
