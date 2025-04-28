class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sstr = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in sstr:
                sstr.remove(s[l])
                l += 1
            sstr.add(s[r])
            res = max(res, r - l + 1)
        
        return res

