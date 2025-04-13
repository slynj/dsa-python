class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minNum = float("infinity")

        while l <= r:
            m = (l + r) // 2

            minNum = min(minNum, nums[m])

            if nums[l] < nums[r]:
                minNum = min(nums[l], minNum)
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return minNum
