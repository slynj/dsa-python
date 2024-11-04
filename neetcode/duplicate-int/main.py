# https://neetcode.io/problems/duplicate-integer

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for _ in range(len(nums)):
            x = nums.pop(0)
            if x in nums:
                return True
        return False