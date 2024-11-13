# https://neetcode.io/problems/two-integer-sum-ii
          
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         for n in numbers:
            if (target - n) in numbers:
                return [numbers.index(n) + 1, numbers.index(target-n) + 1]