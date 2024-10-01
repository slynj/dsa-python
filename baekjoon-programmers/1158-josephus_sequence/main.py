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

