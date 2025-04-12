class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = int((l + r)/2)
        res = float("infinity")

        if r < 1: return nums[0]

        while l <= r:
            res = min(res, nums[m])

            if nums[l] < nums[r]:
                res = min(res, nums[l])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            
            
            m = int((l + r)/2)
        
        return res

        
