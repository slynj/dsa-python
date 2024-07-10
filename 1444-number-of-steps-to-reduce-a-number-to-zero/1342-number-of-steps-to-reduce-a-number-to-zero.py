class Solution:
    
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            steps += 1
            num = num / 2 if (num % 2 == 0) else num - 1
        return steps
    #     return self.recur(num, 0)
        
    # def recur(self, num, steps):
    #     if (num == 0): 
    #         return steps
    #     elif (num % 2 == 0): 
    #         return self.recur(num/2, steps+1)
    #     else:
    #         return self.recur(num-1, steps+1)
            
    
