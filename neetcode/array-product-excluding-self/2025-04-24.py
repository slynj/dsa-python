class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for n in nums]
        product = 1

        for i in range(len(nums)):
            res[i] *= product
            product *= nums[i]
        
        product = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= product
            product *= nums[i]

        return res

