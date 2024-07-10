class Solution:
    
    def numberOfSteps(self, num: int) -> int:
        return self.recur(num, 0)
        
    def recur(self, num, steps):
        if (num == 0): 
            return steps
        elif (num % 2 == 0): 
            return self.recur(num/2, steps+1)
        else:
            return self.recur(num-1, steps+1)
            
    