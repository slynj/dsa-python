class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        consecutive = 0

        for n in nums:
            if (n - 1) not in nums:
                count = 1
                while (n + count) in nums:
                    count += 1
                consecutive = max(consecutive, count)
        
        return consecutive

