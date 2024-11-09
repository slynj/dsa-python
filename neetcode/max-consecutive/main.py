# https://neetcode.io/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        m = max(nums)
        n = min(nums)

        h = {}

        for i in range(n, m + 1):
            h[i] = 0
        
        for n in nums:
            h[n] += 1
        
        c = 0
        cmax = 0

        lst = h.values()

        for l in lst:
            c = c + 1 if l != 0 else 0
            cmax = c if c > cmax else cmax

        return cmax