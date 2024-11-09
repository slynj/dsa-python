# https://neetcode.io/problems/products-of-array-discluding-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        lst = [1] * len(nums)

        pref = 1

        for i in range(len(nums)):
            lst[i] = pref
            pref *= nums[i]
        
        suff = 1

        for i in range(len(nums)-1, -1, -1):
            lst[i] *= suff
            suff *= nums[i]
        
        return lst
